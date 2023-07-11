import os
import streamlit as st
from database import availableDatabase, getParams, get_params_from_labels
from createIndices import createIndexForAllFilesTogather, createIndexForEachFile
from generateResponse import generate_response_from_common_index


import openai
key = '<KEY>' # UPDATE THE KEY BEFORE RUNNING
openai.api_key = key
os.environ['OPENAI_API_KEY'] = key


st.set_page_config(page_title="POC GPT knowledgebase", page_icon="📖", layout="wide")
st.header("📖 Ask your Books")


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

    if "currentlySelectedLabels" not in st.session_state:
      st.session_state.currentlySelectedLabels = []
    if "currentlySelectedIds" not in st.session_state:
      st.session_state.currentlySelectedIds = []
    
    ScienceExpander = st.expander("Class 10 Science")
    scienceChapters = ScienceExpander.multiselect('Select the chapters that you want to ask :',
      getParams(availableDatabase['science'], 'label'), key='scienceChapters')
    
    SocialScienceExpander = st.expander("Class 10 Social-Science")
    socialScienceChapters = SocialScienceExpander.multiselect('Select the chapters that you want to ask :',
      getParams(availableDatabase['socialScience'], 'label'), key='socialScienceChapters')
    
    st.divider()

    if st.button('Create Indices'):
      st.session_state.currentlySelectedLabels = scienceChapters + socialScienceChapters
      st.session_state.currentlySelectedIds = get_params_from_labels(st.session_state.currentlySelectedLabels, availableDatabase, 'id')
      st.write('Selected chapters keys : ', st.session_state.currentlySelectedIds)


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
