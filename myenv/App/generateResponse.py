from llama_index import StorageContext, load_index_from_storage
from langchain import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.agents import initialize_agent
from database import get_target_params_for_this_values
from llama_index.tools.query_engine import QueryEngineTool
from llama_index.query_engine.router_query_engine import RouterQueryEngine
from llama_index.selectors.llm_selectors import LLMSingleSelector
from llama_index.langchain_helpers.agents import (
    LlamaToolkit,
    create_llama_chat_agent,
    IndexToolConfig,
)

global_agent_chain = None


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
  answer = global_agent_chain.run(input=prompt)
  print('Answer in routing buffermemory : ', answer)
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

  index_configs = []
  for subject, query_engine, label in zip(subjects, vectorQueryEngines, labels):
    tool_config = IndexToolConfig(
        query_engine=query_engine,
        name=f"{label}",
        description=f"Useful for when you want to answer queries about subject {subject} and ch(means chapter) {label}.",
        tool_kwargs={"return_sources": True},
    )
    index_configs.append(tool_config)

  toolkit = LlamaToolkit(index_configs=index_configs)
  memory = ConversationBufferMemory(memory_key="chat_history")
  llm = OpenAI(temperature=0)
  agent_chain = create_llama_chat_agent(toolkit, llm, memory=memory, verbose=True)

  global global_agent_chain
  global_agent_chain = agent_chain
