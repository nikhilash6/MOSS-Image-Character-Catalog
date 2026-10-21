## [▶ ライブデモを開く（サンプル120枚）](https://ukr8b3g-cmyk.github.io/MOSS-Image-Character-Catalog/)
<img width="1887" height="1013" alt="Clip_37" src="https://github.com/user-attachments/assets/19c619e5-21dd-464f-90a6-b3c24a22c8fc" />


### [↓ 全件版ZIPをダウンロード — v0.1.0](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/releases/download/v0.1.0/MOSS-Image-Character-Catalog-v0.1.0.zip)

**34,158枚・約2.05 GB／1.91 GiB** · [リリース情報](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/releases/tag/v0.1.0) · [SHA256チェックサム](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/releases/download/v0.1.0/SHA256SUMS.txt)

> [!NOTE]
> **ライブデモは、カタログ全体の一部だけを抜粋したプレビューです。**
>
> **デモ掲載：120枚**（キャラクター96枚＋スタイル24枚）。閲覧・検索・プロンプトコピーを試せます。
>
> **全件版：34,158枚**（キャラクター33,937枚＋スタイル221枚）。全件版のローカルアプリと画像一式は、上のZIPリンクからダウンロードできます。

[English](README.md)

# MOSS-Image キャラクター＆スタイルカタログ

**MOSS-Imageで生成した画像と、再利用できるプロンプトを探すカタログ**です。Anima向けキャラクター一覧を基に、追加キャラクターと画風のサンプルを収録しています。画像を確認し、使いたいプロンプトをコピーできます。Krea2カタログと操作を揃え、英語・日本語に対応しています。

| 全件版ダウンロード | 枚数・容量 |
|---|---:|
| キャラクター | **33,937枚** |
| スタイル | **221枚** |
| **合計** | **34,158枚** |
| 圧縮前のファイル合計 | **約2.75 GB／2.56 GiB** |
| 配布ZIP・DEFLATE 6 | **約2.05 GB／1.91 GiB** |
| オンラインデモ | **キャラクター96枚＋スタイル24枚**、約**8.36 MB** |

**公開状況（2026-10-22）：** **[v0.1.0・全件版ZIPをダウンロード](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/releases/download/v0.1.0/MOSS-Image-Character-Catalog-v0.1.0.zip)**できます。ローカルアプリ、**キャラクター33,937枚＋スタイル221枚**、比較判定ツール、サンプルワークフローJSON 2件を同梱しています。オンラインデモは抜粋120枚です。GitHubの **Code → Download ZIP** で取得できるのはデモと説明書のため、全件版にはReleaseのZIPを使ってください。モデルや参照画像ライブラリーは別途用意してください。

**画像の合格・不合格による選別はしていません。** キャラクターが違うもの、プロンプトと合わないもの、画風の効きが弱いものも含みます。収録や見た目の類似は、正確な再現や学習データへの収録を証明しません。デモの抜粋も「合格した画像の一覧」ではありません。

## まず試す

**[キャラクターを見る](https://ukr8b3g-cmyk.github.io/MOSS-Image-Character-Catalog/) · [スタイルを見る](https://ukr8b3g-cmyk.github.io/MOSS-Image-Character-Catalog/?tab=styles)**

デモにはPython・GPU・インストールは不要です。タブ切替、名前検索、作品・外見タグによる絞り込み、並べ替え、画像の拡大、プロンプト・元タグのコピーを試せます。テーマ・言語・表示設定はブラウザーに記憶されます。

| 機能 | オンラインデモ | ダウンロード版 |
|---|---|---|
| 検索・絞り込み・並べ替え・拡大・コピー | 抜粋120枚で利用可 | 全件で利用可 |
| Add Image、名前・プロンプト・タグ・ワークフローの編集 | — | 利用可 |
| お気に入り・評価・非表示・Undo | — | 利用可 |
| 比較判定・確定した判定JSONの読み込み | — | 利用可 |
| 画像ごとに保存したワークフローJSON | — | 利用可 |
| 画像生成 | なし | ComfyUIで別途実行 |

[Krea2](https://github.com/ukr8b3g-cmyk/Krea2-Character-Catalog)と同様に、静的データで表示する方式です。GitHub Pagesにはサンプルサイトだけを配置します。全件版はPagesのサイト上限1 GBを超えるため、そのまま掲載しません。[デモの範囲・公開方法](docs/LIVE_DEMO.md)。

## 収録内容と追加分

**Anima向けキャラクター一覧＋追加サンプル**を基にしたカタログで、AnimaDexのアーティスト一覧ではありません。元の `anima_characters.csv` は36,492行です。ユーザー指定の上限調整で未生成予定2,761件を除き、さらに未生成41件をキャンセルし、元一覧からの生成済みは**33,690枚**となりました。

| その元一覧の採用分に加えた内容 | 枚数 |
|---|---:|
| 追加キャラクター候補 | 80 |
| Krea2で確認済みだった未収録候補 | 160 |
| 私服差分の追加 | 2 |
| 比較テスト | 5 |
| **追加キャラクター小計** | **247** |
| 画風・画家・表現媒体などのスタイル | **221** |
| **追加分の合計** | **468** |

衣装・形態差分・テストも1枚として数えています。ユニークな人物数ではありません。Krea2の画像や判定結果は取り込んでいません。スタイル221枚は先行40枚と追加181枚で、英文で画風の特徴を指定しています。画家名・媒体・アニメ表現などを試した結果であり、再現精度の保証ではありません。

全件版ZIPは標準圧縮（DEFLATE 6）で**約2.05 GB／1.91 GiB**です。正確なバイト数とSHA256は[リリースページ](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/releases/tag/v0.1.0)に掲載します。モデル・個人設定・ログ・ロック・参照画像ライブラリーは含みません。デモ内の絞り込み件数は抜粋分の件数で、全件版の作品別枚数とは異なります。

## ダウンロードとローカル版の使い方

上のリンクからZIPをダウンロードして展開し、フォルダー全体を保持してください。Windowsでは `Get-FileHash .\MOSS-Image-Character-Catalog-v0.1.0.zip -Algorithm SHA256` の結果を `SHA256SUMS.txt` と照合できます。閲覧・登録に必要なのは**Python 3.10以上とWebブラウザー**です。GPUは別途画像生成する場合に使います。

| OS | 起動するファイル |
|---|---|
| Windows | `START_HERE - Windows.cmd` をダブルクリック |
| macOS | `START_HERE - macOS.command`、または `sh './START_HERE - macOS.command'` |
| Linux | `sh './START_HERE - Linux.sh'` |

基本アドレスは `http://127.0.0.1:8797/` です。使用中なら、ランチャーが開いた・表示した実際のアドレスを使ってください。**サーバー停止**はこのカタログのプロセスを終了します。タブを閉じる操作とは別です。対応Pythonを再利用するか専用環境を準備するため、初回の依存関係セットアップにはインターネット接続が必要な場合があります。

### 探す・コピーする・画像を追加する

1. **キャラクター／スタイル**を切り替えます。キャラクターの初期表示は **Copyright件数順**で、作品・シリーズ単位にまとまります。**その他の作品／オリジナル**は最後に配置し、登録済み20枚以下の作品もここへまとめます。
2. **生成順（新しい順）／生成順（古い順）**で、MOSS画像の保存時刻を基準に並べ替えられます。画像をクリックすると拡大します。**スタイルコピー**には画風の文章だけを含め、共通の見本シーンを除きます。
3. **画像を追加（Add Image）**でキャラクター／スタイルを選び、WebP・PNG・JPEGを指定します。名前・作品／分類・再利用プロンプト・元タグ・ワークフローJSONは任意です。登録するとローカルに保存され、空欄の名前にはファイル名を使います。
4. **Web画像検索**は入力した名前・作品を別タブで検索する補助機能です。検索画像を自動登録しません。保存済み画像の詳細にある**編集**から、後で内容を直せます。

### 比較判定と共有

比較画面は、人が判定するための別画面です。自動的に品質を判別するものではありません。参照比較には各自のAnimaDexを設定します。**MOSSのスタイル画像は、Krea2やAnimaDexの参照画像がなくても合否判定できます。** 参照なしを明示し、MOSS画像単独の判定として記録します。

1. 比較画面で**合格・不合格・保留**を選びます。
2. 共有したい判定を選択し、確定した**JSON**を書き出します。
3. カタログ上部の**判定JSONを読み込む（Import review JSON）**を開き、ファイルを選んでプレビューします。
4. **確認した判定を反映**を押します。合格は表示・再表示、不合格は非表示にします。**画像ファイルは削除しません。** 保留・未選択・未確定の行は変更しません。

取り込み時にMOSS実画像のSHA256を確認し、画像の変更・欠落があれば拒否します。同じ画像一式を持つ利用者同士でJSONを共有してください。CSV一覧出力は別機能で、確定判定の読み込み形式ではありません。個人の参照画像、お気に入り、非表示設定、判定結果は配布ZIPに含めていません。

## 生成設定とサンプルワークフロー

保存済みワークフローを基にした**このカタログで実際に使った設定**です。あらゆる条件への推奨値ではありません。キャラクターは大量生成を現実的な時間で進める設定、スタイルは高速化LoRAを使わないSFTの設定です。

| 設定 | キャラクター連続生成 | スタイル生成 |
|---|---|---|
| 拡散モデル | **MOSS-Image-SFT INT8 ConvRot** | **MOSS-Image-SFT BF16** |
| 拡散モデルのファイル | `moss_image_sft_int8_convrot.safetensors` | `moss_image_sft_bf16.safetensors` |
| テキストエンコーダー | `qwen3.5_9b_int8_convrot.safetensors` | 同じINT8 ConvRotエンコーダー |
| VAE | 当初Flux2 VAE、途中からSmall Decoder | Small Decoder |
| 高速化LoRA | `lora_latest.safetensors`、**強度1.0** | **なし** |
| Steps／CFG | **8／1.0** | **25／2.5** |
| Sampler／Scheduler | `er_sde`／`simple` | 同じ |
| Seed | **8961184**、固定 | 同じ |
| 解像度／バッチサイズ | **896 × 1184／1** | 同じ |
| Denoise／Negative prompt | **1.0／空欄** | 同じ |
| カタログの画像形式 | **WebP品質70**、非可逆、method 0 | 同じ |
| 汎用サンプルのファイル名 | **`MOSS_Image_Character_Sample.json`** | **`MOSS_Image_Style_Sample.json`** |

キャラクターは**BaseではなくSFT**を使っています。大量の候補を確認するため、8ステップ高速化LoRAを**1.0**で使用しました。LoRAなしのSFTやBF16の最高品質を評価したものではありません。最初の**11,694枚**は `flux2-vae.safetensors`、後半の**22,243枚**は `full_encoder_small_decoder.safetensors` です。画像ごとの保存ワークフローに実設定を残し、汎用キャラクターサンプルはSmall Decoderに揃えています。

キャラクタープロンプトは元一覧の名前・作品・外見タグを英文へ組み込み、単体・中央・全身・余白・薄いグレー背景・柔らかい照明を共通に指定しています。人物には服を着た立ち姿を指定しました。元タグ、再利用用コピー文、実際の生成プロンプトは別に保持します。このキャラクターバッチにMOSSプロンプトエンハンサースキルは使っていません。

スタイル**221枚すべて**の保存ワークフローを照合し、SFT BF16拡散モデル・INT8エンコーダー・Small Decoder・LoRAなし・25 steps・CFG 2.5を確認しています。画風の特徴を英文で指定し、次の共通シーンを加えました。

```text
A single adult woman with short dark brown hair, wearing a cream shirt and a navy apron, carefully arranging a small bouquet of yellow and white flowers on a wooden worktable in a bright flower workshop. Three-quarter view from waist up, natural hand gesture, soft window light, simple uncluttered background. One person.
```

NovelAI・Animagine・niji風の項目も、**MOSS-Imageで英文の特徴を指定した試作**です。そのサービスやモデルで生成した画像ではなく、名前どおりの再現を保証しません。モデル、量子化、LoRA、steps、CFG、文章、seedを変えると結果も変わります。今回うまく出なかったことだけで、その題材を生成できないとは判断できません。

**公開後のサンプルの使い方：** 対応するJSONをComfyUIへドラッグし、各Loaderで手元のモデルを選び直し、キャラクターまたは画風・場面の英文を変更して生成します。2件とも標準の **Save ImageでPNG保存**します。カタログのWebP品質70変換・登録は別処理で、サンプルから自動登録はしません。実際のスタイルバッチは `SaveImageKJ` で中間PNGを保存後、WebPへ変換し、埋め込みプロンプト／ワークフローと別ファイルのJSONを保持しました。

<details>
<summary>Loaderと再現条件の詳細</summary>

共通で `UNETLoader` の `weight_dtype=default`、`CLIPLoader` のtype `moss_image`・device `default`、`EmptyFlux2LatentImage`を使用します。キャラクターは `LoraLoaderModelOnly` を追加しています。明示的なshift調整ノードや `SkipLayerGuidanceDiTSimple` は使っていません。キャラクター設定は2026-10-18、スタイル設定は2026-10-21に照合しました。初期の汎用SFTは[公式リポジトリ](https://github.com/OpenMOSS/MOSS-Image#news)で2026-10-16に公開が告知されたモデルで、今後のアニメ専用モデルを評価した結果ではありません。

生成時間はプロンプト、保存・登録処理、モデル読み込み、システム負荷で変わります。ComfyUI内実行時間と保存・登録込み時間は別の指標です。同じファイル名でも、将来のモデル更新まで同じ重み・出力とは限りません。

</details>

### モデルのダウンロード

| ファイル | 配布元 | ComfyUIの配置先 |
|---|---|---|
| `moss_image_sft_int8_convrot.safetensors` | [Comfy-Org：SFT INT8 ConvRot](https://huggingface.co/Comfy-Org/MOSS-Image/blob/main/diffusion_models/moss_image_sft_int8_convrot.safetensors) | `models/diffusion_models` |
| `moss_image_sft_bf16.safetensors` | [Comfy-Org：SFT BF16](https://huggingface.co/Comfy-Org/MOSS-Image/blob/main/diffusion_models/moss_image_sft_bf16.safetensors) | `models/diffusion_models` |
| `qwen3.5_9b_int8_convrot.safetensors` | [Comfy-Org：エンコーダー](https://huggingface.co/Comfy-Org/MOSS-Image/blob/main/text_encoders/qwen3.5_9b_int8_convrot.safetensors) | `models/text_encoders` |
| `flux2-vae.safetensors` | [Comfy-Org：当初のVAE](https://huggingface.co/Comfy-Org/MOSS-Image/blob/main/vae/flux2-vae.safetensors) | `models/vae` |
| `full_encoder_small_decoder.safetensors` | [Black Forest Labs：Small Decoder](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder/blob/main/full_encoder_small_decoder.safetensors) | `models/vae` |
| `lora_latest.safetensors` | [lodestones：8ステップLoRA](https://huggingface.co/lodestones/MOSS-Image-SFT-8-steps-dmd/blob/main/lora_latest.safetensors) | `models/loras` |

MOSS-Image対応のComfyUIを使ってください。サンプルと配置先のサブフォルダーが違う場合は、各Loaderでインストール済みファイルを選択します。モデルと利用条件はそれぞれの配布元を確認してください。

### 生成に使ったPC

**RTX 5060 Ti（VRAM 16 GB）、Ryzen 9 3900X、メモリー64 GB、Windows 11 Pro**です。画像生成に使用した環境で、カタログ閲覧の最低要件ではありません。

<details>
<summary>記録したソフトウェア環境（2026-10-18）</summary>

| 項目 | 記録値 |
|---|---|
| OS | Windows 11 Pro、build 26200 |
| CPU | AMD Ryzen 9 3900X、12コア／24スレッド |
| メモリー | 64 GB搭載、利用可能約63.93 GiB |
| GPU／ドライバー | NVIDIA GeForce RTX 5060 Ti、16 GB／616.92 |
| ComfyUI | 0.41.0、commit `5cc4b870094c89090db54bd8d12649dcaf89f2ba` |
| Python／PyTorch | 3.12.14・64bit／2.14.1+cu130 |

初期に記録した環境であり、後続の全生成が同じバージョンだったという意味ではありません。CUDA 13.0はPyTorchのビルド表記です。別途CUDA Toolkitを導入したことを示すものではありません。macOS／Linux用ランチャーはKrea2版を引き継いでいますが、このMOSS配布物での新たな3 OS CIやmacOS／Linux実機デスクトップ検証は未実施です。

</details>

## プロジェクトとライセンス

UIは[Krea2 Character Catalog](https://github.com/ukr8b3g-cmyk/Krea2-Character-Catalog)を基に、AnimaDexに近い操作感を目指しています。OpenMOSS・Krea2・AnimaDexの公式製品ではありません。

管理者作成の説明書と公開デモのコードは[MIT License](LICENSE)の対象です。生成サンプル画像、第三者のキャラクター・モデル等の権利は[NOTICE.md](NOTICE.md)で区別しています。モデル本体、参照画像ライブラリー、認証情報、個人の判定状態は公開しません。誤りの報告には画像・スタイル名とカタログのバージョンを添えてください。
