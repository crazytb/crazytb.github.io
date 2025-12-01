#!/usr/bin/env python3
import subprocess
import sys

try:
    # Get the last git commit date
    result = subprocess.run(
        ['git', 'log', '-1', '--format=%cd', '--date=format:%Y-%m-%d'],
        capture_output=True,
        text=True,
        check=True
    )
    date_str = result.stdout.strip()

    # Write to a LaTeX file
    with open('git_date.tex', 'w') as f:
        f.write(date_str)

    print(f"Updated date: {date_str}")
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    # Fallback to current date
    from datetime import date
    fallback_date = date.today().strftime('%Y-%m-%d')
    with open('git_date.tex', 'w') as f:
        f.write(fallback_date)
    print(f"Using fallback date: {fallback_date}")
