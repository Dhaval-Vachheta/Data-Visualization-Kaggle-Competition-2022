# # Import Libraries
import streamlit as st
import pandas as pd
import numpy as np

# # # Data Visualizaiton
# # import plotly.express as px
# # import plotly.graph_objects as go
# # from plotly.subplots import make_subplots
# # from matplotlib import pyplot as plt
# # %matplotlib inline
# # import seaborn as sb

# TITLE
# st.title(":blue[Data Visualization]")
st.markdown("<h1 style = 'text-align : center; color : DodgerBlue;'>Data Visualization</h1>", unsafe_allow_html=True)

# # Load CSV Data
# # df = pd.read_csv("../input/kaggle-survey-2022/kaggle_survey_2022_responses.csv")
url = 'https://github.com/Dhaval-Vachheta/Data-Visualization-Kaggle-Competition-2022/blob/main/Dataset/kaggle_survey_2022_responses.csv?raw=true'
df = pd.read_csv(url)

# # Extend Columns In Output
pd.set_option('display.max_columns', 350)

# # Display a static table
# st.table(df)

# Display Entire Data
st.dataframe(df)
