
# Bulk QR Code Generator

Generate beautiful QR code galleries from a list of URLs—locally, with no server required! This project provides both a Python (local script) and a JavaScript (client-side) implementation.

---

## 🚀 Quick Start

**Python:**
1. Install Python 3.7+ and run:
   ```bash
   pip install -r requirements.txt
   python main.py
   ```
2. Open `output/qr_codes.html` in your browser.

**JavaScript:**
1. Open `static/qr_gallery_client.html` in your browser.
2. Paste URLs and click "Generate QR Codes".

---

## ✨ Features
- Bulk QR code generation from a list of URLs
- Modern, responsive, and interactive gallery UI
- Copy and download QR codes (Python version)
- Two approaches: Python local script or pure client-side JavaScript

---

## Python Version

### Requirements
- Python 3.7+
- Install dependencies with:
  ```bash
  pip install -r requirements.txt
  ```
  The main dependencies are:
  - `qrcode[pil]`
  - `Pillow`
  - `Jinja2`


### Usage
1. Add your URLs to `urls.txt` (one per line).
2. Run:
   ```bash
   python main.py
   ```
3. Open `output/qr_codes.html` in your browser. QR images are in the same folder.

### How it works
- Reads URLs from a text file
- Generates QR code PNGs for each URL
- Renders a beautiful HTML gallery using a Jinja2 template
- All output is saved to the `output/` directory

---

## JavaScript (Client-Side) Version

### Requirements
- Any modern web browser (Chrome, Edge, Firefox, Safari)
- No installation or server required


### Usage
1. Open `static/qr_gallery_client.html` in your browser
2. Paste your URLs (one per line) into the textarea
3. Click "Generate QR Codes"
4. The gallery and QR codes are generated instantly in your browser

### How it works
- Uses [qrcodejs](https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js) to generate QR codes in the browser
- No data is sent to any server; everything runs locally
- The UI and gallery are styled to match the Python version

---

bulkqr/
├── src/                      # Python source files
├── templates/                # Jinja2 HTML template (Python version)
├── static/                   # CSS and client-side HTML/JS
├── output/                   # Generated files (Python version, gitignored)
├── main.py                   # Python entry point
├── requirements.txt          # Python dependencies
├── urls.txt                  # Example URL list
└── README.md                 # This file

## 📁 Project Structure
```
bulkqr/
├── src/                      # Python source files
├── templates/                # Jinja2 HTML template (Python version)
├── static/                   # CSS and client-side HTML/JS
├── output/                   # Generated files (Python version, gitignored)
├── main.py                   # Python entry point
├── requirements.txt          # Python dependencies
├── urls.txt                  # Example URL list
└── README.md                 # This file
```

---


## 🤔 Which Version Should I Use?

| Use Case                        | Python Local Script | JavaScript Client-Side |
|----------------------------------|:------------------:|:---------------------:|
| Generate and save QR images      |         ✅         |          ❌           |
| Batch/automate large lists       |         ✅         |          ❌           |
| No install, instant use          |         ❌         |          ✅           |
| Share as a single HTML file      |         ❌         |          ✅           |
| Custom HTML output               |         ✅         |          ❌           |
| All processing local             |         ✅         |          ✅           |


---


## 📝 Example URLs
```
https://aka.ms/cie01
https://aka.ms/cie01reg
https://aka.ms/cie02
https://aka.ms/cie02reg
...
```

---

## 🖼️ Screenshots
<img src="static/demo_screenshot.png" alt="QR Gallery Demo" width="700"/>

---

## 🛠️ Customization
- **Styling:** Edit `static/styles.css` for colors, layout, and fonts
- **Python:** Change QR code settings in `src/qr_generator.py` or HTML in `templates/qr_page.html`
- **JavaScript:** Adjust QR code size or add features in `static/qr_gallery_client.html`

---

## ⚠️ Known Issues
- Very long URLs may need QR code size adjustments
- Python version requires local Python install

---

## 📄 License
MIT

## 🤝 Contributing
Pull requests and suggestions welcome!

---

## License
MIT
