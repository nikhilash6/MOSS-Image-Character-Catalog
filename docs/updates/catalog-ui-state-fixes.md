# Catalog navigation and filter scroll fixes / 検索とフィルター位置の修正

Date: 2026-10-24. The filename/version remains **v0.1.2**; use the current Release
checksum to distinguish this refresh from earlier v0.1.2 ZIPs.

## 日本語

- キャラクター検索後に「スタイルを見る」や別ビューのURLを開くと、検索語が残って結果が0件になる問題を修正しました。明示的なビュー移動では検索・ページをリセットし、同じスタイルURLの再読込ではその検索を保持します。通常のタブ操作ではタブごとの検索を保持します。
- フィルターを再読込・再展開すると、保存したスクロール位置が先頭へ戻る問題を修正しました。項目／仮想スペーサーを配置してから位置を復元し、古い過大な保存値は実際の範囲へ丸めます。
- 画像34,158枚、プロンプト、カタログ、個人の編集・判定データは変更していません。ZIP更新は7-ZipでUIのJavaScriptと関連する説明の計5ファイルだけを更新・追加します。
- 更新前のZIP／チェックサムはReleaseに `before-ui-state-fixes` 名で残します。さらに前の `before-title-link` ファイルも保持します。個人データを含む既存フォルダーへ配布ZIPを無条件に上書きせず、新しいフォルダーへ展開してください。

## English

- Explicit navigation to styles, creatures, categories or a generation run resets
  the previous view's search and page. Reloading the same style URL retains its
  search; ordinary tab switching retains each tab's own query.
- Filter scroll positions are restored after rows/virtual spacers exist. Closed
  filters retain their position, and obsolete oversized offsets are clamped to
  the browser's actual range.
- Images, prompts, catalog data and personal edits/judgments are unchanged. The
  selective 7-Zip update changes/adds only five UI/documentation files. Previous
  ZIP/checksum assets are retained with `before-ui-state-fixes`; the older
  `before-title-link` pair is also retained. Extract into a new directory rather
  than overwrite a folder containing personal data.

## Verification and limits / 検証と範囲

- The public demo and two local UI variants reproduced both issues before the
  fix. An isolated browser regression passed 87 checks for navigation, reload,
  per-tab search, page reset, ordinary/virtual/non-Trial filter lists,
  close/reopen, language/height changes and oversized-position clamping.
- Fixtures use separate storage, read-only HTTP responses and placeholder images.
  They do not edit the user's catalog or test full-collection performance/quality.
- JavaScript syntax, source-count ordering and 16 Windows launcher checks passed.
  An older local hierarchy test fails identically before/after this patch on an
  unrelated expectation; its classification functions and expected value remain.
- The archive gate tests all entries with 7-Zip, compares every unchanged
  compressed payload with the previous ZIP, and verifies all 34,158 catalog image
  SHA-256 values. Release metadata contains the current archive hash and size.
- No new runtime dependency is added. The Python backend, generation workflow,
  models, comparison decisions and launcher settings are unchanged.

Reproducible sources: [package patch](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/blob/main/tools/catalog_ui_state_patch.py),
[7-Zip refresh](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/blob/main/tools/refresh_v012_ui_state.py),
[state regression](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/blob/main/tools/check_ui_state.cjs), and
[optional browser regression](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/blob/main/tools/check_ui_state_browser.cjs).
