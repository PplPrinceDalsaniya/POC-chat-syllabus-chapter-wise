import os
import streamlit as st
from database import availableDatabase, getParams, get_info_from_param
from createIndices import createIndexForAllFilesTogather, createIndexForEachFile
from generateResponse import generate_response_from_common_index, create_search_engine_from_selected_files, create_search_graph_for_selected_files


import openai
key = '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'
openai.api_key = key
os.environ['OPENAI_API_KEY'] = key


st.set_page_config(page_title="POC GPT knowledgebase", page_icon="📖", layout="wide")
st.header("📖 Ask your Books")


search_engine = None


# Initialise session state variables
def initiateSessionStorage():
  if 'generated' not in st.session_state:
    st.session_state['generated'] = []
  if 'past' not in st.session_state:
    st.session_state['past'] = []
  if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
  if "currentlySelectedLabels" not in st.session_state:
    st.session_state.currentlySelectedLabels = []
  if "currentlySelectedIds" not in st.session_state:
    st.session_state.currentlySelectedIds = []


# Sidebar.
def sidebar():
  with st.sidebar:
    st.markdown(
      "# How to use\n"
      "1. Select the books you want to ask the questions.\n"
      "2. Hit `Load` to load those books into chatbot.\n"
      "3. Ask questions about the books you selected."
    )
    st.divider()
    st.title('Step 1 - Select books : ')

    
    ScienceExpander = st.expander("Class 10 Science")
    scienceChapters = ScienceExpander.multiselect('Select the chapters that you want to ask :',
      getParams(availableDatabase['science'], 'label'), key='scienceChapters')
    
    SocialScienceExpander = st.expander("Class 10 Social-Science")
    socialScienceChapters = SocialScienceExpander.multiselect('Select the chapters that you want to ask :',
      getParams(availableDatabase['socialScience'], 'label'), key='socialScienceChapters')
    
    st.divider()

    if st.button('Create Indices'):
      st.session_state.currentlySelectedLabels = scienceChapters + socialScienceChapters
      st.session_state.currentlySelectedIds = get_info_from_param(st.session_state.currentlySelectedLabels, availableDatabase, 'id')
      st.write('Selected chapters keys : ', st.session_state.currentlySelectedIds)
      global search_engine
      # search_engine = create_search_engine_from_selected_files(st.session_state.currentlySelectedIds)
      search_engine = create_search_graph_for_selected_files(st.session_state.currentlySelectedIds)


def main():

  initiateSessionStorage()

  sidebar()

  # This function will create a combined index of all the syllabus available in docs directory.
  # This is meant to be ran for only one time.
  # createIndexForAllFilesTogather()

  # This function will create index for each file available in docs directory.
  # This is meant to be ran for only one time.
  # createIndexForEachFile()
  
  global search_engine
  if (search_engine):
    print('Answer : ', search_engine.query("India is which type of country?"))
    print('Answer : ', search_engine.query("List out 2 metals and 2 non-metals."))


if __name__ == '__main__':
  main()
