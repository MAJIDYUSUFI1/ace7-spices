# Ace7 Spices — Website

A complete static marketing website for **Ace7 Spices™** (a brand of **Ace Adam International LLP**) — a B2B exporter of single-origin Indian red chilli, coriander and turmeric.

15 pages, hand-built in plain HTML / CSS / JS. No framework, no build step, no dependencies to install. Open `index.html` and it runs.

---

## What's inside

```
ace7/
├── index.html              Home
├── about.html              Our story
├── process.html            Our process (source → sort → cold-press → pack)
├── sustainability.html     Fair sourcing
├── quality.html            Quality & traceability (what we test, lot codes, docs)
├── harvest-calendar.html   ★ Interactive 12-month harvest calendar
├── products.html           Range overview
├── red-chilli.html         Guntur red chilli — 16-variety catalogue + ★ interactive SHU/ASTA scale
├── coriander.html          Rajasthan coriander
├── turmeric.html           Sangli & Salem turmeric
├── custom-blends.html      Custom blends, private & white label
├── industries.html         Markets: HORECA · GCC · Europe · India
├── contact.html            ★ Trade inquiry form + FAQ
├── privacy-policy.html     Legal
├── terms.html              Legal
├── assets/
│   ├── styles.css          The whole design system
│   └── script.js           All interactivity
├── images/                 ← drop generated images here (currently empty)
├── IMAGE-PROMPTS.md         44 ready-to-use Nano Banana prompts, one per image
└── README.md               this file
```

`★` = interactive feature.

---

## Adding the images (the only thing left to do)

The site is built to look finished **before** any images exist: every empty slot shows a clean labelled placeholder. To replace them with real photos:

1. Open **`IMAGE-PROMPTS.md`** — it has one detailed prompt per image, plus a shared style line to keep them consistent.
2. Generate each image (Nano Banana / your tool of choice) at the aspect ratio noted.
3. Save it with the **exact filename** shown into the `images/` folder.
4. Refresh the page — the image appears automatically. No code changes.

Keep the `.jpg` extension (or update the `src` in the HTML if you use another format).

---

## The inquiry form (important)

The contact form is **front-end only** — there's no server behind it yet. On submit it validates, shows a success state, and opens a pre-filled email to `support@ace7spices.com` so nothing is lost. To make it submit silently in the background, wire it to a form backend — the quickest options:

- **Formspree** — create a form, then set the `<form>` action to your endpoint and switch the handler to a normal POST.
- **Web3Forms / Getform / Basin** — same idea, paste an access key.
- **Your own** — POST the JSON the script already assembles to any endpoint.

The relevant code is the `data-inquiry` form in `contact.html` and the form handler in `assets/script.js` (look for `data-inquiry`).

---

## Fonts

Loaded free from Google Fonts via the CDN (already linked in every page `<head>`):
- **Fraunces** — display headings
- **IBM Plex Sans** — body text
- **IBM Plex Mono** — spec readouts, lot codes, data labels

No local font files needed. (If you ever go fully offline, self-host them and update the `<link>` tags.)

---

## Deploying

It's static, so anything works. Easiest:

- **Cloudflare Pages / Netlify / Vercel** — drag the `ace7` folder in, done.
- **GitHub Pages** — push the folder, enable Pages.
- **Any web host** — upload the folder to your web root.

Point `ace7spices.com` at it and you're live.

---

## Brand quick-reference

- **Name:** Ace7 Spices™ · **Parent:** Ace Adam International LLP
- **Idea behind the "7":** the *Ace7 Standard* — seven quality marks every lot must earn
- **Colours:** roast near-black `#1E150F`, ivory paper `#F7F1E6`, scarlet `#C8102E`, forest `#1B5E3A`, turmeric `#D98E04`
- **Contact:** support@ace7spices.com · +91 74150 32994 · ace7spices.com

---

*Built page-by-page in plain HTML/CSS/JS so it's easy to edit by hand — open any `.html` file and the structure reads top to bottom.*
