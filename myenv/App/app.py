import os
import streamlit as st
from database import get_target_params_for_this_values

import openai
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
  st.set_page_config(page_title="POC GPT knowledgebase", page_icon="📖", layout="wide")
  initiateSessionStorage()
  sidebar()
  
  if st.session_state['loaded']:
    st.header("📖 Ask your Chapters")
  else:
    st.header("Please load some chapters first.")
  # This function will create a combined index of all the syllabus available in docs directory.
  # This is meant to be ran for only one time.
  # createIndexForAllFilesTogather()

  # This function will create index for each file available in docs directory.
  # This is meant to be ran for only one time.
  # createIndexForEachFile()
  
  # print('Answer : ', generate_response_from_common_index("Acids change the blue litmus paper to which colour?"))
  # print('Answer : ', generate_response_from_common_index("How do they taste?"))


if __name__ == '__main__':
  main()
