# $ pip3 install PyPDF2
# can you make that the md follows the header syntax of the original pdf: like when is header is # in md, when is a subheader then put ## or ### 

import fitz  # PyMuPDF
import sys

def extract_headers(page, depth=0):
    headers = []

    try:
        # Extract text from the page
        content = page.get_text("text")

        # Split lines and filter out empty lines
        lines = [line.strip() for line in content.split('\n') if line.strip()]

        # Filter lines that look like headers (you may need to adjust this)
        header_lines = [line for line in lines if line.isupper() or line.istitle()]

        # Append headers to the list
        headers.extend([(line, depth) for line in header_lines])

        # Extract headers from linked annotations
        for link in page.get_links():
            subheaders = extract_headers(link, depth + 1)
            headers.extend(subheaders)

    except AttributeError:
        # Handle the case when 'page' is not a valid page object (e.g., link annotation)
        pass

    return headers
def write_headers_to_file(headers, output_path):
    with open(output_path, 'w') as output_file:
        for header, depth in headers:
            # Use indentation based on the depth of the header
            output_file.write("  " * depth + header + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <pdf_path> <output_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_path = sys.argv[2]

    pdf_document = fitz.open(pdf_path)
    
    all_headers = []
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        headers = extract_headers(page)
        all_headers.extend(headers)

    write_headers_to_file(all_headers, output_path)
# usage: python3 script_name.py path/to/your/file.pdf output.txt