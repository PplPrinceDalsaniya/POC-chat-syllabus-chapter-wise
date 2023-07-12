from llama_index import download_loader, VectorStoreIndex
from database import availableDatabase
from pathlib import Path
from llama_hub.file.unstructured.base import UnstructuredReader


def create_index_for_this_file(filePath, indexName):
  loader = UnstructuredReader()
  documents = loader.load_data(file=Path(filePath))
  index = VectorStoreIndex.from_documents(documents)
  index.storage_context.persist(f"./vectorIndexDataStore/individualIndices/{indexName}")


def create_index_for_each_entry_in_db():
  for entry in availableDatabase:
    create_index_for_this_file(entry['path'], entry['id'])


def create_combined_index_for_directory(directoryPath, indexName):
  SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
  loader = SimpleDirectoryReader(directoryPath)
  documents = loader.load_data()
  index = VectorStoreIndex.from_documents(documents)
  index.storage_context.persist(f'./vectorIndexDataStore/{indexName}')


def main():
  create_combined_index_for_directory('./Docs', 'combinedIndex')
  create_index_for_each_entry_in_db()


if __name__ == '__main__':
  main()
