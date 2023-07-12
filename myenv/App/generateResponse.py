from llama_index import StorageContext, load_index_from_storage

def generate_response_from_common_index(prompt):
  storage_context = StorageContext.from_defaults(persist_dir="./vectorIndexDataStore/combinedIndex")
  index = load_index_from_storage(storage_context)
  print('Index : ', index)
  query_engin = index.as_query_engine() 
  question = prompt
  print('Question : ', question)
  response = query_engin.query(question)
  return str(response)
