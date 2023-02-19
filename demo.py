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
# st.markdown("<h4 style = 'color : DodgerBlue;'>Display Number of Rows & Columns (Before Data Cleaning)</h4>", unsafe_allow_html = True)
# st.text('\nThe Dataset has ' + str(df.shape[0]) + ' rows.')
# st.text('\nThe Dataset has ' + str(df.shape[1]) + ' columns.')

# Shape of Data 
# st.text('\nShape of Data : ' + str(df.shape))

# st.text("\n\n")

# DataFrame Columns 
# st.markdown("<h4 style = 'color : DodgerBlue;'>Original Dataset Column Names</h4>", unsafe_allow_html = True)
# st.text(df.columns)

# st.text("\n\n")

# Updated DataFrame Columns
# st.markdown("<h4 style = 'color : DodgerBlue;'>Updated Dataset Column Names</h4>", unsafe_allow_html = True)

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
# st.text(df.columns)

# st.text("\n\n")

# Update Columns & Create New Groups In Dataset
# NOTE : Here, I'm updating some of the records & create groups inside the data.
# 1. Here, I've replaced the country name from a big string with a short string/short form.
# Before Replace Country Name
# st.markdown("<h4 style = 'color : DodgerBlue;'>Before Update The Few Countries Name</h4>", unsafe_allow_html = True)
# st.text("\n* * Before Replace Country Name * *\n")
# st.text(df['In which country do you currently reside?'].unique())

# st.text("\n\n")

# Replace United Kingdom of Great Britain and Northern Ireland With UK & Ireland
# st.markdown("<h4 style = 'color : DodgerBlue;'>Replace United Kingdom of Great Britain and Northern Ireland With UK & Ireland</h4>", unsafe_allow_html = True)
df['In which country do you currently reside?'] = df['In which country do you currently reside?'].replace({'United States of America' : 'USA', 'United Kingdom of Great Britain and Northern Ireland' : 'UK & Ireland'})
# After Replace Country Name
# print("\n* * After Replace Country Name * *\n")
# st.text(df['In which country do you currently reside?'].unique())

# st.text("\n\n")

# st.markdown("<h4 style = 'color : DodgerBlue;'>Here, I categorised age ranges between the 3 groups.</h4>", unsafe_allow_html = True)
# st.write(':blue[Young Adults [18 - 39]]\n\n',
# ':blue[Middle Aged Adults [40 - 59]]\n\n',
# ':blue[Old Adults [60 - 70+]]\n\n')

# Before Update Age Data
# print("\n* * Before Update Age Data * *\n")
# df['What is your age (# years)?'].unique()
# Replace Age Values (For Identifying Age Groups - Young Adults(18-39), Middle Aged Adults(40-59) & Old Adults(60-70+))
df['What is your age (# years)?'] = df['What is your age (# years)?'].replace(['18-21', '22-24', '25-29', '30-34', '35-39'], '18-39')
df['What is your age (# years)?'] = df['What is your age (# years)?'].replace(['40-44', '45-49', '50-54', '55-59'], '40-59')
df['What is your age (# years)?'] = df['What is your age (# years)?'].replace(['60-69', '70+'], '60-70+')

# Display Age Columns Unique Values
# df['What is your age (# years)?'].unique()

# After Update Age Data
# print("\n* * After Update Age Data * *\n")
# df['What is your age (# years)?'].unique()

# st.text("\n\n")

# 3. Here, I've categorised gender between 3 groups.
# Man
# Woman
# Other ('Prefer not to say', 'Nonbinary', 'Prefer to self-describe')
# Before Update Gender Data
# print("\n* * Before Update Gender Data * *\n")
# df['What is your gender? - Selected Choice'].unique()

# Update Gender Data
df['What is your gender? - Selected Choice'] = df['What is your gender? - Selected Choice'].replace(['Prefer not to say', 'Nonbinary', 'Prefer to self-describe'], 'Other')

# After Update Gender Data
# print("\n* * After Update Gender Data * *\n")
# df['What is your gender? - Selected Choice'].unique()

# st.text("\n\n")

# 4. Here, I've create 7 Ranges of Earning.
# 0-999
# 1000-9,999
# 10,000-49,999
# 50,000-99,999
# 100,000-499,999
# 500,000-999,999
# ">"10,000,00

# Before Update Earning Data
# print("\n* * Before Update Earning Data * *\n")
# df['What is your current yearly compensation (approximate $USD)?'].unique()
df['What is your current yearly compensation (approximate $USD)?'] = df['What is your current yearly compensation (approximate $USD)?'].replace(['$0-999'], '0-999')
df['What is your current yearly compensation (approximate $USD)?'] = df['What is your current yearly compensation (approximate $USD)?'].replace(['3,000-3,999', '5,000-7,499', '7,500-9,999', '4,000-4,999', '2,000-2,999', '1,000-1,999'], '1000-9,999')
df['What is your current yearly compensation (approximate $USD)?'] = df['What is your current yearly compensation (approximate $USD)?'].replace(['25,000-29,999', '30,000-39,999', '20,000-24,999', '15,000-19,999', '10,000-14,999', '40,000-49,999'], '10,000-49,999')
df['What is your current yearly compensation (approximate $USD)?'] = df['What is your current yearly compensation (approximate $USD)?'].replace(['90,000-99,999', '50,000-59,999', '80,000-89,999', '70,000-79,999', '60,000-69,999'], '50,000-99,999')
df['What is your current yearly compensation (approximate $USD)?'] = df['What is your current yearly compensation (approximate $USD)?'].replace(['100,000-124,999', '200,000-249,999', '150,000-199,999', '125,000-149,999', '250,000-299,999', '300,000-499,999'], '100,000-499,999')
df['What is your current yearly compensation (approximate $USD)?'] = df['What is your current yearly compensation (approximate $USD)?'].replace(['$500,000-999,999', ], '500,000-999,999')
df['What is your current yearly compensation (approximate $USD)?'] = df['What is your current yearly compensation (approximate $USD)?'].replace(['>$1,000,000'], '>10,000,00')

