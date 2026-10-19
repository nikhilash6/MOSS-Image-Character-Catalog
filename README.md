[日本語](README.ja.md)

# MOSS-Image Character Catalog

**Work in progress — public release preparation.**

A local catalog for browsing MOSS-Image character-generation results and their prompts. Inspired by the Krea2 Character Catalog workflow, with a separate MOSS-Image image collection.

The application, image collection and downloadable package are not included in this documentation draft. Release scope, image count and installation instructions will be finalized after generation and packaging checks. No release date is set.

## Scope

The local application supports searching and filtering saved character images, inspecting reusable prompts and saved workflows, and adding or editing local records. Works with 20 or fewer registered images are grouped under an expandable Other works entry while retaining their individual names.

Optional comparison with a separately installed AnimaDex reference collection supports human review. Reference availability or a generated resemblance is not a confirmed character-accuracy verdict. The Style section is reserved for later work.

## About the images

The current collection is being generated with MOSS-Image-SFT, INT8 ConvRot weights and an 8-step acceleration LoRA. Generation settings have changed during production; inspect each image's saved workflow for its actual settings. This collection is a practical reference for those configurations, not a controlled benchmark or a complete inventory of the model's learned characters.

Source character and work names and available appearance tags come from a user-provided Anima-oriented list. These names and tags do not guarantee that MOSS-Image reproduces the intended identity. Entries require human review; incorrect identities and imperfect results may remain.

## Availability

- Application and image package: preparing for release.
- Setup, requirements and download links: to be confirmed against the packaged build.
- Model weights: installed separately; not part of the planned catalog package.
- AnimaDex references and database: separate from the catalog; redistribution scope remains to be reviewed.
- License: the current documentation is licensed under the [MIT License](LICENSE). See [NOTICE.md](NOTICE.md) for scope. This does not license the application, images, models, or third-party materials that are not included here.

This is an independent catalog project. It is not presented as an official OpenMOSS or AnimaDex product. Character and work names identify their respective subjects.

## Project status

Documentation draft prepared on 2026-10-19. No fixed image count, completed quality review, supported-platform guarantee or published release is claimed here.
