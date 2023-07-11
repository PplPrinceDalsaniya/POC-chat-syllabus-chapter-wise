import os
import streamlit as st
from database import availableDatabase, getParams, get_params_from_labels
from createIndices import createIndexForAllFilesTogather, createIndexForEachFile
from generateResponse import generate_response_from_common_index
from sidebar import sidebar


import openai
key = '<KEY>' # UPDATE THE KEY BEFORE RUNNING
openai.api_key = key
os.environ['OPENAI_API_KEY'] = key


st.set_page_config(page_title="POC GPT knowledgebase", page_icon="📖", layout="wide")
st.header("📖 Ask your Books")


def main():
  sidebar()

  # This function will create a combined index of all the syllabus available in docs directory.
  # This is meant to be ran for only one time.
  # createIndexForAllFilesTogather()

  # This function will create index for each file available in docs directory.
  # This is meant to be ran for only one time.
  # createIndexForEachFile()
  
  print('Answer : ', generate_response_from_common_index("Acids change the blue litmus paper to which colour?"))
  print('Answer : ', generate_response_from_common_index("How do they taste?"))


if __name__ == '__main__':
  main()
