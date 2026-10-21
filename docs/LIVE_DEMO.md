# Live demo / ライブデモ

**[Open / 開く](https://ukr8b3g-cmyk.github.io/MOSS-Image-Character-Catalog/)**

The site contains **96 character images and 24 styles (120 samples, about
8.36 MB)**. It uses the distribution copy's static frontend, following the
Krea2 catalog's demo approach. Search, filters, sorting, image enlargement,
prompt/tag copying, language and theme switching work without Python or a GPU.

キャラクター96枚・スタイル24枚の抜粋です。全件版の34,158枚とは区別してください。
作品別の件数や「20枚以下」の集約は、このデモにあるサンプル数で計算します。
ポケモン32枚、Fate24枚、Arknights24枚、原神8枚、東方4枚、Original4枚と、
媒体・画家・アニメなどを含むスタイル24枚を収録しています。

Character selection uses the first distinct names in saved order for those
works, plus four named Original examples; styles span different visual media.
This is an interface sample, **not an accuracy-approved selection or a
statistically representative benchmark**. No pass/fail judgments are supplied.

## What stays local / ローカル版だけの機能

Add Image, editing, favorites, ratings, Hide/Undo, CSV export, comparison
judgments, confirmed-review JSON import and saved workflow downloads belong
to the local application. They are hidden in the demo. There is no Python
backend or write/delete API on this site. Browser preferences affect only
the current browser, not the published catalog.

画像追加・編集・比較判定・判定JSONの反映はローカル版の機能です。
デモは閲覧・検索・コピー用で、全機能を試せる画面ではありません。
全件版のアプリ本体・画像一式・比較判定ツール・サンプルワークフローJSONは、[v0.1.0のRelease ZIP](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/releases/download/v0.1.0/MOSS-Image-Character-Catalog-v0.1.0.zip)で配布しています。

## Public data boundary / 公開範囲

Only the files under `demo/` are deployed to Pages. Public JSON uses an
explicit field allowlist. No API token, operation ID, local image path,
generation log, private review state or reference library is included.
EXIF/XMP chunks were removed from the copied WebP containers without
re-encoding their image data; decoded pixels were compared with the source.
The original catalog and distribution images were not changed.

GitHub Pages permits a published site of up to **1 GB**. The full prepared
catalog is about 2.75 GB, so this initial demo uses a small subset.
[GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits).

## Validate and preview / ローカル確認

From this repository's root:

```sh
python tools/validate_demo.py
node --check demo/review.js
python -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/demo/`; use HTTP rather than `file://`.
Stop this test server with Ctrl+C. Relative image/data links also work under
the GitHub project subdirectory.

## Deployment / GitHub Pages

In repository **Settings → Pages → Build and deployment → Source**, select
**GitHub Actions**. `.github/workflows/pages.yml` validates the sample site,
uploads **only `demo/`**, and deploys it on changes to `main` or a manual run.
It never downloads or publishes the full collection, release archives,
model weights or the local application.

The workflow uses `contents: read` for checkout and grants `pages: write`
and `id-token: write` only to the deployment job. The `github-pages`
deployment job runs only on `main`. See GitHub's
[publishing-source documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
