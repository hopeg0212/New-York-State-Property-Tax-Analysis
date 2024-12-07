#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


file_path = 'Real_Property_Tax_Rates_Levy_Data.csv'
data = pd.read_csv(file_path)


# In[6]:


# Load the dataset and clean the column names to be SQL-ready

import pandas as pd

# Load the dataset
file_path = 'Real_Property_Tax_Rates_Levy_Data_By_Municipality__Beginning_2004_20241206.csv'
data = pd.read_csv(file_path)

# Function to make column names SQL-ready
def make_sql_ready_columns(df):
    df.columns = (
        df.columns.str.strip()  # Remove leading/trailing spaces
        .str.lower()  # Convert to lowercase
        .str.replace(' ', '_')  # Replace spaces with underscores
        .str.replace(r'[^a-zA-Z0-9_]', '', regex=True)  # Remove special characters
    )
    return df

# Apply the function to the dataset
data = make_sql_ready_columns(data)

# Save the cleaned file
output_file_path = 'cleaned_Real_Property_Tax_Rates_Levy_Data.csv'
data.to_csv(output_file_path, index=False)

output_file_path



# In[ ]:




