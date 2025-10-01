# Web CV - Taewon Song

This directory contains the web version of the CV, automatically generated from LaTeX source files.

## Features

- 🎨 **Modern, Responsive Design**: Looks great on all devices
- 🌓 **Dark Mode**: Toggle between light and dark themes
- 🖨️ **Print-Optimized**: Beautiful printed output
- ⚡ **Fast Loading**: Minimal dependencies, pure vanilla JavaScript
- 📱 **Mobile-Friendly**: Responsive layout adapts to any screen size
- ♿ **Accessible**: ARIA labels and semantic HTML

## Structure

```
web/
├── index.html          # Main HTML template
├── css/
│   └── style.css      # All styling (with dark mode & print styles)
├── js/
│   └── main.js        # JavaScript for dynamic content loading
├── data/
│   └── cv_data.json   # Structured CV data (auto-generated from TeX)
└── README.md          # This file
```

## Local Development

### Option 1: Python HTTP Server
```bash
cd web
python3 -m http.server 8000
```
Then open http://localhost:8000

### Option 2: Node.js HTTP Server
```bash
cd web
npx http-server -p 8000
```

### Option 3: PHP Built-in Server
```bash
cd web
php -S localhost:8000
```

## Updating Content

The web CV is automatically generated from the LaTeX source files. To update:

1. **Edit TeX files** in the repository root (e.g., `bio.tex`, `employment.tex`)
2. **Run the parser** to regenerate JSON data:
   ```bash
   python3 scripts/parse_tex_to_json.py
   ```
3. **Refresh** the web page to see changes

## Technologies Used

- **HTML5**: Semantic markup
- **CSS3**: Modern styling with CSS Variables, Grid, Flexbox
- **JavaScript (ES6+)**: Vanilla JS, no frameworks
- **Font Awesome**: Icons
- **Google Fonts**: Inter (sans-serif) and Merriweather (serif)

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Keyboard Shortcuts

- `Ctrl/Cmd + P`: Print CV
- `Ctrl/Cmd + D`: Toggle dark mode

## Customization

### Colors
Edit CSS variables in `css/style.css`:
```css
:root {
    --accent-color: #0066cc;  /* Primary accent color */
    --bg-primary: #ffffff;     /* Background color */
    /* ... more variables ... */
}
```

### Fonts
Change font imports in `index.html` and update CSS variables:
```css
--font-sans: 'Inter', sans-serif;
--font-serif: 'Merriweather', serif;
```

## Deployment

This site is designed to be deployed to GitHub Pages. See the GitHub Actions workflow in `.github/workflows/` for automated deployment.

## License

This template is part of the curriculum_vitae repository.
