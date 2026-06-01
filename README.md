# Static Site Generator

A Python-based static site generator that converts Markdown files into a fully navigable HTML website. 

## How It Works

The generator reads `.md` files from the `content/` directory, converts them to HTML using a custom Markdown parser, wraps each page in `template.html`, and writes the output to the `docs/` directory (used by GitHub Pages for hosting).

Static assets — CSS, images, and any other files in `static/` — are copied directly to the output directory alongside the generated HTML.

## Project Structure

```
Static_Site_Generator/
├── content/          ← Your Markdown source files go here
│   └── index.md      ← Homepage content
├── static/           ← CSS, images, and other static assets
│   └── index.css     ← Site stylesheet
├── src/              ← Python source code (the generator engine)
│   └── main.py       ← Entry point for the generator
├── docs/             ← Generated HTML output (served by GitHub Pages)
├── template.html     ← HTML wrapper applied to every page
├── main.sh           ← Run locally: builds site + starts dev server
├── build.sh          ← Production build (used for GitHub Pages deploy)
└── test.sh           ← Run the test suite
```

## Quickstart

**Prerequisites:** Python 3 installed on your machine.

**Clone the repo:**
```bash
git clone https://github.com/scottw0173/Static_Site_Generator.git
cd Static_Site_Generator
```

**Run locally (builds site and starts a dev server):**
```bash
./main.sh
```
Then open your browser to [http://localhost:8888](http://localhost:8888).

**Run tests:**
```bash
./test.sh
```

## Adding Content

All of your site's pages live as Markdown files inside the `content/` directory. The directory structure you create there mirrors the URL structure of the generated site.

For example:
```
content/
├── index.md              → /index.html       (your homepage)
└── madness-reefing/
    └── index.md          → /madness-reefing/index.html
```

Each `.md` file should begin with an `# H1` heading, which becomes the page's `<title>` tag.

**Example `content/index.md`:**
```markdown
# Scott Warner

Welcome to my site. I'm an operations professional transitioning into tech...
```

## Adding Images

Place image files inside the `static/` directory (you can create subfolders to stay organized):

```
static/
├── index.css
└── images/
    ├── profile.jpg
    └── madness-reefing/
        ├── tank-1.jpg
        └── coral-1.jpg
```

Reference them in your Markdown like this:
```markdown
![A reef tank I built](/images/madness-reefing/tank-1.jpg)
```

## Customizing the Look

- **Layout/structure:** Edit `template.html`. The generator replaces `{{ Title }}` with the page's H1 heading and `{{ Content }}` with the converted HTML body.
- **Styles:** Edit `static/index.css`. Changes apply site-wide.

## Deploying to GitHub Pages

The `docs/` directory is what GitHub Pages serves. To deploy:

1. Run the production build:
   ```bash
   ./build.sh
   ```
2. Commit and push `docs/` to the `main` branch:
   ```bash
   git add docs/
   git commit -m "Rebuild site"
   git push
   ```
3. In your repository settings on GitHub, go to **Pages** and set the source to `main` branch, `/docs` folder.

Your site will be live at `https://scottw0173.github.io/Static_Site_Generator/`.

## Supported Markdown

The generator handles standard Markdown syntax including:

- Headings (`#`, `##`, `###`, etc.)
- Bold (`**text**`) and italic (`*text*`)
- Unordered and ordered lists
- Links (`[text](url)`)
- Images (`![alt](path)`)
- Inline code (`` `code` ``) and code blocks (` ``` `)
- Blockquotes (`> text`)
- Paragraphs and line breaks
