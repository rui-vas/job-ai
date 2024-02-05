from langchain_community.document_loaders import UnstructuredPDFLoader

loader = UnstructuredPDFLoader("~/Downloads/CV_Rui-Vas_2024.pdf")

data = loader.load()

print(data)