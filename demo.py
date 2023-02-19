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

# # Load CSV Data
# # df = pd.read_csv("../input/kaggle-survey-2022/kaggle_survey_2022_responses.csv")
url = 'https://github.com/Dhaval-Vachheta/Data-Visualization-Kaggle-Competition-2022/blob/main/Dataset/kaggle_survey_2022_responses.csv'
df = pd.read_csv(url,index_col=0)

# # Extend Columns In Output
# # pd.set_option('display.max_columns', 350)

# # Display Data
# st.dataframe(df)

# df = pd.DataFrame(
#     np.random.randn(10, 5),
#     columns=("col %d" % i for i in range(5)))

# # Display a static table
# st.table(df)

# Display an interactive table
st.dataframe(df)
