from pathlib import Path
from src.qr_generator import generate_qr_code
from src.url_processor import read_urls_from_file
from src.html_generator import generate_html
import os

def main():
    # Input file with URLs
    url_file = 'urls.txt'  # You can change this as needed
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)

    # Read URLs
    urls = read_urls_from_file(url_file)
    urls_and_images = []
    for idx, url in enumerate(urls):
        image_name = f'qr_{idx+1}.png'
        image_path = output_dir / image_name
        generate_qr_code(url, image_path)
        urls_and_images.append((url, image_name))

    # Generate HTML
    generate_html(
        urls_and_images,
        template_dir='templates',
        output_html='output/qr_codes.html'
    )
    print('QR codes and HTML page generated in the output/ directory.')

if __name__ == '__main__':
    main()
