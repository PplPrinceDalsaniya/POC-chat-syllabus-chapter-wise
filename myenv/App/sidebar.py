import streamlit as st
from database import availableDatabase, getParams, get_params_from_labels


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
