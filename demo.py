# # Import Libraries
import streamlit as st
import pandas as pd
import numpy as np

# # # Data Visualizaiton
# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# from matplotlib import pyplot as plt
# %matplotlib inline
# import seaborn as sb

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

st.text("\n\n")

# Analysis Questions
st.write('\n:blue[**Following Questions Are Described Using EDA(Exploratory Data Analysis)**]\n\n',
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

# Display Number of Rows & Columns (Before Data Cleaning)
st.markdown("<h4 style = 'color : DodgerBlue;'>Display Number of Rows & Columns (Before Data Cleaning)</h4>", unsafe_allow_html = True)
st.text('\nThe Dataset has ' + str(df.shape[0]) + ' rows.')
st.text('\nThe Dataset has ' + str(df.shape[1]) + ' columns.')

# Shape of Data 
st.text('\nShape of Data : ' + str(df.shape))

st.text("\n\n")

# DataFrame Columns 
st.markdown("<h4 style = 'color : DodgerBlue;'>Original Dataset Column Names</h4>", unsafe_allow_html = True)
st.text(df.columns)

st.text("\n\n")

# Updated DataFrame Columns
st.markdown("<h4 style = 'color : DodgerBlue;'>Updated Dataset Column Names</h4>", unsafe_allow_html = True)

# Just Copy DataFrame Into Another Variable
new_df = df.copy()

# Replace Columns Name
df.columns = df.iloc[0]

# Records Store From 1 Index
df = df[1:]

# Reset Index
df.reset_index(inplace = True)

# Drop Index Column
df.drop('index', axis = 1, inplace = True)

# Display Column Names
st.text(df.columns)

# Update Columns & Create New Groups In Dataset
# NOTE : Here, I'm updating some of the records & create groups inside the data.
# 1. Here, I've replaced the country name from a big string with a short string/short form.
# Before Replace Country Name
st.markdown("<h4 style = 'color : DodgeBlue;'>Before Update The Few Countries Name</h4>", unsafe_allow_html = True)
st.text("\n* * Before Replace Country Name * *\n")
st.text(df['In which country do you currently reside?'].unique())
