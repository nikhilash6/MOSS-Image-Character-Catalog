**[日本語READMEはこちら](README.ja.md)**

## [▶ Open the live demo — 120 sample images](https://ukr8b3g-cmyk.github.io/MOSS-Image-Character-Catalog/)
<img width="1887" height="1013" alt="Clip_37" src="https://github.com/user-attachments/assets/f37ba1b4-12d7-4915-a7fe-f6506990f50b" />


### [↓ Download the complete catalog ZIP — v0.1.0](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/releases/download/v0.1.0/MOSS-Image-Character-Catalog-v0.1.0.zip)

**34,158 images · about 2.05 GB / 1.91 GiB** · [Release notes](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/releases/tag/v0.1.0) · [SHA256 checksums](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/releases/download/v0.1.0/SHA256SUMS.txt)

> [!NOTE]
> **The live demo is a preview showing only a small part of the collection.**
>
> **Demo: 120 images** — 96 characters + 24 styles. Try browsing, searching and copying prompts.
>
> **Full collection: 34,158 images** — 33,937 characters + 221 styles. Download the complete local application and image collection using the ZIP link above.

# MOSS-Image Character & Style Catalog

A searchable library of **MOSS-Image-generated images and reusable prompts**, built from an Anima-oriented character list plus additional characters and picture styles. Browse a subject, inspect its result, and copy a prompt into your own workflow. The interface follows the Krea2 catalog's familiar operations, with English and Japanese available.

| Complete download | Images / size |
|---|---:|
| Characters | **33,937** |
| Styles | **221** |
| **Total** | **34,158** |
| Files before compression | **About 2.75 GB / 2.56 GiB** |
| Release ZIP, DEFLATE 6 | **2.05 GB / 1.91 GiB** |
| Online demo | **96 characters + 24 styles**, about **8.36 MB** |

**Release status — 2026-10-22:** **[v0.1.0 — Download the complete ZIP](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/releases/download/v0.1.0/MOSS-Image-Character-Catalog-v0.1.0.zip)** includes the local application, **33,937 character images + 221 styles**, comparison tools and both sample workflow JSON files. The online demo shows only 120 samples. GitHub **Code → Download ZIP** contains the demo and documentation; use the Release ZIP for the full collection. Model weights and reference libraries are separate downloads.

**The collection has not been selected by pass/fail judgments.** Incorrect character identities, mismatched prompts and weak style results remain included. Neither inclusion nor resemblance proves training-set coverage or accurate reproduction. The demo is an interface sample, not a list of approved results.

## Try it now

