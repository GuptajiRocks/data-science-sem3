import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title of the Streamlit app
st.title('Exploratory Data Analysis Project')

# Function to load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('D:\\Bennett University\\Sem 3\\Data Analysis Using Python - CSET214\\Courses\\14sep\\train.csv')  # Replace this with your dataset's file path
    return data

# Load the data
data = load_data()

# Display a subheader for the dataset overview
st.subheader('Dataset Overview')
st.write(data.head())

# Display basic info and statistics of the dataset
st.subheader('Dataset Info')
st.write('Number of Rows: ', data.shape[0])
st.write('Number of Columns: ', data.shape[1])
st.write(data.describe())

# Display missing data
st.subheader('Missing Data')
st.write(data.isnull().sum())

# Visualize the distribution of a numerical column (Age)
st.subheader('Age Distribution')

fig, ax = plt.subplots()
sns.histplot(data['Age'].dropna(), kde=True, bins=30, ax=ax)
st.pyplot(fig)

# Display the correlation matrix
st.subheader('Correlation Matrix')

corr = data.corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Visualize the relationship between a categorical (Survived) and numerical (Age) variable
st.subheader('Survival by Age')

fig, ax = plt.subplots()
sns.boxplot(x='Survived', y='Age', data=data, ax=ax)
st.pyplot(fig)

# Display the distribution of categorical variables
st.subheader('Distribution of Categorical Variables')

# Sidebar for categorical column selection
category_col = st.sidebar.selectbox('Choose a categorical column', data.select_dtypes(include='object').columns)

fig, ax = plt.subplots()
sns.countplot(x=category_col, data=data, ax=ax)
st.pyplot(fig)

# Sidebar filters for interactive EDA
st.sidebar.subheader('Filter Data')

# Age filter
age_filter = st.sidebar.slider('Age Range', int(data['Age'].min()), int(data['Age'].max()), 
                               (int(data['Age'].min()), int(data['Age'].max())))

# Gender filter
gender_filter = st.sidebar.multiselect('Gender', options=data['Sex'].unique(), default=data['Sex'].unique())

# Apply the filters to the dataset
filtered_data = data[(data['Age'] >= age_filter[0]) & (data['Age'] <= age_filter[1]) & (data['Sex'].isin(gender_filter))]

# Display filtered data
st.subheader('Filtered Data')
st.write(filtered_data.head())

# Additional plot: Survival rate by class
st.subheader('Survival Rate by Class')

fig, ax = plt.subplots()
sns.barplot(x='Pclass', y='Survived', data=data, ax=ax)
st.pyplot(fig)

# Heatmap of missing values
st.subheader('Heatmap of Missing Values')

fig, ax = plt.subplots()
sns.heatmap(data.isnull(), cbar=False, cmap='viridis', ax=ax)
st.pyplot(fig)

