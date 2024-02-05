from pypdf import PdfReader

reader = PdfReader("/Users/ruivasconcelos/Downloads/CV_Rui-Vas_2024.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(number_of_pages)
print(text)