**[Browse characters](https://ukr8b3g-cmyk.github.io/MOSS-Image-Character-Catalog/) · [Browse styles](https://ukr8b3g-cmyk.github.io/MOSS-Image-Character-Catalog/?tab=styles)**

No Python, GPU or installation is needed for the demo. Switch tabs, search names, filter by work or appearance, change the order, click an image to enlarge it, and copy its prompt or original tags. Theme, language and display preferences are remembered in your browser.

| Feature | Online demo | Downloadable local version |
|---|---|---|
| Search, filters, sorting, enlargement, prompt copying | Yes, for 120 samples | Yes, for the full collection |
| Add Image and edit names, prompts, tags or workflows | — | Yes |
| Favorites, ratings, Hide and Undo | — | Yes |
| Comparison judgments and importing confirmed review JSON | — | Yes |
| Saved per-image workflow JSON | — | Yes |
| Generate images | No | Use ComfyUI separately |

The demo uses the same static-view approach as [Krea2](https://github.com/ukr8b3g-cmyk/Krea2-Character-Catalog). Only the sample site is deployed to GitHub Pages. The full collection exceeds Pages' 1 GB site limit. [Demo scope and deployment](docs/LIVE_DEMO.md).

## What the collection contains

This is a **character-list-based catalog with additional samples**, not an AnimaDex artist list. The source `anima_characters.csv` has 36,492 rows. Applying user limits removed 2,761 planned entries, and another 41 ungenerated entries were cancelled, leaving **33,690 generated source entries**.

| Added beyond that selected source list | Images |
|---|---:|
| Additional character candidates | 80 |
| Missing candidates previously reviewed in Krea2 | 160 |
| Casual-outfit additions | 2 |
| Comparison tests | 5 |
| **Additional character subtotal** | **247** |
| Picture styles and artist/medium studies | **221** |
| **Total additions** | **468** |

Outfits, forms and tests count as separate images, not unique identities. Krea2 images and verdicts are not imported. The 221 styles include 40 earlier samples and 181 later additions. Their prompts describe visual characteristics in English; painter names, media and animation styles are experiments, not accuracy guarantees.

The complete Release ZIP uses standard DEFLATE compression (level 6) and is about **2.05 GB / 1.91 GiB**. Its exact byte size and SHA256 are listed on the [release page](https://github.com/ukr8b3g-cmyk/MOSS-Image-Character-Catalog/releases/tag/v0.1.0). Model weights, personal settings, logs, locks and reference libraries are excluded. The online demo's filter counts describe its sample subset, not the full collection.

## Download and use the local version

Download the ZIP above, extract it, and keep the extracted folder together. To verify the download on Windows, run `Get-FileHash .\MOSS-Image-Character-Catalog-v0.1.0.zip -Algorithm SHA256` and compare the result with `SHA256SUMS.txt`. You need **Python 3.10+ and a web browser** to view and manage images; GPU hardware is only needed for separate generation.

| OS | Startup file |
|---|---|
| Windows | Double-click `START_HERE - Windows.cmd` |
| macOS | Open `START_HERE - macOS.command`, or run `sh './START_HERE - macOS.command'` |
| Linux | Run `sh './START_HERE - Linux.sh'` |

The preferred address is `http://127.0.0.1:8797/`. If it is occupied, use the address opened/reported by the launcher. **Stop server** ends this catalog's process; closing a tab is separate. A compatible Python is reused, or the launcher prepares a private environment. Initial dependency setup may need internet access.

### Catalog runtime check — 2026-10-22

This check concerns the **local catalog application**, separately from the ComfyUI image-generation environment below. The tested combination was **Windows, CPython 3.13.12 (64-bit) and Pillow 12.3.0 with WebP support**, in a private test environment. Python discovery was restricted to that 3.13 environment so the launcher could not silently fall back to Python 3.10.

**Confirmed in this check:**

- Catalog and comparison Python modules imported successfully. The Windows PowerShell bootstrap selected Python 3.13.12 and launched the catalog.
- The catalog `/` and editor `/editor` routes returned HTTP 200; `/api/info` and `/api/list` returned valid JSON.
- The catalog image inspector decoded one 896 × 1184 WebP sample from the v0.1.0 ZIP.
- The launcher, bootstrap and Pillow requirements used in the test matched the released ZIP. The temporary HTTP service was shut down after testing.

**Not covered by this check:** browser rendering or interactive operations; Add Image, editing, favorites, Hide/Undo, comparison judgments or review-JSON import end to end; loading or browsing all 34,158 images; macOS/Linux; or every Python/Pillow version and installation type. The HTTP test used an **empty isolated catalog fixture**, not the complete collection. Successful module imports do not establish that the comparison workflow was tested end to end.

**Python 3.10+ is the declared minimum, not a claim that every later version has been fully tested.** These results show that the limited checks above pass on 3.13.12; they do not explain an individual user's startup failure. For a failure report, include the actual Python/Pillow versions and the startup error text or `app/outputs/review_server.err.log`, if created.

#### Additional Linux validation in Codex Cloud — 2026-10-22

A separate **Codex Cloud verification report** records tests of the **official v0.1.0 Release ZIP** on **Debian 13, x86_64**, using isolated environments and **Pillow 12.3.0**. The downloaded ZIP matched the published SHA256. This records the supplied cloud report; the underlying cloud logs were not independently rechecked in the Windows session.

| CPython | Pillow | Dependency installation / pip check | Imports / startup / browser operations / save and restart |
|---|---|---|---|
| 3.10.22 | 12.3.0 | Passed | Passed |
| 3.11.17 | 12.3.0 | Passed | Passed |
| 3.12.15 | 12.3.0 | Passed | Passed |
| 3.13.16 | 12.3.0 | Passed | Passed |
| 3.14.8 | 12.3.0 | Passed | Passed |

**Reported coverage:** the shipped Linux launcher with an explicitly selected Python; syntax checks for 13 Python files and imports of 11 modules; eight real Release images (six characters and two styles); searching, enlargement, clipboard copying, sorting, language/theme switching, editing and saving, registering a test PNG, and persistence after reload and normal stop/restart. Browser operations used headless Chromium 154.0.8037.57. Japanese characters and spaces in application/environment paths and filenames were tested. Only test copies were edited; product code and original data were unchanged.

**Not covered by the cloud run:** Windows-specific startup, macOS, automatic Python discovery, automatic environment/dependency preparation, automatic desktop-browser opening, all 34,158 images or full-collection performance, end-to-end comparison/review-JSON import, or other Python patch versions/platforms. No application unit tests were bundled, so none were run. No required-function failure was reproduced; the optional `/favicon.ico` request returned 404, without blocking the tested operations. No product fix was applied.

The Linux results extend the tested combinations; they do not turn the limited Windows check above into full Windows validation or identify the cause of an individual user's startup failure. **“Python 3.10+” means 3.10 or newer, not 3.10 only.**

### Find, copy and register images

1. Select **Characters** or **Styles**. Characters start in **Copyright (most first)** order, grouped by series. **Other works / Original** appears last. Works with 20 or fewer saved images are grouped there.
2. Use **Generation (newest first)** or **Generation (oldest first)** for the saved MOSS image chronology. Click an image to inspect it. **Copy style** copies the style description without the shared demonstration scene.
3. Select **Add Image**, choose Character or Style, then select a WebP, PNG or JPEG. Names, category, reusable prompt, original tags and workflow JSON are optional. Register saves a local catalog entry; blank names use the filename.
4. **Web image search** opens your entered name/category in a new tab to help with research. Search results are not automatically imported. Use **Edit** in an image's detail view to correct its metadata later.

### Review and share decisions

Comparison is a separate human review screen, not an automatic quality judge. Configure your own AnimaDex reference installation for reference comparisons. **MOSS style images can also be judged without Krea2/AnimaDex images**; missing references are labelled and judgments are explicitly MOSS-only.

1. In comparison, choose **Accept**, **Reject** or **Hold**.
2. Select the decisions you want to share and export the confirmed **JSON**.
3. In the catalog toolbar, choose **Import review JSON**, select that file and inspect the preview.
4. Choose **Apply confirmed decisions**. Accept shows/restores an image; Reject hides it. **Image files are not deleted.** Hold, unselected and unconfirmed rows remain unchanged.

Import checks the actual MOSS image SHA256 and rejects changed/missing images. Share the JSON with people using the same catalog images. CSV list export is a different function; it is not the confirmed-decision import format. Personal references, favorites, hidden flags and review verdicts are excluded from the Release ZIP.

## Generation settings and sample workflows

These settings document the actual saved catalog workflows, not universal recommendations. The character batch prioritized practical throughput across many candidates; the style studies used a longer, unaccelerated SFT workflow.

| Setting | Character batch | Style studies |
|---|---|---|
| Diffusion checkpoint | **MOSS-Image-SFT INT8 ConvRot** | **MOSS-Image-SFT BF16** |
| Diffusion filename | `moss_image_sft_int8_convrot.safetensors` | `moss_image_sft_bf16.safetensors` |
| Text encoder | `qwen3.5_9b_int8_convrot.safetensors` | Same INT8 ConvRot encoder |
| VAE | Flux2 VAE initially; later Small Decoder | Small Decoder |
| Acceleration LoRA | `lora_latest.safetensors`, **strength 1.0** | **None** |
| Steps / CFG | **8 / 1.0** | **25 / 2.5** |
| Sampler / scheduler | `er_sde` / `simple` | Same |
| Seed | **8961184**, fixed | Same |
| Resolution / batch size | **896 × 1184 / 1** | Same |
| Denoise / negative prompt | **1.0 / empty** | Same |
| Catalog image format | **WebP quality 70**, lossy, method 0 | Same |
| Portable sample filename | **`MOSS_Image_Character_Sample.json`** | **`MOSS_Image_Style_Sample.json`** |

The character workflow uses **SFT, not Base**. An 8-step acceleration LoRA at **1.0** made the large run practical. It is not a maximum-quality benchmark of unaccelerated SFT or BF16. The first **11,694** character images used `flux2-vae.safetensors`; the later **22,243** used `full_encoder_small_decoder.safetensors`. Per-image saved workflows preserve those differences; the portable character sample uses Small Decoder.

Character prompts combine the source name, work and appearance tags with one centered subject, full-body framing, generous margins, a light-gray background and soft lighting. Human subjects receive a clothed standing-pose instruction. Source tags, the reusable copy prompt and actual generation prompt are distinct. The MOSS prompt-enhancer skill was not used for these character batches.

All **221 style images** were checked against saved workflows: SFT BF16 diffusion, INT8 encoder, Small Decoder, no LoRA, 25 steps and CFG 2.5. English descriptions specify the style's visual characteristics, then append this common scene:

```text
A single adult woman with short dark brown hair, wearing a cream shirt and a navy apron, carefully arranging a small bouquet of yellow and white flowers on a wooden worktable in a bright flower workshop. Three-quarter view from waist up, natural hand gesture, soft window light, simple uncluttered background. One person.
```

NovelAI-, Animagine- and niji-inspired entries are descriptive experiments generated with **MOSS-Image**, not those services/models. Names alone do not establish faithful reproduction. Changing the checkpoint, quantization, LoRA, steps, CFG, wording or seed can change the result; a weak sample does not establish that the subject is impossible to generate.

**Using the two samples after release:** drag the appropriate JSON into ComfyUI, select your installed model files in the Loaders, replace the character or style/scene prompt, and generate. Both examples use standard **Save Image (PNG)**. The catalog's WebP quality-70 conversion and registration are separate steps; the samples do not register images automatically. Actual style batch saving used `SaveImageKJ` for an intermediate PNG, followed by WebP conversion with prompt/workflow metadata and a separate workflow JSON.

<details>
<summary>Loader details and reproducibility</summary>

Both use `UNETLoader` with `weight_dtype=default`, `CLIPLoader` type `moss_image`/device `default`, and `EmptyFlux2LatentImage`. Characters add `LoraLoaderModelOnly`. No explicit shift modifier or `SkipLayerGuidanceDiTSimple` node is used. Character settings were checked on 2026-10-18; style settings on 2026-10-21. The initial general-purpose SFT release was announced on 2026-10-16 in the [official MOSS-Image repository](https://github.com/OpenMOSS/MOSS-Image#news). These results do not evaluate a future anime-specific checkpoint.

Prompt, image conversion/registration, model loading and system load affect timing. ComfyUI execution time and total time including saving/registration are distinct measurements. Identical filenames do not ensure identical future model weights or outputs.

</details>

### Model downloads

| File | Source | ComfyUI model folder |
|---|---|---|
| `moss_image_sft_int8_convrot.safetensors` | [Comfy-Org: SFT INT8 ConvRot](https://huggingface.co/Comfy-Org/MOSS-Image/blob/main/diffusion_models/moss_image_sft_int8_convrot.safetensors) | `models/diffusion_models` |
| `moss_image_sft_bf16.safetensors` | [Comfy-Org: SFT BF16](https://huggingface.co/Comfy-Org/MOSS-Image/blob/main/diffusion_models/moss_image_sft_bf16.safetensors) | `models/diffusion_models` |
| `qwen3.5_9b_int8_convrot.safetensors` | [Comfy-Org: encoder](https://huggingface.co/Comfy-Org/MOSS-Image/blob/main/text_encoders/qwen3.5_9b_int8_convrot.safetensors) | `models/text_encoders` |
| `flux2-vae.safetensors` | [Comfy-Org: original VAE](https://huggingface.co/Comfy-Org/MOSS-Image/blob/main/vae/flux2-vae.safetensors) | `models/vae` |
| `full_encoder_small_decoder.safetensors` | [Black Forest Labs: Small Decoder](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder/blob/main/full_encoder_small_decoder.safetensors) | `models/vae` |
| `lora_latest.safetensors` | [lodestones: 8-step LoRA](https://huggingface.co/lodestones/MOSS-Image-SFT-8-steps-dmd/blob/main/lora_latest.safetensors) | `models/loras` |

Use a MOSS-Image-capable ComfyUI. Sample subfolders may differ from yours; choose the installed files in the corresponding Loaders. Models and their licenses are provided by their respective publishers.

### Generation PC

**RTX 5060 Ti (16 GB VRAM), Ryzen 9 3900X, 64 GB system RAM, Windows 11 Pro.** This is the rendering environment, not a minimum requirement for browsing the catalog.

<details>
<summary>Recorded software environment — 2026-10-18</summary>

| Component | Recorded value |
|---|---|
| OS | Windows 11 Pro, build 26200 |
| CPU | AMD Ryzen 9 3900X, 12 cores / 24 threads |
| RAM | 64 GB installed; about 63.93 GiB usable |
| GPU / driver | NVIDIA GeForce RTX 5060 Ti, 16 GB / 616.92 |
| ComfyUI | 0.41.0, commit `5cc4b870094c89090db54bd8d12649dcaf89f2ba` |
| Python / PyTorch | 3.12.14, 64-bit / 2.14.1+cu130 |

This is the initial recorded setup; later runs can differ. CUDA 13.0 denotes the PyTorch build, not proof of a separate CUDA Toolkit installation. Mac/Linux launchers are inherited from the Krea2 application; this MOSS package has not received a fresh three-OS CI run or physical macOS/Linux desktop validation.

</details>

## Project scope and license

The UI is adapted from [Krea2 Character Catalog](https://github.com/ukr8b3g-cmyk/Krea2-Character-Catalog) and aims for familiar AnimaDex-like browsing. This is an independent project, not an official OpenMOSS, Krea2 or AnimaDex product.

Maintainer-authored documentation and the published demo code are covered by [MIT](LICENSE). Generated sample images and third-party character/model rights are addressed separately in [NOTICE.md](NOTICE.md). Model weights, reference libraries, credentials and private review state are not published. Report an issue with the image/style name and catalog version; accuracy corrections are welcome.
