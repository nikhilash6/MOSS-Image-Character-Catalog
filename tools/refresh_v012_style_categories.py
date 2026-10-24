"""7-Zip-only selective update; verify all images and preserve old Release assets."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import shutil
import struct
import subprocess
import zipfile

from style_category_patch import patch_js, patch_html

ROOT = Path(__file__).resolve().parents[1]
REPO = 'ukr8b3g-cmyk/MOSS-Image-Character-Catalog'
RELEASE_ID = 421022122
BASE_ID = 672077605
SUM_ID = 672077606
BASE_SHA = '4e234dd18959ab0efd8db4898600c29dd768591f27e8119a3fa4d0dbb9d6ba69'
SUM_SHA = '2bdb64438876895121641ed201de2cd5c14f85a96dbc37aed48a349026868b03'
UI_BEFORE = '5b5569643d1c5817c5c3b8a229f592857ebf6e26603227713e4fabceb3544499'
UI_AFTER = '12ce1b6ad24b528b6b7f818de08e0c71e657eb4e92c7e4cc80b2326eeffd2563'
HTML_AFTER = 'e295c3df6880f2fa373c2d20d701e3caf83af6e3bb2dfd4e5f36dd689b066284'
PREFIX = 'MOSS-Image-Character-Catalog/'
NAME = 'MOSS-Image-Character-Catalog-v0.1.2.zip'
STAGED_NAME = NAME.replace('.zip', '-style-categories.zip')
OLD_NAME = NAME.replace('.zip', '-before-style-categories.zip')
SUM_STAGED = 'SHA256SUMS-style-categories.txt'
SUM_OLD = 'SHA256SUMS-before-style-categories.txt'
DOCS = ['README.md', 'README.ja.md', 'docs/releases/v0.1.2.md', 'docs/STYLE_CATEGORIES.md', 'docs/STYLE_CATEGORIES.ja.md', 'docs/style-categories.csv', 'docs/style-categories.json']


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def compressed_digest(stream, info):
    stream.seek(info.header_offset)
    header = stream.read(30)
    if header[:4] != b'PK\x03\x04':
        raise ValueError('Unexpected ZIP local header')
    name_size, extra_size = struct.unpack_from('<HH', header, 26)
    stream.seek(name_size + extra_size, 1)
    remaining = info.compress_size
    h = hashlib.sha256()
    while remaining:
        chunk = stream.read(min(remaining, 1024 * 1024))
        if not chunk:
            raise ValueError('Truncated ZIP payload')
        h.update(chunk); remaining -= len(chunk)
    return h.digest()


def build(base, output, sevenzip):
    if digest(base) != BASE_SHA:
        raise ValueError('Current published source ZIP hash mismatch')
    output.mkdir(parents=True, exist_ok=True)
    target = output / STAGED_NAME
    if target.exists():
        raise FileExistsError(target)
    with zipfile.ZipFile(base) as archive:
        raw = archive.read(PREFIX + 'app/review/review.js')
        raw_html = archive.read(PREFIX + 'app/review/index.html')
    assert hashlib.sha256(raw).hexdigest() == UI_BEFORE
    patched = patch_js(raw)
    patched_html = patch_html(raw_html)
    assert hashlib.sha256(patched).hexdigest() == UI_AFTER
    assert hashlib.sha256(patched_html).hexdigest() == HTML_AFTER
    replacements = {'app/review/review.js': patched,'app/review/index.html':patched_html}
    replacements.update({name: (ROOT / name).read_bytes() for name in DOCS})
    stage = output / 'stage'
    for name, content in replacements.items():
        path = stage / PREFIX / name
        path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(content)
    listing = output / 'update-files.txt'
    listing.write_text('\n'.join(PREFIX + name for name in replacements) + '\n', encoding='utf-8')
    shutil.copy2(base, target)
    # Preserve all non-selected entries and force replacement of selected ones,
    # regardless of timezone or source/archive timestamp differences.
    subprocess.run([sevenzip, 'u', '-tzip', '-mm=Deflate', '-mx=5', '-scsUTF-8', '-up1q1r2x2y2z2w2', str(target), '@' + str(listing)], cwd=stage, check=True)
    subprocess.run([sevenzip, 't', str(target)], check=True)
    with zipfile.ZipFile(base) as old, zipfile.ZipFile(target) as new, base.open('rb') as old_stream, target.open('rb') as new_stream:
        a = {item.filename: item for item in old.infolist()}
        b = {item.filename: item for item in new.infolist()}
        assert len(a) == len(old.infolist()) == 136695
        assert len(b) == len(new.infolist()) == 136699
        assert set(b) == set(a) | {PREFIX + name for name in replacements}
        unchanged = 0
        for name, item in b.items():
            relative = name.removeprefix(PREFIX)
            if relative in replacements:
                assert new.read(name) == replacements[relative], name
            else:
                previous = a[name]
                assert (previous.CRC, previous.file_size, previous.compress_size, previous.compress_type) == (item.CRC, item.file_size, item.compress_size, item.compress_type), name
                assert compressed_digest(old_stream, previous) == compressed_digest(new_stream, item), name
                unchanged += 1
        rows = json.loads(new.read(PREFIX + 'app/outputs/user_catalog.json'))['items']
        assert len(rows) == 34158
        images = {PREFIX + 'app/outputs/' + row['files']['image']: row['image_sha256'] for row in rows}
        assert len(images) == 34158
        for index, (name, expected) in enumerate(images.items(), 1):
            assert hashlib.sha256(new.read(name)).hexdigest() == expected, name
            if index % 10000 == 0:
                print('Verified image hashes:', index, flush=True)
    sums = output / SUM_STAGED
    checksum = digest(target)
    sums.write_text(checksum + '  ' + NAME + '\n', encoding='ascii')
    result = {'source_sha256': BASE_SHA, 'sha256': checksum, 'size': target.stat().st_size, 'entries': len(b), 'unchanged_compressed_entries': unchanged, 'images_verified': len(images), 'changed_files': list(replacements), 'content_sha256': {name: hashlib.sha256(content).hexdigest() for name, content in replacements.items()}}
    (output / 'verification.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    return target, sums, result


def gh(*args):
    result = subprocess.run(['gh', *args], check=True, capture_output=True)
    return json.loads(result.stdout) if result.stdout.strip() else None


def api(path, body=None, output=None):
    command = ['api', 'repos/' + REPO + '/' + path]
    if body is not None:
        request = output / 'api-request.json'; request.write_text(json.dumps(body, ensure_ascii=False), encoding='utf-8')
        command += ['--method', 'PATCH', '--input', str(request)]
    return gh(*command)


def publish(output, target, sums, result):
    release = api('releases/' + str(RELEASE_ID))
    assert release['tag_name'] == 'v0.1.2' and not release['draft'] and not release.get('immutable')
    existing = {item['name']: item for item in release['assets']}
    assert existing[NAME]['id'] == BASE_ID and existing[NAME]['digest'] == 'sha256:' + BASE_SHA
    assert existing['SHA256SUMS.txt']['id'] == SUM_ID and existing['SHA256SUMS.txt']['digest'] == 'sha256:' + SUM_SHA
    assert not set(existing).intersection({STAGED_NAME, SUM_STAGED, OLD_NAME, SUM_OLD})
    subprocess.run(['gh', 'release', 'upload', 'v0.1.2', str(target), str(sums), '--repo', REPO], check=True)
    staged = {item['name']: item for item in api('releases/' + str(RELEASE_ID))['assets']}
    new = staged[STAGED_NAME]; new_sum = staged[SUM_STAGED]
    assert new['digest'] == 'sha256:' + result['sha256'] and new['size'] == result['size']
    assert new_sum['digest'] == 'sha256:' + digest(sums)
    # Only after both uploads are verified, preserve and rename the old pair.
    try:
        api('releases/assets/' + str(BASE_ID), {'name': OLD_NAME}, output)
        api('releases/assets/' + str(SUM_ID), {'name': SUM_OLD}, output)
        api('releases/assets/' + str(new['id']), {'name': NAME}, output)
        api('releases/assets/' + str(new_sum['id']), {'name': 'SHA256SUMS.txt'}, output)
    except Exception:
        # Restore the canonical old pair if promotion is only partly complete.
        current = {item['id']: item for item in api('releases/' + str(RELEASE_ID))['assets']}
        for item, temp_name in [(new, STAGED_NAME), (new_sum, SUM_STAGED)]:
            if current[item['id']]['name'] in {NAME, 'SHA256SUMS.txt'}:
                api('releases/assets/' + str(item['id']), {'name': temp_name}, output)
        api('releases/assets/' + str(BASE_ID), {'name': NAME}, output)
        api('releases/assets/' + str(SUM_ID), {'name': 'SHA256SUMS.txt'}, output)
        raise
    url = 'https://github.com/' + REPO + '/releases/download/v0.1.2/'
    body = f'**[全件版ZIPをダウンロード / Download the complete ZIP]({url}{NAME})** — {result["size"]:,} bytes\n\n'
    body += f'[SHA256SUMS.txt]({url}SHA256SUMS.txt) · [日本語README](https://github.com/{REPO}/blob/main/README.ja.md) · [English README](https://github.com/{REPO}/blob/main/README.md)\n\n'
    body += '**2026-10-25 — Eight style categories / スタイル8カテゴリ:** Issue #2 implemented with thanks to Brie-Wensleydale. All 221 styles have one category; select multiple categories and combine with search. Names support English/Japanese and selections survive reload. 全221件を重複なく分類。画像・プロンプト・生成設定・判定データは変更していません。\n\n'
    notes = (ROOT / 'docs/releases/v0.1.2.md').read_text(encoding='utf-8')
    notes = notes.replace('](../updates/', '](https://github.com/' + REPO + '/blob/main/docs/updates/')
    body += notes
    body += f'\n\n## Current archive verification / 現行ZIPの検証\n\n7-Zip updated only nine UI/documentation files. All {result["entries"]:,} entries passed the archive test; {result["unchanged_compressed_entries"]:,} other compressed payloads are unchanged and all 34,158 image SHA-256 values match. The previous ZIP/checksum are retained as `{OLD_NAME}` / `{SUM_OLD}`; earlier `before-title-link` and `before-ui-state-fixes` assets are also retained.\n\n```text\n{result["sha256"]}  {NAME}\n```\n'
    api('releases/' + str(RELEASE_ID), {'body': body}, output)
    final = api('releases/' + str(RELEASE_ID)); assets = {item['name']: item for item in final['assets']}
    assert assets[NAME]['id'] == new['id'] and assets[NAME]['digest'] == 'sha256:' + result['sha256']
    assert assets['SHA256SUMS.txt']['id'] == new_sum['id']
    for name, old in existing.items():
        preserved = OLD_NAME if name == NAME else SUM_OLD if name == 'SHA256SUMS.txt' else name
        assert assets[preserved]['id'] == old['id'] and assets[preserved]['digest'] == old['digest']
    result['assets'] = {name: {key: item[key] for key in ['id', 'digest', 'size']} for name, item in assets.items()}
    (output / 'publication.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base', type=Path); parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--sevenzip', default='7z'); parser.add_argument('--publish', action='store_true')
    args = parser.parse_args(); output = args.output.resolve(); output.mkdir(parents=True, exist_ok=True)
    if args.publish:
        assert os.environ.get('GITHUB_ACTIONS') == 'true' and os.environ.get('GITHUB_REPOSITORY') == REPO and os.environ.get('GITHUB_REF') == 'refs/heads/main'
        base = output / 'published-before-style-categories.zip'
        with base.open('xb') as stream:
            subprocess.run(['gh', 'api', 'repos/' + REPO + '/releases/assets/' + str(BASE_ID), '-H', 'Accept: application/octet-stream'], stdout=stream, check=True, timeout=900)
    else:
        if args.base is None:
            parser.error('--base is required for a local build')
        base = args.base.resolve()
    target, sums, result = build(base, output, args.sevenzip)
    if args.publish:
        publish(output, target, sums, result)
    else:
        print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
