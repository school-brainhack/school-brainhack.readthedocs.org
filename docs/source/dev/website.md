# Website Overview

This document provides a technical overview of the Brainhack School website infrastructure. It is intended for developers and maintainers.

## Goals

The Brainhack School website serves several purposes:

* Central hub for course materials, lectures, and projects
* Archive of past editions
* English-only content
* Static and easily deployable via GitHub Pages

We use **Hugo** for its static site generation, GitHub Pages compatibility, and scalability, despite its... eccentricities.

---

## Directory Layout (as of 2025)

```
├── config.yaml                 # Site configuration
├── content/                   # Markdown-based content
│   └── en/                    # English pages
│       └── sites/             # One folder per local site (each with image + index.md)
├── data/                      # Structured data for modules, instructors, etc.
│   └── en/
│       ├── clients/           # YAML files defining sponsor entries (1.yaml, 2.yaml, ...)
│       ├── instructors.yaml   # List of global team members
│       └── carousel/          # Slides for homepage carousel (data_science.yaml, etc.)
├── static/                    # Static assets (img, css, etc.)
│   └── img/                   # Logos, favicons, media
├── layouts/                   # Custom Hugo templates
│   └── partials/, _default/, etc.
├── themes/                    # Contains hugo-universal-theme
├── public/                    # Output folder (auto-generated)
├── .github/workflows/         # GitHub Actions workflows
```

---

## Updating `config.yaml`

This file contains the core Hugo configuration.

### Top-Level Fields

```yaml
baseURL: "https://school-brainhack.github.io/"
languageCode: "en"
title: "Brainhack School"
theme: "hugo-universal-theme"
defaultContentLanguage: "en"
style: green
logo: "img/logo_brainhack_2025.png"
logo_small: "img/logo-small_2025.png"
```

### Disabling Sponsors Section

To hide the sponsors section (labeled "Clients" in the theme), locate the following block in `config.yaml` and set `enable: false`:

```yaml
clients:
  enable: true
  title: Sponsors
  subtitle: ""
```

Change to:

```yaml
clients:
  enable: false
```

This will disable the rendering of the sponsors block from the homepage.

### Editing Sponsors

Sponsor entries are defined in separate YAML files located in `data/en/clients/`:

```
data/en/clients/
├── 1.yaml
└── 2.yaml
```

Each file typically contains:

```yaml
title: Sponsor Name
image: "img/sponsor-logo.png"
url: "https://sponsor-website.com"
```

To add or remove sponsors, simply create, edit, or delete these numbered `.yaml` files.

### Editing the Global Team

The list of instructors and organizers shown as the "Global Team" is stored in a single YAML file:

```
data/en/instructors.yaml
```

Each entry includes tags like:

```yaml
- name: Lune Bellec
  gh: pbellec
  email: lune.bellec@criugm.qc.ca
  website:
  affiliation: University of Montreal
  urlaff: https://umontreal.ca
```

**Supported tags:** `name`, `gh` (GitHub handle), `email`, `website`, `affiliation`, `urlaff`, `twitter`, `week`, `weight`, and `content`.

> 💡 Image: if `gh` is defined, the image is pulled from GitHub. Otherwise, add a custom image to `static/img/instructors/`.

To remove someone from the team, delete their entry. To reorder, use `weight` or simply rearrange the list.

### Editing the Homepage Carousel

The top homepage carousel is one of the signature visual features of the site. Each slide is defined in a separate YAML file under:

```
data/en/carousel/
```

Examples include:

```
├── code.yaml
├── brainhack_school.yaml
├── hpc.yaml
├── ml.yaml
├── neuroimaging.yaml
├── open_data.yaml
└── visu.yaml
```

The file `brainhack_school.yaml` is typically used for the first (main) slide and must be updated each year.

Sample structure:

```yaml
weight: 0
title: "Brainhack School"
description: >
  <ul class="list-style-none">
    <li>Worldwide</li>
    <li>2025</li>
  </ul>
image: "img/carousel/fig_data_science.png"
```

You can control the order of the slides with the `weight` field. Lower values appear first.

Images must be stored in `static/img/carousel/`.

### Managing the List of Sites

Each participating site has its own folder and landing page under:

```
content/en/sites/
```

Example structure:

```
├── criugm/
│   ├── criugm.png
│   └── index.md
├── polytechnique/
│   ├── polytechnique.jpeg
│   └── index.md
├── toronto/
│   ├── toronto.png
│   └── index.md
└── _index.md              # Overview index for all sites
```

Each site folder must include:

* an `index.md` file with the site's description and metadata
* a site logo/image referenced from the markdown (can be `.jpg`, `.png`, or `.jpeg`)

To add a new site:

1. Create a new subfolder under `content/en/sites/`
2. Add `index.md` with front matter
3. Add a representative image

> 💡 The `_index.md` file provides the parent page that lists all sites.

---

## Technology Stack

* **Hugo** (`v0.108.0`, extended edition)
* **GitHub Pages** for deployment
* **GitHub Actions** for CI/CD
* **YAML/Markdown** for content and config
* Optional: `dart-sass-embedded` for themes using SASS

---

## Deployment Process

* A GitHub Actions workflow (`.github/workflows/hugo.yml`) builds the site and uploads it to GitHub Pages.
* Only commits to `main` trigger production builds.
* Artifacts are built into `public/` by Hugo.

---

## Known Pain Points

* Hugo’s layout system is inconsistent across content types
* Theme (hugo-universal-theme) is dated
* Hugo GitHub Action needs regular updating

---

## Developer Tips

* Use `hugo server -D` for local development with drafts
* Use `tree -L 2`   liberally to stay sane and map your environment
