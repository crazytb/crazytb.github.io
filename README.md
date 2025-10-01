# Curriculum Vitae - Dr. Taewon Song

LaTeX-based curriculum vitae with automatic web deployment.

## 🌟 Features

- 📄 **PDF Generation**: Professional LaTeX-based CV
- 🌐 **Web Version**: Modern, responsive web CV
- 🔄 **Automatic Sync**: Web CV automatically generated from LaTeX source
- 🌓 **Dark Mode**: Toggle between light and dark themes
- 🖨️ **Print-Optimized**: Both PDF and web versions are print-friendly
- 🚀 **Auto-Deploy**: GitHub Actions automatically builds and deploys

## 📁 Project Structure

```
curriculum_vitae/
├── cv-taewon.tex           # Main LaTeX file
├── settings.sty            # LaTeX style definitions
├── *.tex                   # Content sections (bio, employment, etc.)
├── own-bib.bib            # Bibliography
├── scripts/
│   └── parse_tex_to_json.py   # TeX to JSON converter
├── web/                    # Web CV (auto-generated)
│   ├── index.html
│   ├── css/style.css
│   ├── js/main.js
│   └── data/cv_data.json
└── .github/workflows/      # CI/CD automation
```

## 🚀 Quick Start

### Build PDF Locally

```bash
# Using pdflatex
pdflatex cv-taewon.tex

# Or using latexmk (recommended)
latexmk -pdf cv-taewon.tex
```

### Generate Web Version

```bash
# Parse TeX files to JSON
python3 scripts/parse_tex_to_json.py

# Start local web server
cd web
python3 -m http.server 8000

# Open http://localhost:8000 in your browser
```

## 📝 Updating Content

### 1. Edit TeX Files

The CV is modular - edit the appropriate section file:

- `bio.tex` - Biography/summary
- `employment.tex` - Work experience
- `education.tex` - Academic background
- `skills.tex` - Skills and languages
- `projects.tex` - Research projects
- `publications.tex` + `own-bib.bib` - Publications

### 2. Build and Test

```bash
# Build PDF
pdflatex cv-taewon.tex

# Generate web version
python3 scripts/parse_tex_to_json.py

# Test locally
cd web && python3 -m http.server 8000
```

### 3. Deploy

Simply push to GitHub - the workflow will automatically:
1. Build the PDF from LaTeX
2. Parse TeX files to JSON
3. Deploy web version to GitHub Pages

```bash
git add .
git commit -m "Update CV content"
git push origin main
```

## 🌐 Web CV

The web version features:

- **Responsive Design**: Works on all devices
- **Dark Mode**: System preference detection + manual toggle
- **Modern UI**: Clean, professional appearance
- **Fast Loading**: No heavy frameworks, pure vanilla JS
- **Accessible**: WCAG compliant
- **Print Support**: Optimized print styles

### Live Demo

Once deployed, your CV will be available at:
```
https://<username>.github.io/curriculum_vitae/
```

## 🛠️ Development

### Prerequisites

- **For PDF**: LaTeX distribution (TeX Live, MiKTeX, etc.)
- **For Web**: Python 3.x
- **For Deployment**: Git + GitHub account

### LaTeX Packages Used

- `curve` - CV document class
- `kotex` - Korean language support
- `biblatex` - Bibliography management
- `fontawesome5` - Icons
- `hyperref` - Hyperlinks

### Web Technologies

- **HTML5**: Semantic markup
- **CSS3**: Modern styling with variables, grid, flexbox
- **JavaScript (ES6+)**: Vanilla JS, no dependencies
- **Font Awesome**: Icons
- **Google Fonts**: Inter & Merriweather

## ⚙️ Configuration

### GitHub Pages Setup

1. Go to repository **Settings** → **Pages**
2. Source: **GitHub Actions**
3. The workflow will automatically deploy on push to `main`

### Customizing Colors

Edit `web/css/style.css`:

```css
:root {
    --accent-color: #0066cc;     /* Your brand color */
    --bg-primary: #ffffff;        /* Background */
    --text-primary: #212529;      /* Text color */
}
```

### Customizing Fonts

Edit the Google Fonts import in `web/index.html` and update CSS variables.

## 📜 Build Commands

### LaTeX

```bash
# Quick build
pdflatex cv-taewon.tex

# Full build with bibliography
pdflatex cv-taewon.tex
biber cv-taewon
pdflatex cv-taewon.tex
pdflatex cv-taewon.tex

# Using latexmk (automatic)
latexmk -pdf cv-taewon.tex

# Clean auxiliary files
latexmk -c

# Clean all (including PDF)
latexmk -C
```

### Web

```bash
# Parse TeX to JSON
python3 scripts/parse_tex_to_json.py

# Local development server
cd web && python3 -m http.server 8000

# Alternative: using Node.js
npx http-server web -p 8000
```

## 🤝 Contributing

This is a personal CV repository, but feel free to:

- Report bugs
- Suggest improvements
- Fork for your own CV
- Submit pull requests

## 📄 License

This CV template is open source. Feel free to use it for your own CV.

## 🙏 Acknowledgments

- Original LaTeX template by [LianTze Lim](https://github.com/liantze)
- Icons by [Font Awesome](https://fontawesome.com/)
- Fonts by [Google Fonts](https://fonts.google.com/)

## 📧 Contact

**Dr. Taewon Song**
- Email: twsong@sch.ac.kr
- GitHub: [@crazytb](https://github.com/crazytb)
- Website: https://sites.google.com/view/ainolab/

---

**Last updated**: October 2025
