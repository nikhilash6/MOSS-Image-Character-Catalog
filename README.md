[日本語](README.ja.md)

# MOSS-Image Character & Style Catalog

**Release preparation — updated 2026-10-22. The counts and checks below describe the locally prepared package. This GitHub repository currently publishes documentation; the application, image ZIP and sample JSON downloads have not yet been published.**

**v0.1.0 — local catalog with 33,937 character images and 221 style images.** Browse saved images, prompts and workflows. English is the initial interface language; Japanese is available. Model weights are not included. Krea2 images and review verdicts have not been imported.


## Collection and package size

**A local MOSS-Image image/prompt catalog built from an Anima-oriented character-tag list, with additional character candidates and picture styles. This is not the AnimaDex artist list.**

| Content | Images |
|---|---:|
| Characters | **33,937** |
| Styles | **221** |
| **Total** | **34,158** |
| Uncompressed file total | **About 2.75 GB / 2.56 GiB** |
| Standard ZIP compression (DEFLATE 6), approximate | **2.05 GB / 1.91 GiB** (compressed size measured without saving a ZIP) |

Characters comprise 33,690 generated entries from the original CSV, plus 80 additional candidates, 160 missing candidates previously reviewed in Krea2, two casual-outfit additions and five comparison tests. The original CSV has 36,492 rows; user caps removed 2,761 planned entries and 41 ungenerated entries were cancelled. Outfits, forms and tests count as separate images, not unique characters. The additions beyond that selected source list are 247 character images and 221 styles. Package size excludes model weights, personal settings and reference databases and varies with ZIP software/settings.

**The collection has not been filtered by pass/fail judgments of image quality, character identity or style accuracy.** Images that do not match their names/prompts, and styles that did not work well, remain included. Registered images are retained for users to inspect and review themselves. Personal hidden flags and review verdicts are not part of the distribution ZIP.

## Character generation settings (initial setup, 2026-10-18)

**These are results from the initial-release MOSS-Image-SFT model with an 8-step acceleration LoRA.** This catalog uses the SFT checkpoint, not MOSS-Image-Base, and uses INT8 ConvRot model/encoder files rather than the original full-precision weights. The LoRA reduces rendering time for the large catalog. This is a practical reference for this particular setup, not an evaluation of the unmodified Base model or a maximum-quality benchmark.

Settings below were checked against a saved generated image's workflow and the active API workflow on **2026-10-18**. The initial Base/SFT public release was announced on **2026-10-16** in the [official repository](https://github.com/OpenMOSS/MOSS-Image#news).

