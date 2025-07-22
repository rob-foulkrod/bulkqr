from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from typing import List, Tuple

def generate_html(urls_and_images: List[Tuple[str, str]], template_dir: str, output_html: str):
    """
    Generate an HTML file displaying URLs and their QR code images.
    urls_and_images: List of (url, image_path) tuples.
    template_dir: Directory containing the HTML template.
    output_html: Path to save the generated HTML file.
    """
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('qr_page.html')
    html_content = template.render(items=urls_and_images)
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
