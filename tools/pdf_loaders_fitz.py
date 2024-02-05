import fitz  # PyMuPDF

# Open the PDF file
with fitz.open("~/Downloads/CV_Rui-Vas_2024.pdf") as doc:
    text = ""
    for page in doc:
        # Extract text from each page
        text += page.get_text()
