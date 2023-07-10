import streamlit as st
from dotenv import load_dotenv

st.set_page_config(page_title="POC GPT knowledgebase", page_icon="📖", layout="wide")
st.header("📖 Ask your Books")

# Available Chapterlist Arrays
availableScienceChapters = [
  {
    "path": './docs/Science/Science_ch2.pdf',
    "label": 'Ch-2 : Acids, Bases and Salts',
    "key": 'science_ch_2'
  },
  {
    "path": './docs/Science/Science_ch3.pdf',
    "label": 'Ch-3 : Metals and Non-metals',
    "key": 'science_ch_3'
  },
  {
    "path": './docs/Science/Science_ch13.pdf',
    "label": 'Ch-13 : Our Environment',
    "key": 'science_ch_13'
  },
]


availableSocialScienceChapters = [
  {
    "path": './docs/ScocialScience/SS_ch1.pdf',
    "label": 'Ch-1 : Resources and Development',
    "key": 'ss_ch_2'
  },
  {
    "path": './docs/ScocialScience/SS_ch2.pdf',
    "label": 'Ch-2 : Forest and wildlife resources',
    "key": 'ss_ch_2'
  },
  {
    "path": './docs/ScocialScience/SS_ch3.pdf',
    "label": 'Ch-3 : Water Resources',
    "key": 'ss_ch_3'
  },
  {
    "path": './docs/ScocialScience/SS_ch4.pdf',
    "label": 'Ch-4 : Agriculture',
    "key": 'ss_ch_4'
  },
]


def getParams(chapters, key):
  return [chapter[key] for chapter in chapters]


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
      getParams(availableScienceChapters, 'label'), key='scienceChapters')
    SocialScienceExpander = st.expander("Class 10 Social-Science")
    socialScienceChapters = SocialScienceExpander.multiselect('Select the chapters that you want to ask :',
      getParams(availableSocialScienceChapters, 'label'), key='socialScienceChapters')
    st.divider()
    st.write('Science chapters : ', scienceChapters)
    st.write('Social-Science chapters : ', socialScienceChapters)


def main():
  load_dotenv()
  sidebar()


if __name__ == '__main__':
  main()
