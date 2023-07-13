from llama_index import StorageContext, load_index_from_storage
from database import get_target_params_for_this_values
from llama_index.tools.query_engine import QueryEngineTool
from llama_index.query_engine.router_query_engine import RouterQueryEngine
from llama_index.selectors.llm_selectors import LLMSingleSelector


specific_search_engine = None


def generate_response_from_common_index(prompt):
  storage_context = StorageContext.from_defaults(persist_dir="./vectorIndexDataStore/combinedIndex")
  index = load_index_from_storage(storage_context)
  query_engin = index.as_query_engine() 
  question = prompt
  print('Question : ', question)
  response = query_engin.query(question)
  print('Answer in common : ', response)
  return str(response)


def generate_response_from_given_query_engine(prompt):
  answer = str(specific_search_engine.query(prompt))
  print('Answer in routing : ', answer)
  return answer


def load_search_engine(labels):
  ids = get_target_params_for_this_values('id', 'label', labels)
  subjects = get_target_params_for_this_values('subject', 'label', labels)
  vectorIndices = []

  for id in ids:
    storageContext = StorageContext.from_defaults(persist_dir=f"./vectorIndexDataStore/individualIndices/{id}")
    index = load_index_from_storage(storage_context=storageContext)
    print(f'Index Loaded for {id}')
    vectorIndices.append(index)

  vectorQueryEngines = [index.as_query_engine() for index in vectorIndices]

  vector_tools = []
  for subject, query_engine, label in zip(subjects, vectorQueryEngines, labels):
    vector_tool = QueryEngineTool.from_defaults(
        query_engine=query_engine,
        description=f"Useful for when you want to answer queries about subject {subject} and ch(means chapter) {label}.",
    )
    vector_tools.append(vector_tool)

  query_engine = RouterQueryEngine(
    selector=LLMSingleSelector.from_defaults(),
    query_engine_tools=(vector_tools)
  )

  global specific_search_engine
  specific_search_engine = query_engine