# Display Unique Values
# df['What is your current yearly compensation (approximate $USD)?'].unique()

# # After Update Earning Data
# print("\n* * After Update Earning Data * *\n")
# df['What is your current yearly compensation (approximate $USD)?'].unique()

st.text("\n\n")

# 5. Some of the options has separate columns, So here I define a function to combine those options in single column.
# Define Function For Combine All Optional Columns of Options
def store_option_into_column(col1, col2, new_column_name):
    
    # Fill NA With '0'
    for i in df.columns[col1:col2]:
        df[i].fillna(0, inplace = True)

    # Empty List
    lst1=[]

    for i in range(len(df)):
        # Empty List
        lst2 = []

        for j in df.columns[col1:col2]:
            tmp = df.loc[i][j]

            if tmp == 0:
                lst2.append(tmp)

            if len(lst2) == (col2 - col1):
                lst1.append('None')
                break

            if tmp != 0:
                lst1.append(tmp.strip())
                break

    # Create New Columns        
    df[new_column_name] = lst1
    
# Function Calling "store_option_into_column"
store_option_into_column(5, 16, 'Learning Platform')
store_option_into_column(17, 23, 'Suggested Learning Platform')
store_option_into_column(30, 44, 'Programming Language(Regular)')
store_option_into_column(45, 58, 'IDE(Regular)')
store_option_into_column(59, 74, 'Used Hosted Notebook')
store_option_into_column(75, 89, 'Suggested Data Visualization')
store_option_into_column(91, 105, 'ML Frameworks')
store_option_into_column(106, 119, 'ML Algorithms')
store_option_into_column(120, 127, 'Computer Vision Methods')
store_option_into_column(127, 132, 'NLP Methods')
store_option_into_column(159, 170, 'Used Cloud Computing Platform')
store_option_into_column(172, 176, 'Suggested Cloud Computing Platform')
store_option_into_column(177, 184, 'Suggested Storage Products')
store_option_into_column(185, 200, 'Suggested Data Products')
store_option_into_column(201, 215, 'Suggested Business Intelligence Tools')

# Display Combined Options For Suggested Data Visualization Unique Values
# df['Suggested Data Visualization'].unique()

# Display Number of Rows & Columns (After Data Cleaning)
# print('\nAfter Data Cleaning Dataset Has ' + str(df.shape[0]) + ' Rows.')

# print('\nAfter Data Cleaning Dataset Has ' + str(df.shape[1]) + ' Columns.')

# # Shape of Data 
# print('\nShape of Data : ', df.shape)

# st.text("\n\n")

# Number of Missing Values
# df.isnull().sum

st.markdown("<h4 style = 'color : DodgerBlue;'>1. Analysis Based On Kaggler\'s Age Group(Young Adults, Middle Aged Adults & Old Adults.</h4>", unsafe_allow_html = True)
def fig1():
	# Calculation For Young Adults
	count_young_adults = len(df[(df['What is your age (# years)?'].isin(['18-39']))])
	young_adults = len(df[(df['What is your age (# years)?'].isin(['18-39']))]) * 100 / len(df[1:])

	print('Young Adults Counts (18-39) : ' + str(count_young_adults))
	print('\nYoung Adults % (18-39) : ' + str(young_adults) + '%')

	# Calculation For Middle Aged Adults
	count_middle_aged_adults = len(df[(df['What is your age (# years)?'].isin(['40-59']))])
	middle_aged_adults = len(df[(df['What is your age (# years)?'].isin(['40-59']))]) * 100 / len(df[1:])

	print('Count of Middle Aged Adults Counts (40-59) : ' + str(count_middle_aged_adults))
	print('\nMiddle Aged Adults % (40-59) : ' + str(middle_aged_adults) + '%')

	# Calculation For Old Adults
	count_old_adults = len(df[(df['What is your age (# years)?'].isin(['60-70+']))])
	old_adults = len(df[(df['What is your age (# years)?'].isin(['60-70+']))]) * 100 / len(df[1:])

	print('Old Adults Counts (60-70+) : ' + str(count_old_adults))
	print('\nOld Adults % (60-70+) : ' + str(old_adults) + '%')

	# Define Color Sets 
	colors = ['#002266', '#3377ff', '#ccddff']

	# Pie Chart Based On Age Analysis
	labels = ['Young Adults (18-39)', 'Middle Aged Adults (40-59)', 'Old Adults (60-70+)']
	values = [count_young_adults, count_middle_aged_adults, count_old_adults]

	# Pie Chart
	pie1 = go.Pie(labels = labels, values = values, marker_colors = colors)

	# Explode Width, Color & Size
	pie1.marker.line.width = 10
	pie1.marker.line.color = 'white'
	pie1.hole = 0.5

	# Pie Chart Data Display
	pie1.textposition = 'outside'
	pie1.textinfo = 'percent+label'
	pie1.showlegend = True

	# Display Pie Chart
	fig1 = go.Figure(data = [pie1], layout = dict(title = dict(text = "Kaggle Survey 2022 - Analysis Based On World Wide Kaggler's Age")))
	fig1.update_layout(annotations = [dict(text = 'AGE', x = 0.50, y = 0.5, font_size = 20, showarrow = False)])
	fig1.show()
   
st.button("Show Figure 1", on_click=fig1, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)

