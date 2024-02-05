from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("/Users/ruivasconcelos/Downloads/CV_Rui-Vas_2024.pdf")
pages = loader.load_and_split()
print(pages[0].page_content)

