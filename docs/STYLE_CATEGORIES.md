# Eight style categories — Issue #2

Thanks to Brie-Wensleydale for the [category proposal](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/issues/2).

All **221 styles** have exactly one category, with no omissions or duplicates. The proposal was adapted to the actual entries; these are browsing groups, not claims about MOSS training data or proof of accurate style reproduction.

| Category | Styles |
|---|---:|
| Anime & Manga / アニメ・マンガ | 15 |
| Western Animation & Comics / 海外アニメ・コミック | 30 |
| Drawing & Print Media / 描画・版画・画材 | 9 |
| 3D / Digital / Photography / 3D・デジタル・写真 | 8 |
| Craft / Sculpture / Folk / 工芸・彫刻・民芸 | 19 |
| World Traditional Art / 世界の伝統美術 | 31 |
| Contemporary / Pop / Street / Surreal / 現代・ポップ・ストリート・幻想美術 | 50 |
| Classical & Modern Painting / 古典・近代絵画 | 59 |
| **Total** | **221** |

Select **Styles**, then use **Category** at the top of the left filter panel. Multiple categories are combined (OR), and the name/prompt search can narrow those results. **Clear filters** restores all styles. Category names follow English/Japanese language selection; filters survive reload. The sample demo uses the same classification, but its counts cover only its 24 style samples.

The [CSV assignment list](style-categories.csv) contains every catalog key and name. The [JSON mapping](style-categories.json) is the source used by the [patch tool](../tools/style_category_patch.py). Existing saved records, images, prompts, workflows, ratings and visibility are not rewritten. New images without an assignment retain their existing category.

Adjustments: World Traditional Art includes traditions beyond East Asia; Fortnite and Resident Evil are digital/3D, Claymation is craft, Herge and Moebius are Western comics, Mr. is contemporary, and Classical & Modern Painting also includes Japanese modern oil painting. Overlapping traditions still receive one browsing category each.

Verified locally in the full catalog: all eight category counts and displayed labels, multiple selection, search combinations, reload persistence, English/Japanese switching, newest/oldest ordering, character-tab preservation, and image loading. Existing hidden/rating data and the original generation project were preserved. This was not a new generation or full visual-quality review.

The **v0.1.2 package refresh of 2026-10-25** includes this feature, updated bilingual READMEs and these lists. Use the current [Release ZIP](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/releases/download/v0.1.2/MOSS-Image-Character-Catalog-v0.1.2.zip) and its updated SHA256SUMS.txt. Images remain **33,937 characters + 221 styles = 34,158**. No model weights or reference library are added.
