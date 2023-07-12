import streamlit as st
from database import get_target_params_for_this_values
from createIndices import create_combined_index_for_directory

import openai, os
key = '<KEY>' # UPDATE THE KEY BEFORE RUNNING
openai.api_key = key
os.environ['OPENAI_API_KEY'] = key


def initiateSessionStorage():
  # This flag is for tracking combined searchEngine generation
  if 'loaded' not in st.session_state:
    st.session_state['loaded'] = False
  # This is for current selected labels
  if "currentlySelectedLabels" not in st.session_state:
    st.session_state['currentlySelectedLabels'] = []


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
      get_target_params_for_this_values('label', 'subject', ['science']), key='scienceChapters')
    
    SocialScienceExpander = st.expander("Class 10 Social-Science")
    socialScienceChapters = SocialScienceExpander.multiselect('Select the chapters that you want to ask :',
      get_target_params_for_this_values('label', 'subject', ['socialscience']), key='socialScienceChapters')
    
    st.divider()

    if st.button('Load Chapters'):
      st.session_state['currentlySelectedLabels'] = scienceChapters + socialScienceChapters
      st.session_state['loaded'] = True
      st.write('Selected chapters labels : ', st.session_state['currentlySelectedLabels'])


def main():

  # This function will create a combined index of all the syllabus available in docs directory.
  # This is meant to be ran for only one time.
  # create_combined_index_for_directory('./Docs', 'combinedIndex')

  # This function will create index for each file available in database.
  # This is meant to be ran for only one time.
  # create_index_for_each_entry_in_db()

  st.set_page_config(page_title="POC GPT knowledgebase", page_icon="📖", layout="wide")

  initiateSessionStorage()
  sidebar()
  
  if st.session_state['loaded']:
    st.header("📖 Ask your Chapters")
  else:
    st.header("Please load some chapters first.")


if __name__ == '__main__':
  main()
