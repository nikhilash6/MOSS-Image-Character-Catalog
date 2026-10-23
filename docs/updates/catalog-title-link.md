# Catalog title repository link / カタログタイトルのリンク

**v0.1.2 package refresh: 2026-10-24.**

The catalog heading opens the [GitHub repository](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog) in a new tab. English/Japanese localization, version display and appearance are preserved, with visible keyboard focus and hover. The online sample uses the same link.

カタログの太字タイトルからGitHubリポジトリを新しいタブで開けます。日英切替・バージョン表示・見た目を維持し、キーボードフォーカスとホバーを表示します。公開デモも同じリンクです。

## Download / ダウンロード

Use the [v0.1.2 Release ZIP](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/releases/download/v0.1.2/MOSS-Image-Character-Catalog-v0.1.2.zip) and updated [SHA256SUMS.txt](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/releases/download/v0.1.2/SHA256SUMS.txt). The filename and application version remain v0.1.2; the refreshed archive has a different checksum. The exact size and hash are on the Release page. Files labelled `before-title-link` retain the earlier package and checksum for reference.

ファイル名とアプリのバージョンはv0.1.2を維持していますが、修正版ZIPのチェックサムは変わります。正確な容量とSHA256はReleaseページをご覧ください。`before-title-link` 付きファイルは更新前のZIP・チェックサムです。

## Contents and verification / 内容と検証

- UI changes are limited to `app/review/index.html` and `app/review/review.css`; both READMEs and these update notes are included.
- All 33,937 character images and 221 styles (34,158 total), prompts, workflows, settings and uncurated status are preserved.
- The package is updated using 7-Zip CLI. Publication requires the archive test and every image SHA256 check to pass.
- Link attributes, localized inner title and the served local HTML were checked. Browser-click verification was unavailable; no new full-browser or generation test is claimed.
- The original generation project is unchanged.

画面の変更はタイトルリンクのHTML/CSSのみです。日英READMEと更新説明も同梱し、画像・プロンプト・ワークフロー・生成設定・未選別の状態を維持しています。7-Zipで更新し、ZIP全体の検査と全画像のSHA256照合に合格したものを公開します。ブラウザーの実クリック確認は未実施です。オリジナルの生成用プロジェクトは変更していません。

[Source patch](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/blob/main/patches/catalog-title-repository-link.patch) · [Packaging and validation script](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/blob/main/tools/refresh_v012_title_link.py)