| Setting | Actual catalog setting |
|---|---|
| Model family/checkpoint | MOSS-Image-SFT, initial public release |
| Diffusion model file | `MOSS-Image/moss_image_sft_int8_convrot.safetensors` |
| Model loader | `UNETLoader`, `weight_dtype=default` |
| Text encoder file | `qwen3.5_9b_int8_convrot.safetensors` |
| Text encoder loader | `CLIPLoader`, type `moss_image`, device `default` |
| VAE | `flux2-vae.safetensors` |
| Acceleration LoRA | [lodestones/MOSS-Image-SFT-8-steps-dmd](https://huggingface.co/lodestones/MOSS-Image-SFT-8-steps-dmd), file `moss_image/lora_latest.safetensors` |
| LoRA loader / model strength | `LoraLoaderModelOnly` / **1.0** |
| Sampler / scheduler | **`er_sde` / `simple`** |
| Steps / CFG / denoise | **8 / 1.0 / 1.0** |
| Seed | **8961184**, fixed |
| Canvas / batch size | **896 × 1184 / 1** (`EmptyFlux2LatentImage`) |
| Negative prompt | Empty |
| Additional guidance | No `SkipLayerGuidanceDiTSimple` or explicit shift modifier node in this workflow |
| Final catalog image | WebP, quality **70**, `lossless=False`, method **0**; embedded prompt/workflow metadata and a separate workflow JSON |

The acceleration LoRA was used to check a large number of candidates in a practical amount of time. The character generation run and character sample use model strength **1.0**. These results do not represent unaccelerated SFT or BF16 character generation.

The source is the user-supplied **Anima-oriented character tag list** (`anima_characters.csv`), also used for the Krea2 catalog. This project tests how MOSS-Image reproduces characters when prompted with that list; Anima is the tag-list context, not the image-generation model used here. The list is not an official inventory of characters learned by MOSS-Image, and its tags do not guarantee correct identity or full compatibility.

The generation prompt combines the source CSV's character name, work and available appearance tags with a shared full-body framing instruction: one subject, centered, approximately 65% of the canvas, generous margins, a light-gray background and soft lighting. Human subjects use a clothed standing-pose instruction. The original tags, reusable copy prompt and actual generation prompt are stored separately. The MOSS prompt-enhancer skill was **not used** for the character batches described here.

**Character sample: `MOSS_Image_Character_Sample.json`**. Drag it into ComfyUI and select your installed model files. It uses SFT INT8 ConvRot, 8-step LoRA strength 1.0, 8 steps, CFG 1.0, er_sde/simple, seed 8961184, 896×1184 and Small Decoder. Change the English character/appearance prompt to try another subject. The first 11,694 character images used the original Flux2 VAE; the later 22,243 used Small Decoder. Per-image saved workflows preserve the actual settings. The portable sample uses ordinary Save Image for PNG output; catalog WebP quality-70 conversion and registration are separate operations.

**Interpretation limits:** SFT fine-tuning, quantization, the acceleration LoRA, eight-step sampling, prompt wording and seed can all affect appearance and character fidelity. Results are not guaranteed to match Base, full-precision weights, SFT without the LoRA, or different sampling settings. A weak example does not establish that the character is impossible to generate; resemblance does not establish accurate identity or prove training-set inclusion. Generated entries await human review.

**Future anime model:** In a [developer AMA](https://www.reddit.com/r/StableDiffusion/comments/1x7zf1r/hey_guys_im_one_of_the_core_developers_of/), an OpenMOSS core developer stated that releasing an anime version was a priority. This catalog documents the initial general-purpose SFT setup above, not that planned anime-specific model. No release date or expected quality is asserted here, and results should not be transferred to a future checkpoint without testing.

## Style image generation (2026-10-21)

The current English-caption style studies use the settings below, checked against the saved Rembrandt test workflow and the batch runners on **2026-10-21**. They use a different setup from the character-image batch documented above.

| Setting | Style-study setting |
|---|---|
| Diffusion model | **MOSS-Image-SFT**, `MOSS-Image/moss_image_sft_bf16.safetensors` |
| Model loader | `UNETLoader`, `weight_dtype=default` |
| Text encoder | `qwen3.5_9b_int8_convrot.safetensors`; `CLIPLoader`, type `moss_image`, device `default` |
| VAE | `full_encoder_small_decoder.safetensors` |
| LoRA | **None**; no LoRA loader in this workflow |
| Steps / CFG / denoise | **25 / 2.5 / 1.0** |
| Sampler / scheduler | **`er_sde` / `simple`** |
| Seed | **8961184**, fixed |
| Canvas / batch size | **896 × 1184 / 1** |
| Negative prompt | Empty |
| Final image | **WebP, quality 70**, `lossless=False`, method **0** |
| Saving | `SaveImageKJ` writes an intermediate PNG; the local registration helper converts it to WebP and preserves embedded metadata and a separate workflow JSON |

The diffusion checkpoint is BF16, but the text encoder is INT8 ConvRot: this is not an entirely BF16 pipeline. These settings describe this catalog's actual style studies, not universal model recommendations. **Style sample: `MOSS_Image_Style_Sample.json`**. Drag it into ComfyUI and change the English style description or shared scene. It uses ordinary Save Image for PNG output; WebP conversion and catalog registration are separate. Character settings differ as described above.

Style prompts use an English description of visible drawing features, materials, contours, forms and coloring. Named-artist studies include the artist's name in prose, without an `@` prefix or repeated artist tags. The local **moss-image-prompt-enhancer** caption compiler is used to prepare these prompts; it does not generate the images or call an external enhancement service. The reusable copy prompt contains the style paragraph; the actual generation prompt adds this shared scene:

```text
A single adult woman with short dark brown hair, wearing a cream shirt and a navy apron, carefully arranging a small bouquet of yellow and white flowers on a wooden worktable in a bright flower workshop. Three-quarter view from waist up, natural hand gesture, soft window light, simple uncluttered background. One person.
```

Media such as puppetry or sculpture reinterpret the same person, clothing, flowers and action in that medium. NovelAI-, Animagine- and niji-inspired entries are descriptive experiments rendered with **MOSS-Image**, not images generated by those services or checkpoints. Their names do not guarantee reproduction of a particular model's output. Different styles may produce visually similar results; human review is still needed.

Inspect each image's saved workflow for the actual generation graph. Generation time varies by prompt, model loading and system load; ComfyUI execution time and total time including conversion and registration are recorded separately.

## PC and software used for generation

Observed on **2026-10-18** from local hardware information and the running ComfyUI API:

| Component | Generation environment |
|---|---|
| OS | Windows 11 Pro, build **26200** |
| CPU | AMD Ryzen 9 **3900X**, 12 cores / 24 threads |
| System RAM | **64 GB** installed; approximately 63.93 GiB reported usable |
| GPU | NVIDIA GeForce **RTX 5060 Ti, 16 GB VRAM** |
| NVIDIA driver | **616.92** |
| ComfyUI | **0.41.0**, local checkout `5cc4b870094c89090db54bd8d12649dcaf89f2ba` |
| ComfyUI Python | **3.12.14**, 64-bit |
| PyTorch | **2.14.1+cu130** (CUDA 13.0 build) |

These describe the machine used to render this catalog, not minimum hardware requirements. CUDA 13.0 identifies the PyTorch build; it is not a claim that a separate CUDA Toolkit is installed. Rendering speed depends on settings, prompts, model residency and other load. The catalog browser itself is separate from GPU image generation and does not require this GPU merely to view saved images. Mac/Linux launchers do not imply that rendering was tested on those systems.

## Start

Extract or keep this whole folder together. Python **3.10+** and a browser are required.

| OS | Open |
|---|---|
| Windows | Double-click **START_HERE - Windows.cmd** |
| macOS | **START_HERE - macOS.command**, or `sh './START_HERE - macOS.command'` |
| Linux | `sh './START_HERE - Linux.sh'` |

The intended local address is **http://127.0.0.1:8797/**. If the port is busy, the launcher chooses an available address and reports it. Stop server stops this catalog only.

A compatible existing Python is reused. Otherwise the inherited launcher can create a private environment; it does not install into an existing Python. First dependency setup may require internet access.

## Register images

1. Open the catalog and select **Add image**.
2. Choose a WebP, PNG, or JPEG. Select **Character** or **Style**.
3. Optionally enter a name, work/category, reusable prompt, original tags, and workflow JSON. Text fields are optional.
4. Register the image. Click a saved image to inspect it and choose **Edit** for corrections.

**Close (keep draft)** preserves Editor inputs; **Cancel (discard inputs)** discards unsaved inputs; saving/registering commits them. Hiding cards is reversible and does not delete image files.

Images and local metadata are saved under **app/outputs/user_items/**, **app/outputs/user_catalog.json**, and **app/outputs/user_catalog_edits.json**. Back up app/outputs before cleanup or migration. Files copied into arbitrary folders are not automatically imported: use Add image.

## Workflow and scope

This distribution contains saved images for browsing and two ComfyUI samples: `MOSS_Image_Character_Sample.json` and `MOSS_Image_Style_Sample.json`. Generation batch tools are not included. Opening the catalog alone does not submit generation. Optional AnimaDex comparison is separate; see the comparison setup guide included in the prepared package. Models must be installed separately.

Official model files: [Comfy-Org/MOSS-Image](https://huggingface.co/Comfy-Org/MOSS-Image). This template is adapted from the Krea2 catalog v0.9.6 application. Character/style accuracy and generation quality are not established by the template. Mac/Linux launchers are included, but this new MOSS-Image template has not received a fresh three-OS CI run.

## Included styles and browsing

All 221 saved style workflows were checked: the 40 earlier images and the additional 181 share the BF16 SFT diffusion, INT8 encoder, no-LoRA, 25-step/CFG-2.5 setup above. The Style tab displays these images. Generation (newest first) and Generation (oldest first) use the saved MOSS image time. Copy style copies only the style caption, leaving out the common demonstration scene. The UI uses familiar Krea2 catalog operations and aims for AnimaDex-like usability; it is a separate application.

Optional comparison requires your own separately configured AnimaDex database and images. Styles remain visible as MOSS-only images when no unambiguous artist/tag reference exists. Missing references are labelled explicitly, without inventing a reference. Styles without a reference support Accept, Reject and Hold judgments of the MOSS image itself. Export only confirmed selected Accept/Reject decisions and use **Import review JSON** at the top of the catalog, preview the changes, and confirm them to update visibility (Accept shows, Reject hides without deleting images). Held and unselected entries remain unchanged. MOSS-only judgments are recorded explicitly and the actual MOSS image SHA256 is checked before applying. No personal reference library or comparison verdicts are bundled. Inclusion is not a verdict that every style was successfully reproduced. Generation batches, intermediate PNGs, progress logs and model weights are excluded.

## Model downloads and samples


| File | Download |
|---|---|
| `moss_image_sft_int8_convrot.safetensors` | [Comfy-Org / MOSS-Image INT8 ConvRot](https://huggingface.co/Comfy-Org/MOSS-Image/blob/main/diffusion_models/moss_image_sft_int8_convrot.safetensors) |
| `moss_image_sft_bf16.safetensors` | [Comfy-Org / MOSS-Image SFT BF16](https://huggingface.co/Comfy-Org/MOSS-Image/blob/main/diffusion_models/moss_image_sft_bf16.safetensors) |
| `qwen3.5_9b_int8_convrot.safetensors` | [Comfy-Org / text encoder](https://huggingface.co/Comfy-Org/MOSS-Image/blob/main/text_encoders/qwen3.5_9b_int8_convrot.safetensors) |
| `flux2-vae.safetensors` | [Comfy-Org / original VAE](https://huggingface.co/Comfy-Org/MOSS-Image/blob/main/vae/flux2-vae.safetensors) |
| `full_encoder_small_decoder.safetensors` | [Black Forest Labs / FLUX.2 Small Decoder](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder/blob/main/full_encoder_small_decoder.safetensors) |
| `lora_latest.safetensors` | [lodestones / 8-step acceleration LoRA](https://huggingface.co/lodestones/MOSS-Image-SFT-8-steps-dmd/blob/main/lora_latest.safetensors) |

Put diffusion models under ComfyUI models/diffusion_models, the encoder under models/text_encoders, VAE under models/vae and LoRA under models/loras. If names/subfolders differ from the samples, select your installed files in each Loader. Use a MOSS-Image-capable ComfyUI. Model weights are separate downloads; future weights with the same filename may differ.

**Style sample: `MOSS_Image_Style_Sample.json`** — SFT BF16 diffusion, INT8 encoder, Small Decoder, no LoRA, 25 steps, CFG 2.5, er_sde/simple, seed 8961184, 896×1184. **Character sample: `MOSS_Image_Character_Sample.json`** — SFT INT8 ConvRot diffusion, INT8 encoder, Small Decoder, LoRA strength 1.0, 8 steps, CFG 1.0, same sampler/seed/resolution. Drag the appropriate JSON into ComfyUI. Both portable examples use ordinary Save Image (PNG); the saved catalog images were converted to WebP quality 70 afterward. Neither sample automatically registers an image.

## Add your images and share human judgments

Use **Add Image** for a character or style. Choose an image, enter any needed name/category/prompt/tags/workflow, and press Register. **Web image search** opens the entered name/category in a new tab; it does not automatically import search results.

In comparison, choose Accept, Reject or Hold, select decisions, and export the confirmed JSON. In the catalog toolbar, choose **Import review JSON**, select that file, inspect the counts and preview, then click **Apply confirmed decisions**. Accept shows/restores an image; Reject hides it without deleting it. Held, unselected and unconfirmed rows remain untouched. A changed/missing MOSS image rejects the import. Favorites, ratings and image files are preserved.

Share this decision JSON with people using the same catalog images. This is separate from CSV list export. Styles can be reviewed without reference images; the export records MOSS-only judgment explicitly. Import checks MOSS image identity and imports the human judgments; it does not redo a reference comparison or automatically assess quality on the recipient PC.

Characters initially use **Copyright (most first)**: series are grouped and ordered by image count, with Original and small works placed last under **Other works / Original**. Generation newest/oldest options remain available.

<img width="1887" height="1013" alt="image" src="https://github.com/user-attachments/assets/c71a2f9b-4540-4596-be2f-db8b5a50720e" />

## Publication scope and license

The currently published documentation is licensed under the [MIT License](LICENSE); see [NOTICE.md](NOTICE.md) for scope. This does not license the unpublished application, images, models or third-party materials. This independent project is not an official OpenMOSS or AnimaDex product. Character and work names identify their respective subjects.
