#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


file_path = 'Real_Property_Tax_Rates_Levy_Data.csv'
data = pd.read_csv(file_path)


# In[5]:


import pandas as pd

def load_data(filepath):
    """Load data from a CSV file."""
    try:
        data = pd.read_csv(filepath)
        print("Data loaded successfully!")
        return data
    except FileNotFoundError:
        print(f"Error: The file {filepath} does not exist.")
        return None

def clean_column_names(df):
    """Standardize column names by replacing spaces with underscores and lowercasing."""
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace(r'[^a-zA-Z0-9_]', '')
    return df

def handle_missing_values(df):
    """Fill missing numeric values with zero and categorical values with 'Unknown'."""
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    df[numeric_cols] = df[numeric_cols].fillna(0)
    df[categorical_cols] = df[categorical_cols].fillna('Unknown')
    return df

def convert_data_types(df):
    """Convert data types to appropriate formats."""
    # Convert fiscal_year_ending to datetime format
    df['fiscal_year_ending'] = pd.to_datetime(df['fiscal_year_ending'], format='%Y', errors='coerce')

    # Convert any IDs or codes from floats to strings if they are not meant to be used for calculations
    df['swis_code'] = df['swis_code'].astype(str)
    df['school_code'] = df['school_code'].astype(str)
    
    return df

def save_cleaned_data(df, output_filepath):
    """Save the cleaned DataFrame to a new CSV file."""
    df.to_csv(output_filepath, index=False)
    print(f"Cleaned data saved to {output_filepath}")

def main():
    filepath = 'Real_Property_Tax_Rates_Levy_Data.csv'
    output_filepath = 'cleaned_Real_Property_Tax_Rates_Levy_Data.csv'
    
    # Load data
    df = load_data(filepath)
    if df is None:
        return
    
    # Clean operations
    df = clean_column_names(df)
    df = handle_missing_values(df)
    df = convert_data_types(df)
    
    # Save cleaned data
    save_cleaned_data(df, output_filepath)

if __name__ == "__main__":
    main()


# In[ ]:




