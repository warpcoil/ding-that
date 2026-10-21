# Ding That: Astra child theme

A child theme for [Astra](https://wpastra.com/) for dingthat.com, home of the free Ding That dingbat fonts. It follows the same structure as the Graph Lines and PDF Wire themes, and it's built for accessibility first:

- **Fonts:** Atkinson Hyperlegible Next, JetBrains Mono and the three Ding That fonts are self-hosted, so pages make no requests to Google.
- **Colours:** every text colour meets WCAG 2.2 AA contrast. A dark scheme follows the visitor's system setting.
- **Keyboard:** one visible focus ring everywhere, and a skip link that shows when focused.
- **Touch:** buttons and menu items are at least 44 px tall.
- **Display settings:** supports forced colours (Windows High Contrast) and reduced motion, and has a clean print style.
- **Look:** a violet brand colour, a faint dot grid in the hero (like a type designer's layout paper), a printed specimen card as the hero illustration, and a dark band for the licence and open source.
- **Glyphs:** every glyph picture on the site is hidden from screen readers and has its name written next to it.
- **Type tester:** the tabs follow the ARIA tab pattern (arrow keys move between fonts), every glyph button has a spoken name, and additions are announced in a live region.

## What's included

| Path | What it is |
| --- | --- |
| `style.css` | Theme header and all styles. Maps the design onto Astra's nine global colours. |
| `functions.php` | Loads the styles, preloads fonts, adds editor styles, registers block styles and the pattern category, adds the `[ding]` and `[ding_tester]` shortcodes, and adds Customizer settings for the download and source-code addresses. |
| `patterns/` | Nine block patterns: hero, "Three fonts" cards, **glyph gallery** (16 glyphs from each font), steps, "What every font includes", the dark licence and open-source band, **type tester**, a call-to-action box, and **Complete home page**. |
| `page-content/` | Block markup for The fonts (full character maps), Help, FAQ, Accessibility statement, Privacy notice, Open source and the Type tester. |
| `fonts/` | WOFF2 fonts and their SIL Open Font License texts, including Ding That GUI, Shapes and Objects. |
| `assets/` | Logo (SVG and PNG), icon SVG, site icon (SVG and 512 × 512 PNG), and the type tester's scripts in `assets/js/`. |
| `screenshot.png` | Shown in Appearance › Themes. |

**Block styles** you can pick in the editor's Styles panel:

| Block | Style | Use |
| --- | --- | --- |
| Group | **Notice** | Tinted box with an information icon, for tips and important notes |
| List | **Contents** | "On this page" box with two columns on wide screens |
| Paragraph | **Eyebrow label** | Small rounded label above a heading |

**Glyphs in your own content:**

- Shortcode: `[ding font="objects" key="h"]` shows a decorative house. Add `label="Home"` when the glyph carries meaning, and screen readers announce the label instead of the letter. `font` is `gui`, `shapes` or `objects`.
- HTML: `<span class="dt-g dt-g--shapes" aria-hidden="true">v</span>` in a Custom HTML block.
- Box drawing: a Custom HTML block with `<pre class="dt-boxdraw">…</pre>` sets the GUI font with tight lines.
- Type tester: `[ding_tester]` in a Shortcode block adds the interactive tester from the specimen page: font tabs, a text box, a size slider, a live preview and a grid of every glyph. `font="shapes"` or `font="objects"` chooses the tab that opens first. Its scripts load only on pages that use it, and it works with a keyboard and screen readers.

## Requirements

- WordPress 6.3 or later (the FAQ uses the Details block)
- Astra 4 (free version is enough)
- PHP 7.4 or later

## Installation

1. Install and activate **Astra** from Appearance › Themes › Add New.
2. Upload this theme: Appearance › Themes › Add New › Upload Theme, choose `dingthat-astra-child.zip`, then **Activate**. Astra must stay installed, because this theme builds on it.

## Setting up the site

Do these in order. Step 1 matters because the patterns read the addresses at the moment you insert them.

### 1. Addresses

Appearance › Customize › **Ding That**:

- **Download address:** where visitors get the fonts. The default is `https://github.com/warpcoil/ding-that/releases/latest`, which only works once you've published a release on GitHub with the zip attached. You can instead upload the zip to the Media Library and use its address.
- **Source code address:** defaults to `https://github.com/warpcoil/ding-that`.

Publish.

### 2. Astra settings (Appearance › Customize)

- **Global › Colors:** the theme already overrides Astra's nine global colours. To make the editor's colour picker show the same swatches, set the palette to:

  | Slot | Name | Light | Used for |
  | --- | --- | --- | --- |
  | 1 | Brand | `#5B3CC4` | Links, buttons, focus ring |
  | 2 | Brand hover | `#432A99` | Hover states |
  | 3 | Ink | `#17141F` | Headings |
  | 4 | Text | `#2E2A38` | Body text |
  | 5 | Surface | `#F5F3FA` | Bands and footer |
  | 6 | Paper | `#FFFFFF` | Page background |
  | 7 | Line | `#E1DCEB` | Borders |
  | 8 | Muted | `#4A4458` | Secondary text |
  | 9 | Tint | `#F0ECFD` | Notices |

- **Global › Typography:** leave body and heading fonts on the default ("Inherit" or system). The theme sets Atkinson Hyperlegible Next itself.
- **Global › Container:** container width **1200 px**.
- **Header Builder:**
  - **Logo:** upload `assets/logo.png` under Site Identity, at a width of about 160 px, with alternative text "Ding That". Upload `assets/site-icon.png` as the Site Icon.
  - **Menu:** a Primary menu with Fonts, Type tester, Help, FAQ and Open source.
  - **Button:** add the Button element with the text "Download the fonts", linking to the download address.
- **Footer Builder:** to match graphlines.com and pdfwire.com, use three menu columns: **Fonts** (Download the fonts, The fonts, Type tester, Help, FAQ), **Project** (Open source, GitHub) and **About this site** (Accessibility statement, Privacy notice). Set the copyright text, for example "© [current_year] Ding That".
- **Breadcrumb (optional):** turn on breadcrumbs for inner pages.

### 3. Home page

1. Pages › Add New, title **Ding That**.
2. In the **Astra Settings** sidebar of the page editor, set **Disable Title** (the hero has its own H1) and **Content Layout: Full Width / Stretched**, with no sidebar.
3. Open the block inserter › **Patterns** › **Ding That** › **Complete home page**.
4. Publish. Then Settings › Reading › **A static page**, and choose Ding That as the homepage.

To build a different landing page, insert the patterns one at a time instead.

### 4. Inner pages

For each file in `page-content/`, create a page with the title and slug from the table below. Then open ⋮ › **Code editor**, paste the file, and replace the placeholders:

- `{{DOWNLOAD_URL}}`: the download address
- `{{CONTACT_EMAIL}}`: your contact address
- `{{STATEMENT_DATE}}`: today's date
- `{{SITE_DATA: …}}` and `{{ENFORCEMENT_PROCEDURE: …}}`: the bracketed notes in the privacy notice and accessibility statement

Keep the default content layout, so the page title shows in the grey title band.

| File | Title | Slug |
| --- | --- | --- |
| `02-fonts.html` | The fonts | `fonts` |
| `03-help.html` | Help: using the Ding That fonts | `help` |
| `04-faq.html` | Frequently asked questions | `faq` |
| `05-accessibility.html` | Accessibility statement | `accessibility` |
| `06-privacy.html` | Privacy notice | `privacy` |
| `07-open-source.html` | Open source and licences | `open-source` |
| `08-type-tester.html` | Type tester | `type-tester` |

The character maps, box-drawing samples and glyph gallery are Custom HTML blocks, so the editor keeps the glyph markup exactly as written.

## Accessibility notes

- **Heading order:** the home page's hero heading is its only H1. On inner pages, Astra prints the page title as the H1, and content headings start at H2.
- **Glyphs:** a screen reader would read a glyph as the letter typed, so every glyph picture is `aria-hidden`, with its name in text beside it. The hero illustration is one image with a text description, and the box-drawing samples are labelled images.
- **Colour:** chips are decorative; the words next to them carry the meaning. Colour is never the only signal.
- **Specimen card stays white:** the hero illustration represents a printed sheet, so it stays white in dark mode.
- **Logo in dark mode:** the logo is turned light with a CSS filter, so no second image is needed.
- **Font loading:** the Ding That fonts use `font-display: block`, so visitors never see stray letters in place of pictures while the fonts load.

## What has been tested

The stylesheet, patterns and page content were checked in a browser preview, which loaded WordPress's block-library CSS with Astra-style header and footer markup:
- desktop, a 390 px phone width, and dark mode
- no sideways scrolling at either width
- the patterns and page files parse as valid blocks with WordPress's block parser
- the PHP files pass `php -l`
- text and button colours checked against WCAG AA contrast in both schemes

The theme has **not** yet been run on a live WordPress site with Astra installed. Please check it on a staging site first, especially the header and footer builder styling, which depends on Astra's exact markup.

## Licence

Theme code: GPL-2.0-or-later, as WordPress requires. Fonts: SIL Open Font License 1.1 (see `fonts/`).
