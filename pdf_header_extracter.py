# $ pip3 install PyPDF2

import PyPDF2
import sys

def extract_headers(pdf_path, output_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        headers = []
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            content = page.extract_text()

            # Split lines and filter out empty lines
            lines = [line.strip() for line in content.split('\n') if line.strip()]
            
            # Filter lines that look like headers (you may need to adjust this)
            header_lines = [line for line in lines if line.isupper() or line.istitle()]

            # Append headers to the list
            headers.extend(header_lines)

    # Write headers to a text file
    with open(output_path, 'w') as output_file:
        for header in headers:
            output_file.write(header + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <pdf_path> <output_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_path = sys.argv[2]

    extract_headers(pdf_path, output_path)


    # python3 script_name.py path/to/your/file.pdf output.txt