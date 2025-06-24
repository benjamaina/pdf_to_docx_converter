# 📄 PDF to DOCX Converter

A simple Python script that converts PDF files into editable Word (DOCX) documents using the `pdf2docx` library.

## 🔧 Features

- 📥 Converts any `.pdf` file to `.docx`
- 🔄 Retains formatting where possible
- 🖥️ Command-line based, no GUI required
- 💡 Lightweight and easy to use

## 🧰 Tech Stack

- Python 3.6+
- [`pdf2docx`](https://pypi.org/project/pdf2docx/)

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/benjamaina/pdf_to_docx_converter.git
cd pdf_to_docx_converter
Install the required library:

bash
Copy
Edit
pip install pdf2docx
Run the script:

bash
Copy
Edit
python converter.py
Follow the prompt:

text
Copy
Edit
Enter the path to the PDF file: sample.pdf
Enter the output Word file name (e.g., output.docx): sample.docx
Conversion complete!
📁 Project Structure
Copy
Edit
pdf_to_docx_converter/
└── converter.py
💡 Tips
Works best with text-based PDFs (not scanned images)

Avoid PDFs with complex layouts for best results

For scanned/image PDFs, consider integrating OCR (like pytesseract)

🚀 Future Ideas
Batch conversion of multiple PDFs

Add GUI with Tkinter or PyQt

Add drag-and-drop file support
