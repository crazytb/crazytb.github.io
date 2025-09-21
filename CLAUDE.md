# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview
This is a LaTeX-based curriculum vitae (CV) repository for Dr. Taewon Song. The CV is built using a custom LaTeX template with modular sections for academic/professional content.

## Build Commands
- **Compile CV**: `pdflatex cv-taewon.tex` or `latexmk -pdf cv-taewon.tex`
- **Clean build files**: `latexmk -c` (removes auxiliary files but keeps PDF)
- **Full clean**: `latexmk -C` (removes all generated files including PDF)

## Architecture
The CV is structured as a modular LaTeX document:

- **Main file**: `cv-taewon.tex` - Entry point that includes all sections and defines document structure
- **Style file**: `settings.sty` - Custom LaTeX package containing all formatting, colors, and layout definitions
- **Content sections** (separate .tex files):
  - `bio.tex` - Biography/summary section
  - `employment.tex` - Employment history
  - `education.tex` - Educational background
  - `skills.tex` - Technical skills
  - `projects.tex` - Projects and achievements
  - `misc.tex` - Miscellaneous information
  - `referee.tex` / `referee-full.tex` - References
- **Publications**: `publications.tex` + `own-bib.bib` - Bibliography managed with biblatex
- **Assets**: `photo.jpg` - Profile photo (conditional display)

## Key Features
- Uses the `curve` document class for CV formatting
- Korean language support via `kotex` package
- Conditional photo display controlled by `fullonly` environment
- Custom color scheme (SwishLineColour, MarkerColour) defined in settings.sty
- Bibliography with IEEE style, automatic name bolding for author
- FontAwesome icons for contact information
- Modular content structure for easy maintenance

## Content Management
Each section is a separate .tex file that can be edited independently. The main file uses `\makerubric{}` to include most sections and `\input{}` for custom formatted sections like publications and references.

To add/modify content:
1. Edit the appropriate section file (bio.tex, employment.tex, etc.)
2. For publications, update `own-bib.bib` and ensure name variants are listed in `\mynames{}`
3. Rebuild with `pdflatex cv-taewon.tex`