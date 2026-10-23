# Catalog title repository link

The catalog heading now opens the GitHub repository in a new tab. The title retains its English/Japanese localization, version display and current appearance. Keyboard focus and hover are visible. The online sample uses the same link.

カタログの太字タイトルをクリックするとGitHubリポジトリが新しいタブで開きます。日英切替・バージョン表示・見た目を維持し、キーボードフォーカスとホバーを表示します。公開デモも同じリンクに揃えています。

## Local application patch

[Source patch](../../patches/catalog-title-repository-link.patch) changes only `app/review/index.html` and `app/review/review.css` in the v0.1.2 local app. It does not include images, metadata or the full application. The original generation project is unchanged.

The corrected ZIP is a separately named local build, **not a newly published Release**. The existing v0.1.2 Release and its checksum remain unchanged.

修正版ZIPは別名のローカルビルドです。新しいReleaseの公開や既存Releaseの差し替えは行っていません。

## Packaging verification

- Created with 7-Zip CLI by updating a copy of the original ZIP; only the two UI files changed.
- 7-Zip archive test passed for all 136,693 entries.
- All 34,158 image SHA256 values match the catalog.
- Confirmed the link attributes and localized inner title in the packaged HTML.
- Browser click validation was not completed because browser automation was unavailable.

Local build: `MOSS-Image-Character-Catalog-v0.1.2-title-link.zip`

Size: **2,054,768,134 bytes**.

```text
fbab28891a37ea70fcff6a49414fb32161d7dfc4cf51e65fcd6724bb202ba85d  MOSS-Image-Character-Catalog-v0.1.2-title-link.zip
```
