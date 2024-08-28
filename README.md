# Static Site Generator

## Overview

Converts Markdown files into HTML pages, using python. Is able to handle multiple markdown files, and link between pages.
 
## Installation

1. Clone the repository:
   ```
   git clone https://github.com/LucasAMachado/static-site-generator.git
   cd static-site-generator
   ```

2. Set up a virtual environment (optional):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

## Usage

### Generating the Site

Run the main script to generate your static site:

```
./main.sh
```

This script does the following:
1. Executes `python src/main.py` to convert Markdown files to HTML.
2. Starts a local server to serve the generated files.

### Adding Content

1. Place your Markdown files in the `content/` directory.
2. Run the generation script again to update the site.

### Customization

- Modify `template.html` to change the overall structure of the generated pages.
- Edit `static/index.css` to customize the site's styling.

## Running Tests

To ensure everything is working correctly, run the tests:

```
./test.sh
```

This command executes all tests located in the `src/tests` directory.