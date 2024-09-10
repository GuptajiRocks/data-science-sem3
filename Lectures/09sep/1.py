import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

data = np.random.rand(10,10)

st.pyplot(sns.heatmap(data, cmap="coolwarm"))

#st.write(ste)
# Scatter plot used for correlation
# Box plot used for outlier detection, spread and skewness of data
#
# Skewness of data is the inclination of data points over a time period
# Record, Visualize and Analyze are three major aspects of Visualisation
# 
# Violin Plot: Distribution of data across different categories
# 
# HeatMap: Correlation matrix with different stages being represented by diff colors.
# 
# Area Plot: 
# 
# Bubble Chart: Visualising multi dimensional data, used to show importance between different data points
# 
# Joint plot: Scatter PLot + Histogram
# 
# 3D plot, facet grid: Jesus christ Idk
# 
# #
