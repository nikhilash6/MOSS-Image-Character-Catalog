[English](README.md)

# MOSS-Image キャラクター＆スタイルカタログ

**公開準備中（2026年10月22日更新）。以下はローカルで生成・検証した配布予定内容です。このGitHubリポジトリではREADME等の文書を公開しており、アプリ本体・画像ZIP・サンプルJSONのダウンロード公開はまだ行っていません。**

**v0.1.0／キャラクター33,937枚・スタイル221枚を収録したローカルカタログです。** 生成済み画像とプロンプト・workflowを閲覧できます。モデル本体は同梱していません。 初期言語は英語です。画面で日本語へ切り替えられます。Krea2の画像・合否判定・個人設定は引き継いでいません。


## 収録内容と容量

**Anima向けのキャラクタータグ一覧を元に、追加候補と画風をMOSS-Imageで生成した画像・プロンプトのローカルカタログです。AnimaDexのアーティスト一覧ではありません。**

| 内容 | 枚数 |
|---|---:|
| キャラクター | **33,937** |
| スタイル・画風 | **221** |
| **合計** | **34,158** |
| 展開後のファイル合計 | **約2.75 GB／2.56 GiB** |
| ZIP標準圧縮（DEFLATE 6）の容量目安 | **約2.05 GB／1.91 GiB**（ZIPは保存せず圧縮量を計測） |

キャラクターは、元CSVからの生成33,690枚に、追加候補80枚＋Krea2で確認した未収録候補160枚＋私服版2枚＋比較試作5枚を加えた33,937枚です。元CSVは36,492行で、ユーザー指定上限2,761件と未生成キャンセル41件を除いています。衣装・形態違い、比較試作もそれぞれ1枚として数え、異なるキャラクター数を表す数字ではありません。プラスアルファはキャラクター247枚とスタイル221枚です。容量はモデル・参照DB・個人設定を含まない配布構成の目安で、圧縮ソフトや設定によって変わります。

**品質・キャラクター同一性・画風再現の合格／不合格による選別は行っていません。** 名前やプロンプトと一致しない画像、画風が十分に出ていない画像も含みます。配布時に品質判定による除外はせず、登録済み画像を収録します。利用者が自分で確認し、必要に応じて非表示・再表示や比較判定を行うための資料です。個人の非表示状態・判定結果は配布ZIPに含めません。

## キャラクター画像の生成条件（初期設定・2026年10月18日）

**今回の画像は、初期公開のMOSS-Image-SFTに、生成時間短縮用の8-step LoRAを適用した結果です。** MOSS-Image-Baseではありません。また、元のフル精度重みではなく、INT8 ConvRot版のモデル・テキストエンコーダーを使用しています。大量生成の時間短縮を目的とした設定であり、未変更のBaseモデルの評価や最高画質の比較試験ではありません。

以下は **2026年10月18日** に、実際の生成画像に保存されたワークフローと使用中のAPIワークフローを照合した設定です。Base／SFTの初回公開は、[公式リポジトリ](https://github.com/OpenMOSS/MOSS-Image#news)で2026年10月16日と案内されています。

| 項目 | 実際の設定 |
|---|---|
| 使用モデル | 初期公開の **MOSS-Image-SFT** |
| 拡散モデルファイル | `MOSS-Image/moss_image_sft_int8_convrot.safetensors` |
| モデル読込 | `UNETLoader`、`weight_dtype=default` |
| テキストエンコーダー | `qwen3.5_9b_int8_convrot.safetensors` |
| エンコーダー読込 | `CLIPLoader`、type=`moss_image`、device=`default` |
| VAE | `flux2-vae.safetensors` |
| 高速化LoRA | [lodestones/MOSS-Image-SFT-8-steps-dmd](https://huggingface.co/lodestones/MOSS-Image-SFT-8-steps-dmd) の `moss_image/lora_latest.safetensors` |
| LoRA読込／モデル強度 | `LoraLoaderModelOnly`／**1.0** |
| サンプラー／スケジューラー | **`er_sde`／`simple`** |
| ステップ／CFG／denoise | **8／1.0／1.0** |
| シード | **8961184**、固定 |
| 解像度／バッチサイズ | **896 × 1184／1**（`EmptyFlux2LatentImage`） |
| ネガティブプロンプト | 空欄 |
| 追加ガイダンス | `SkipLayerGuidanceDiTSimple`および明示的なshift変更ノードは使用していません |
| カタログ保存画像 | WebP、品質 **70**、`lossless=False`、method **0**。プロンプト・ワークフローメタデータと別途JSONを保存 |

LoRAは大量の候補を現実的な時間で確認するために使いました。キャラクターの連続生成とサンプルのモデル強度は **1.0** です。LoRAなしのSFTやBF16版の結果を示すものではありません。

入力元は、Krea2版でも使用した、ユーザー提供の **Anima向けキャラクタータグ一覧（`anima_characters.csv`）** です。そのタグ一覧を用いて、MOSS-Imageでキャラクターの再現を試みています。「Anima向け」は入力リストの用途を指し、画像をAnimaモデルで生成したという意味ではありません。MOSS-Imageの公式対応キャラクター一覧や学習済み一覧ではなく、タグの互換性・正しい再現を保証するものでもありません。

生成プロンプトは、元CSVのキャラクター名・作品名・外見タグに、全身・1体・中央・画面の約65%・十分な余白・薄いグレーの背景・柔らかい照明という共通指定を加えています。人物には着衣・立ち姿の指定も加えています。元タグ、コピー用プロンプト、実際の生成プロンプトは別々に保持します。MOSSプロンプト拡張スキルは、**ここで説明するキャラクターの一括生成には使用していません**。

**キャラクター用サンプル：`MOSS_Image_Character_Sample.json`**。ComfyUIへドラッグ＆ドロップし、導入したモデル名を選び直して実行します。SFT INT8 ConvRot＋8-step LoRA強度1.0、8steps、CFG1.0、er_sde/simple、seed8961184、896×1184、Small Decoderの構成です。キャラクター・外見の英文を変えて試せます。初期の11,694枚は標準のFlux2 VAE、その後の22,243枚はSmall Decoderで、画像ごとの実設定は詳細画面の「保存JSONを開く」で確認できます。

サンプルは通常のSave ImageでPNG保存します。収録画像は中間PNGからWebP品質70へ変換して登録したものです。サンプルにWebP変換・カタログ自動登録は含みません。画像を生成した後、Add Image／画像を追加で登録できます。

**結果の読み方：** SFTによる追加学習、量子化、高速化LoRA、少ステップ生成、プロンプト、シードはいずれも絵柄やキャラクター再現に影響し得ます。Baseモデル、フル精度版、LoRAなしのSFT、別の生成条件と同じ結果になるとは限りません。再現が弱い画像があっても、そのキャラクターを生成できないと断定する資料ではありません。外見の類似だけで正しいキャラクターや学習済みと断定するものでもありません。自動生成した画像は人間による確認待ちです。

**今後のアニメ版について：** [開発者AMA](https://www.reddit.com/r/StableDiffusion/comments/1x7zf1r/hey_guys_im_one_of_the_core_developers_of/)では、OpenMOSSのコア開発者がアニメ版の公開を優先する方針を述べています。今回のカタログは上記の**初期公開の汎用SFTモデル＋高速化LoRA**による記録であり、その将来のアニメ特化版の評価ではありません。ここでは公開日や性能を確約せず、将来のモデルには別途検証が必要です。

## スタイル画像の生成条件（2026年10月21日）

収録したスタイル221枚（先行40枚＋追加181枚）の保存workflowを全件照合し、以下の設定が共通であることを確認しました。**2026年10月21日**に、保存済みレンブラント試作のワークフローとバッチ実行処理を照合しました。上記のキャラクター画像とは生成条件が異なります。

| 項目 | スタイル画像の設定 |
|---|---|
| 拡散モデル | **MOSS-Image-SFT**、`MOSS-Image/moss_image_sft_bf16.safetensors` |
| モデル読込 | `UNETLoader`、`weight_dtype=default` |
| テキストエンコーダー | `qwen3.5_9b_int8_convrot.safetensors`。`CLIPLoader`、type=`moss_image`、device=`default` |
| VAE | `full_encoder_small_decoder.safetensors` |
| LoRA | **使用していません**。このワークフローにLoRA読込ノードはありません |
| ステップ／CFG／denoise | **25／2.5／1.0** |
| サンプラー／スケジューラー | **`er_sde`／`simple`** |
| シード | **8961184**、固定 |
| 解像度／バッチサイズ | **896 × 1184／1** |
| ネガティブプロンプト | 空欄 |
| 最終画像 | **WebP、品質70**、`lossless=False`、method **0** |
| 保存処理 | `SaveImageKJ`で中間PNGを保存後、ローカルの登録処理でWebPに変換。埋込メタデータと別途ワークフローJSONを保持 |

拡散モデルはBF16版ですが、テキストエンコーダーはINT8 ConvRot版です。全体をBF16で処理する構成ではありません。これは今回のスタイル画像の実使用条件であり、モデル全般への推奨設定を示すものではありません。**スタイル用サンプル：`MOSS_Image_Style_Sample.json`**。ComfyUIへドラッグ＆ドロップして読み込みます。英文の画風説明と共通場面を変えて使えます。通常のSave ImageでPNG保存し、WebP変換・自動登録は含みません。キャラクター用とは設定が異なります。

プロンプトは、描画の特徴・素材・輪郭・造形・塗りを英文で指定します。画家指定では名前も英文中に含め、`@`やアーティストタグの2回反復は使いません。準備にはローカルの **moss-image-prompt-enhancer** のCaptionコンパイラーを使用しています。この処理自体は画像生成や外部サービスへの問い合わせを行いません。コピー用プロンプトは画風の段落だけを保持し、実際の生成時には次の共通場面を加えます。

```text
A single adult woman with short dark brown hair, wearing a cream shirt and a navy apron, carefully arranging a small bouquet of yellow and white flowers on a wooden worktable in a bright flower workshop. Three-quarter view from waist up, natural hand gesture, soft window light, simple uncluttered background. One person.
```

人物・服装・花・作業内容を共通にし、人形や彫刻ではその媒体の造形へ置き換えます。NovelAI風・Animagine風・niji風も、**MOSS-Imageで英文の特徴を指定する実験**です。各サービスや別のモデルで生成した画像ではなく、名称だけでそのモデルの画風が再現できると保証するものでもありません。異なる画風が似た結果になる可能性もあるため、実画像の目視確認が必要です。

各画像の実際の生成構成は、保存済みワークフローで確認できます。生成時間はプロンプト・モデル読込・PCの負荷などで変わるため、ComfyUI内の実行時間と、変換・保存・登録を含む時間を分けて記録しています。

## 生成に使用したPC・ソフトウェア環境

**2026年10月18日** に、PCのハードウェア情報と稼働中ComfyUIのAPIから確認しました。

| 項目 | 使用環境 |
|---|---|
| OS | Windows 11 Pro、ビルド **26200** |
| CPU | AMD Ryzen 9 **3900X**、12コア／24スレッド |
| メインメモリ | **64 GB**搭載、OS報告の使用可能容量は約63.93 GiB |
| GPU／VRAM | NVIDIA GeForce **RTX 5060 Ti／16 GB** |
| NVIDIAドライバー | **616.92** |
| ComfyUI | **0.41.0**、ローカルのコミット `5cc4b870094c89090db54bd8d12649dcaf89f2ba` |
| ComfyUIのPython | **3.12.14**、64-bit |
| PyTorch | **2.14.1+cu130**（CUDA 13.0ビルド） |

これは**このカタログ画像を生成したPCの記録**であり、最低動作要件ではありません。CUDA 13.0はPyTorchのビルド情報で、別途CUDA Toolkitを導入しているという意味ではありません。生成速度は設定・プロンプト・モデルの常駐状態・他の処理によって変動します。保存済み画像をカタログで閲覧するだけなら、このGPUは必要ありません。macOS／Linux用の起動ファイルの同梱は、そのOSで画像生成を検証したという意味ではありません。

## 起動

Windowsは **START_HERE - Windows.cmd** をダブルクリックしてください。フォルダ全体を一緒に保管します。Python 3.10以上とブラウザーが必要です。通常のURLは **http://127.0.0.1:8797/** です。空いていない場合は別のポートを案内します。

既存の互換Pythonを利用し、不足時は専用環境を作成するランチャーを流用しています。既存Pythonへ勝手に依存を追加しません。初回の依存導入には通信が必要な場合があります。

macOS：`sh './START_HERE - macOS.command'`、Linux：`sh './START_HERE - Linux.sh'`。このMOSS版での3OS CIはまだ行っていません。

## 画像追加・編集

1. 「画像を追加」を押し、WebP・PNG・JPEGを選びます。
2. 「キャラクター」か「スタイル」を選びます。
3. 名前・作品／分類・プロンプト・元タグ・ワークフローJSONは必要な分だけ入力します。未入力でも登録できます。
4. 登録後は画像を開き、「編集」から修正できます。

「閉じる」は入力の下書きを保持し、「キャンセル」は未保存入力を破棄します。「登録／変更を保存」で確定します。「サーバー停止」はバックグラウンド処理を終了する別の操作です。

登録画像は **app/outputs/user_items/**、情報は **app/outputs/user_catalog.json** と **app/outputs/user_catalog_edits.json** に保存されます。移動や整理の前にはapp/outputsをバックアップしてください。画像を任意フォルダに置くだけでは登録されません。

## ワークフローと任意の比較

この配布物は保存済み画像を閲覧するためのカタログです。生成用バッチ・中間PNG・進捗ログ・モデル重みは同梱していません。サンプルは **`MOSS_Image_Character_Sample.json`** と **`MOSS_Image_Style_Sample.json`** の2件です。カタログを開くだけでは生成を開始しません。任意のAnimaDex比較は独立した機能です。配布物に含める比較の設定手順を参照してください。モデル本体は別途導入が必要です。

公式配布：[Comfy-Org/MOSS-Image](https://huggingface.co/Comfy-Org/MOSS-Image)。画面と画像登録機能はKrea2カタログv0.9.6から流用しています。

## 配布版のスタイル閲覧

「スタイル」タブで221枚を表示できます。「生成順（新しい順）／生成順（古い順）」はMOSS画像の保存日時で並びます。コピーするのは画風の英文部分で、見本の女性・花の共通場面は含みません。UIはAnimaDexに近い操作性を目指し、Krea2カタログと共通する操作を使用していますが、同一のアプリではありません。

比較は任意で、利用者自身のAnimaDexデータを別途設定します。スタイルは参照画像がなくてもMOSS画像を単独表示します。参照が一意に対応する場合は左右に並べ、参照なしの項目には「参照画像なし」と明示します。参照なしのスタイルも「合格・不合格・保留」で目視判定できます。選択した合格・不合格だけを確定JSONへ出力し、カタログ上部の「判定JSONを読み込む」で内容を確認して反映します（合格は表示、不合格は非表示、画像は削除しません）。保留・未選択は反映しません。参照なしの判定はMOSS単独判定として記録し、反映前に実画像のSHA256を照合します。元画像・個人の参照DB・比較判定は同梱していません。221枚すべての画風再現を合格と判定したという意味ではありません。

## モデルの入手先とサンプルの使い方


| ファイル名 | 入手先 |
|---|---|
| `moss_image_sft_int8_convrot.safetensors` | [Comfy-Org / MOSS-Image INT8 ConvRot](https://huggingface.co/Comfy-Org/MOSS-Image/blob/main/diffusion_models/moss_image_sft_int8_convrot.safetensors) |
| `moss_image_sft_bf16.safetensors` | [Comfy-Org / MOSS-Image SFT BF16](https://huggingface.co/Comfy-Org/MOSS-Image/blob/main/diffusion_models/moss_image_sft_bf16.safetensors) |
| `qwen3.5_9b_int8_convrot.safetensors` | [Comfy-Org / text encoder](https://huggingface.co/Comfy-Org/MOSS-Image/blob/main/text_encoders/qwen3.5_9b_int8_convrot.safetensors) |
| `flux2-vae.safetensors` | [Comfy-Org / original VAE](https://huggingface.co/Comfy-Org/MOSS-Image/blob/main/vae/flux2-vae.safetensors) |
| `full_encoder_small_decoder.safetensors` | [Black Forest Labs / FLUX.2 Small Decoder](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder/blob/main/full_encoder_small_decoder.safetensors) |
| `lora_latest.safetensors` | [lodestones / 8-step acceleration LoRA](https://huggingface.co/lodestones/MOSS-Image-SFT-8-steps-dmd/blob/main/lora_latest.safetensors) |

拡散モデルはComfyUIのmodels/diffusion_models、エンコーダーはmodels/text_encoders、VAEはmodels/vae、LoRAはmodels/lorasへ配置します。JSON中のサブフォルダーや名前が手元と違う場合は、各Loaderで導入したファイルを選び直してください。MOSS-Image対応版のComfyUIが必要です。モデルは同梱していません。上記リンクの重みが将来更新される場合があるため、同じファイル名だけで完全一致は保証できません。

## 自分の画像登録と判定の共有

「Add Image／画像を追加」でキャラクターとスタイルの両方を登録できます。名前・作品／分類・再利用プロンプト・元タグ・保存workflowを必要に応じて入力し、Register／登録で保存します。「Webで画像を検索」は入力した名前・作品を新しいタブで検索する補助です。検索結果を自動で登録・転載する機能ではありません。

比較画面で合格・不合格・保留を人が選び、反映対象をチェックして「選択した判定を確定してJSON出力」で保存します。カタログ上部の **「判定JSONを読み込む」** からそのJSONを選ぶと、合格・不合格の件数、表示に戻す／非表示にする件数を確認できます。**「確認した判定を反映」** を押すまで変更しません。保留・未選択・未確定は除外し、別の画像に入れ替わっている場合は反映を拒否します。画像やお気に入りは削除しません。

このJSONを同じ画像入りのカタログを使う人と共有できます。CSVの一覧保存とは別の形式です。参照画像のないスタイルもMOSS画像だけで判定でき、単独判定と参照比較を区別して記録します。読み込み時はMOSS画像の一致を検証し、共有者の目視判定を取り込むもので、利用者のPCで参照画像との比較をやり直したり自動判定したりはしません。

キャラクターの初期並びはCopyright (most first)／作品件数順です。同一シリーズをまとめて多い順に並べ、Originalと少数作品は「その他の作品・オリジナル」にまとめて末尾へ送ります。生成順の古い順・新しい順も選べます。

## 公開範囲とライセンス

現在公開している文書は [MIT License](LICENSE) です。[NOTICE.md](NOTICE.md) の範囲を参照してください。まだ公開していないアプリ・画像・モデル・第三者素材への許諾を意味しません。本プロジェクトはOpenMOSSまたはAnimaDexの公式製品ではありません。作品名・キャラクター名は対象の識別用です。
