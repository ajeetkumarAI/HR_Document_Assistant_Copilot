from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=300,
        separators=["\n\n", "\n", "(?<=. )", " ", ""]
    )

    chunks = text_splitter.split_documents(docs)
    return chunks