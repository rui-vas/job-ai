from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("~/Downloads/CV_Rui-Vas_2024.pdf")
pages = loader.load_and_split()

pages[0]