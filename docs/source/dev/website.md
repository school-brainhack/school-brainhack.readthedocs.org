# Website Overview

This document provides a technical overview of the Brainhack School website infrastructure. It is intended for developers and maintainers. The main website repository is hosted at: [https://github.com/school-brainhack/school-brainhack.github.io](https://github.com/school-brainhack/school-brainhack.github.io) and the website is live at: [https://school-brainhack.github.io](https://school-brainhack.github.io)

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

## 🔗 Registration Page (Hugo site)

To edit the registration page on the main website, update the Markdown file:

```
content/en/register.md
```

Embed the Google Form using standard HTML inside the markdown file, for example:

```html
<iframe src="https://docs.google.com/forms/d/e/EXAMPLE_FORM_ID/viewform?embedded=true" width="100%" height="1200" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
```

Replace the `EXAMPLE_FORM_ID` with the actual form ID provided by Google.

### 🌐 Managing Past Editions

To ensure proper navigation between yearly editions of the website, it's recommended to fork each year's site into its own GitHub organization or repo (e.g. 2025-school-brainhack.github.io).

The past editions are referenced in the main site's config (usually in the navigation menu) with entries like:
```
- parent: past
  name: 2024
  url: https://2024-school-brainhack.github.io/
- parent: past
  name: 2022
  url: https://2022-school-brainhack.github.io/
- parent: past
  name: 2021
  url: https://psy6983.brainhackmtl.org/
- parent: past
  name: 2020
  url: https://school2020.brainhackmtl.org/
- parent: past
  name: 2019
  url: https://brainhackmtl.github.io/school2019/
- parent: past
  name: 2018
  url: https://brainhackmtl.github.io/school2018/
```
When preparing a new edition:
1. Fork the current repository into a dedicated organization (e.g. `2025-school-brainhack`)
2. Set GitHub Pages to publish from `main` or `docs/`
3. Update the past editions list on the main site
## 🧩 Sidebar Templates and Localised Content

The Brainhack School website uses custom sidebar templates based on page context:

- `layouts/partials/sidebar.html`: Used on the **project gallery**
- `layouts/partials/sidebar_modules.html`: Used for **teaching modules**
- `layouts/partials/sidebar_sites.html`: Used for the **list of participating sites**

Each of these partials can be injected into the main layout depending on the active section.

### Sidebar Content Source

Text blocks such as:

```go
<p>{{ T "SidebarSub" | markdownify }}</p>
```

Reference the translation string with ID `SidebarSub` in the file `i18n/en.yaml`. This is part of Hugo’s i18n system, which was originally designed for multilingual support but is now also used as a message registry.

To update or remove this kind of string:

1. Open `i18n/en.yaml`
2. Edit the relevant `id` (e.g. `SidebarSub`)
3. Rebuild the site locally with `hugo server -D`

## 🗂️ The i18n File as a Message Registry

The file `i18n/en.yaml` contains a list of string identifiers and their English translations. While originally intended for multilingual support, it is now used to centralize fixed text elements like button labels, form fields, and sidebar messages.

Example entries:

```yaml
- id: home
  translation: "Home"
- id: contactTitle
  translation: "Contact"
- id: contactForm
  translation: "Contact form"
- id: contactName
  translation: "Your Name"
- id: contactSend
  translation: "Send Message"
```

To locate uneditable static text, search this file using `grep`.

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
