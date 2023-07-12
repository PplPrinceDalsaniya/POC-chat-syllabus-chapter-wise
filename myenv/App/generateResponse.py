import os
from llama_index import ComposableGraph, GPTTreeIndex, StorageContext, load_index_from_storage
import streamlit as st
from database import availableDatabase, get_info_from_param
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.query_engine import SubQuestionQueryEngine

def generate_response_from_common_index(prompt):
  storage_context = StorageContext.from_defaults(persist_dir="./combinedVectorIndex")
  index = load_index_from_storage(storage_context)
  print('Index : ', index)
  query_engin = index.as_query_engine()
  question = prompt
  print('Question : ', question)
  response = query_engin.query(question)
  return str(response)

def create_search_engine_from_selected_files(ids):
  availableIndices = os.listdir('./vectorIndexDataStore')
  descriptions = get_info_from_param(ids, availableDatabase, 'desc', 'id')
  query_engine_tools = []

  for i in range(len(ids)):
    # In this else case we can add code to create a new index because this id don't have its index.
    if f'{ids[i]}_index' in availableIndices:
      storage_context = StorageContext.from_defaults(persist_dir=f"./vectorIndexDataStore/{ids[i]}_index")
      index = load_index_from_storage(storage_context)
      query_engine = index.as_query_engine(similarity_top_k=2)
      tool = QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(name=ids[i], description=descriptions[i])
      )
      query_engine_tools.append(tool)
  search_engine = SubQuestionQueryEngine.from_defaults(query_engine_tools=query_engine_tools)
  return search_engine


def create_search_graph_for_selected_files(ids):
  availableIndices = os.listdir('./vectorIndexDataStore')
  descriptions = get_info_from_param(ids, availableDatabase, 'desc', 'id')
  indices = []
  index_summaries = []
  for i in range(len(ids)):
    if f'{ids[i]}_index' in availableIndices:
      storage_context = StorageContext.from_defaults(persist_dir=f"./vectorIndexDataStore/{ids[i]}_index")
      index = load_index_from_storage(storage_context)
      indices.append(index)
      index_summaries.append(descriptions[i])
  graph = ComposableGraph.from_indices(GPTTreeIndex, indices, index_summaries=index_summaries)
  # set query config
  query_configs = [
      {
          "index_struct_type": "simple_dict",
          "query_mode": "default",
          "query_kwargs": {
              "similarity_top_k": 3,
              "response_mode": "tree_summarize"
          }
      },
  ]
  return graph.as_query_engine()


# def main():
#   arr = ["socialscience_ch_3", "science_ch_13", "science_ch_3"]
#   create_search_engine_from_selected_files(arr)


# if __name__ == '__main__':
#   main()
