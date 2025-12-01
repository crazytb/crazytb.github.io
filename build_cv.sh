#!/bin/bash
# CV Build Script
# Automatically updates git date and builds the CV

echo "=== Building CV ==="

# Step 1: Update git date
echo "Step 1: Updating git commit date..."
python3 update_date.py

if [ $? -ne 0 ]; then
    echo "Warning: Could not get git date, using fallback"
fi

# Step 2: Build PDF
echo "Step 2: Building PDF with latexmk..."
latexmk -pdf cv-taewon.tex

if [ $? -eq 0 ]; then
    echo "=== Build successful! ==="
    echo "Output: cv-taewon.pdf"
    ls -lh cv-taewon.pdf
else
    echo "=== Build failed! ==="
    exit 1
fi
