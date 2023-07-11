from llama_index import download_loader, VectorStoreIndex
from database import availableDatabase, get_params_from_labels, getParams
from pathlib import Path
from llama_hub.file.unstructured.base import UnstructuredReader


def createIndexForAllFilesTogather():
  SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
  loader = SimpleDirectoryReader('./Docs')
  documents = loader.load_data()
  index = VectorStoreIndex.from_documents(documents)
  index.storage_context.persist("./combinedVectorIndex")


def createIndexForFile(labels):
  chapter_ids = get_params_from_labels(labels, availableDatabase, 'id')
  for id in chapter_ids:
    loader = UnstructuredReader()
    documents = loader.load_data(file=Path(f'./Docs/{id}.pdf'))
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(f"./vectorIndexDataStore/{id}_index")


def createIndexForEachFile():
  for subject in availableDatabase:
    createIndexForFile(getParams(availableDatabase[subject], 'label'))


def main():
  createIndexForEachFile()


if __name__ == '__main__':
  main()
