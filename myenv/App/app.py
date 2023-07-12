import streamlit as st
from streamlit_chat import message
from database import get_target_params_for_this_values
from createIndices import create_combined_index_for_directory, create_index_for_each_entry_in_db
from generateResponse import generate_response_from_common_index

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
  if 'generated' not in st.session_state:
    st.session_state['generated'] = []
  if 'past' not in st.session_state:
    st.session_state['past'] = []
  if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]


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
    st.divider()
    response_container = st.container()
    input_container = st.container()

    with input_container:
      with st.form(key='my_form', clear_on_submit=True):
          user_input = st.text_area("You:", key='input', height=50)
          submit_button = st.form_submit_button(label='Send')

      if submit_button and user_input:
          output = generate_response_from_common_index(user_input)
          st.session_state['past'].append(user_input)
          st.session_state['generated'].append(output)
          
    if st.session_state['generated']:
      with response_container:
        for i in range(len(st.session_state['generated'])):
          message(st.session_state["past"][i], is_user=True, key=str(i) + '_user1')
          message(st.session_state["generated"][i], key=str(i))
  
  else:
    st.header("Please load some chapters first.")  



if __name__ == '__main__':
  main()
