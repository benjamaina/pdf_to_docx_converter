from pdf2docx import Converter
from tkinter import filedialog, messagebox
import tkinter as tk

def convert_pdf_to_docx():
    input_pdf_path = pdf_path_var.get()
    output_docx_path = docx_path_var.get()
    
    if not input_pdf_path or not output_docx_path:
        messagebox.showerror("Error", "Please select both input and output paths.")
        return
    try:
        converter = Converter(input_pdf_path)
        converter.convert(output_docx_path)
        converter.close()
        messagebox.showinfo(f"Conversion of {input_pdf_path} to {output_docx_path} successful.")
        return True

    except Exception as e:
        messagebox.showinfo(f"Error occurred while converting {input_pdf_path} to {output_docx_path}: {str(e)}")
        return False

def select_pdf():
    pdf_path = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF Files", "*.pdf")])
    pdf_path_var.set(pdf_path)


def select_output():
    docx_path = filedialog.asksaveasfilename(title="Save as DOCX File", filetypes=[("DOCX Files", "*.docx")])
    docx_path_var.set(docx_path)

root = tk.Tk()
root.title("PDF to DOCX converter")
root.geometry("400x250")
root.resizable(False,False)

pdf_path_var = tk.StringVar()
docx_path_var = tk.StringVar()

tk.Label(root, text="select PDF File:").pack(pady=5)
tk.Entry(root, textvariable=pdf_path_var, width=40, state="readonly").pack(pady=2)
tk.Button(root, text="Browse", command=select_pdf).pack(pady=2)


tk.Label(root, text="select DOCX File:").pack(pady=5)
tk.Entry(root, textvariable=docx_path_var, width=40, state="readonly").pack(pady=2)
tk.Button(root, text="Browse", command=select_output).pack(pady=2)

tk.Button(root, text="Convert", command=convert_pdf_to_docx, bg="green", fg="white").pack(pady=20)

root.mainloop()