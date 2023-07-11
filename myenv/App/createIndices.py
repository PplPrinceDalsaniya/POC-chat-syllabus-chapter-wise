from llama_index import download_loader, VectorStoreIndex

def createIndexForAllFilesTogather():
  SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
  loader = SimpleDirectoryReader('./Docs')
  documents = loader.load_data()
  index = VectorStoreIndex.from_documents(documents)
  index.storage_context.persist("./combinedVectorIndex")
