import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
#  Shaik Khadeer, AI Engineer.
##### *Resume* 
''')

image = Image.open('dp.jpg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Data Scientist, Researcher and Administrator with almost 1 year of experience in data-oriented environment and a passion for delivering insights based on predictive modeling. 
- Now studying in RGUKT IIIT Ongole, E2 .
- Proficient in Python, R, SQL, Machine Learning, Deep Learning, Data Visualization, Web Development, Model Deployment.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/khadeer-shaik-367474288/" target="_blank">Shaik Khadeer</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**RGUKT IIIT ONGOLE E2** , 2024-Present','**Exicted in AI Engineer Course**'
'2021-2027')
st.markdown('''
- GPA: `8.6`
- place : `Ongole, Andhra Pradesh, India`
- Studying in E2 CSE branch.
- Learning Python, R, SQL, Machine Learning, Deep Learning, Data Visualization, Web Development, Model Deployment.
- Working on projects related to Data Science and Machine Learning.
- Participated in Hackathons and Coding Competitions.
- Member of Coding Club.
- Member of AI Club.
- AI enthusiast.
''')

txt('**Bachelors of Computer Science** (Computer Science), *Rajiv Gandhi University of Knowledge and Technologies*, Ongole',
'2021-2027')
st.markdown('''
- GPA: `8.6`
- Graduated with First Class Honors.
''')

#####################
st.markdown('''
## Work Experience
''')


st.markdown('''
- **Doing Machine Learning Projects ,Focusing on AI based technologies..**
- Searching for Internships in AI and Machine Learning.
''')






#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`,`C`, `C++`, `Java`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`,`Deep Learning` ,`Neural Networks`')
txt3('Deep Learning', '`TensorFlow`,`Keras`,`PyTorch`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/khadeer-shaik-367474288/')
txt2('Twitter', 'https://x.com/khadee_shaik')
txt2('GitHub', 'https://github.com/khadee-shaik')
txt2('Medium', 'https://medium.com/@khadeer-shaik')
txt2('Kaggle', 'https://www.kaggle.com/khadeershaik')
txt2('Email', 'skr7993257687@gmail.com')