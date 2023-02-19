# # Import Libraries
import streamlit as st
import pandas as pd
import numpy as np

# # # Data Visualizaiton
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from matplotlib import pyplot as plt
%matplotlib inline
import seaborn as sb

# TITLE
# st.title(":blue[Data Visualization]")
st.markdown("<h1 style = 'text-align : center; color : DodgerBlue;'>Data Visualization</h1>", unsafe_allow_html = True)

# Header
st.markdown("<h4 style = 'text-align : center; color : DodgerBlue;'>Kaggle Survey 2022 Dataset</h4>", unsafe_allow_html = True)

# Load CSV Data
url = 'https://github.com/Dhaval-Vachheta/Data-Visualization-Kaggle-Competition-2022/blob/main/Dataset/kaggle_survey_2022_responses.csv?raw=true'
df = pd.read_csv(url)

# Extend Columns In Output
pd.set_option('display.max_columns', 350)

# Display a static table
# st.table(df)

# Display Entire Data
st.dataframe(df)

# Analysis Questions
st.write('\n**Following Questions Are Described Using EDA(Exploratory Data Analysis)**\n\n',
'1. Analysis Based On Kaggler\'s Age Group(Young Adults, Middle Aged Adults & Old Adults).\n',
'2. Analysis Based On Top 10 Countries Wise Age Division.\n',
'3. Analysis Based On Kaggler\'s Gender(Man, Woman & Other).\n',
'4. Analysis of Top 5 Countries Based On Highest Participants.\n',
'5. Analysis Based On Gender Wise Division For Kaggler\'s In Top 10 Countries.\n',
'6. Analysis Based On Top 10 Countries Wise Earning.\n',
'7. Age Group Analysis Based On Gender.\n',
'8. Kaggler\'s Analysis Based On Earning.\n',
'9. Analysis Based On Earning Wise Age Division.\n',
'10. Analysis Based On Current Role & Position.\n',
'11. Analysis Based On Current Role Wise Earning.\n',
'12. Analysis Based On Current Role With Gender Classification.\n',
'13. Analysis Based On Current Role With Age Group.\n',
'14. Analysis Based On Writting Code Experience.\n',
'15. Analysis Based On Code Experience With Age Group.\n',
'16. Analysis Based On Countries Wise Code Writting Experience.\n',
'17. Analysis Based On Suggested Cloud Computing Platform.\n',
'18. Analysis Based On NLP Methods.\n',
'19. Analysis Based On Computer Vision Methods.\n',
'20. Analysis Based On ML Algorithms.\n',
'21. Analysis Based On ML Frameworks.\n',
'22. Analysis Based On Suggested Data Visualization.\n',
'23. Analysis Based On Suggested Business Intelligence Tools.\n',
'24. Analysis Based On Suggested Data Products.\n',
'25. Analysis Based On Suggested Learning Platform.\n',
'26. Analysis Based On Used Hosted Notebook.\n',
'27. Analysis Based On Used IDE On Regular Basis.\n',
'28. Analysis Based On Programming Language(Regular).\n',
'29. Analysis Based On Learning Platform.\n')
