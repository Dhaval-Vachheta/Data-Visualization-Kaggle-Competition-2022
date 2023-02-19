# Import Libraries
import pandas as pd
import numpy as np

# Data Visualizaiton
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from matplotlib import pyplot as plt
%matplotlib inline
import seaborn as sb

# Load CSV Data
# df = pd.read_csv("../input/kaggle-survey-2022/kaggle_survey_2022_responses.csv")
url = 'https://github.com/Dhaval-Vachheta/Data-Visualization-Kaggle-Competition-2022/blob/main/Dataset/kaggle_survey_2022_responses.csv'
df = pd.read_csv(url)

# Extend Columns In Output
pd.set_option('display.max_columns', 350)

# Display Data
df.head()
