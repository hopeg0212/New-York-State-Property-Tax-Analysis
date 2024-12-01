#!/usr/bin/env python
# coding: utf-8

# In[8]:


pip install sodapy


# In[9]:


pip install pandas


# In[11]:


#!/usr/bin/env python

import pandas as pd
from sodapy import Socrata

def main():
    # Initialize the client with the dataset's base URL, your app token, and your credentials
    client = Socrata("data.ny.gov",
                     app_token="rW5rcLZfhjn60pNPRR4iEVhBG",
                     username="hopeg0212@gmail.com",
                     password="2fmjTtn8PhyNe!N")

    # Fetch the data from the dataset
    results = client.get("q4hy-kbtf", limit=2000)

    # Convert the results to a DataFrame
    results_df = pd.DataFrame.from_records(results)

    # Data cleaning and transformation steps
    clean_and_transform_data(results_df)

    # Save the cleaned DataFrame to a CSV file
    results_df.to_csv('output.csv', index=False)
    print("Data has been successfully saved to output.csv")

def clean_and_transform_data(df):
    """ Clean and transform DataFrame as needed. """
    # Example: Convert date columns to datetime objects
    if 'issue_date' in df.columns:
        df['issue_date'] = pd.to_datetime(df['issue_date'])
    
    # Add more data cleaning and transformation steps here
    # Example: Fill missing values, remove duplicates, etc.
    df.fillna(method='ffill', inplace=True)  # Forward fill for missing values

if __name__ == "__main__":
    main()


# In[13]:


import os
app_token = os.getenv("APP_TOKEN")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")


# In[17]:


pip install google-auth


# In[18]:


pip install pandas-gbq


# In[19]:


# Install required packages for the project
get_ipython().system('pip install pandas sodapy google-auth pandas-gbq')


# In[20]:


# Check if the google-auth and pandas-gbq modules are correctly installed
try:
    from google.oauth2 import service_account
    from pandas_gbq import to_gbq
    print("Modules are installed and imported successfully!")
except ImportError as e:
    print("An error occurred:", e)


# In[28]:


import os
import json
import logging
import pandas as pd
from sodapy import Socrata

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define paths and constants
current_dir = os.getcwd()
csv_file_path = os.path.join(current_dir, 'traffic_tickets_data.csv')
offset_file_path = os.path.join(current_dir, 'last_successful_offset.json')

# API configuration
data_url = 'data.ny.gov'
dataset_id = 'q4hy-kbtf'
app_token = 'rW5rcLZfhjn60pNPRR4iEVhBG'  # Your API token

client = Socrata(data_url, app_token, timeout=100)

def get_last_successful_offset():
    """Retrieve the last successful offset from a file."""
    if os.path.exists(offset_file_path):
        with open(offset_file_path, 'r') as f:
            data = json.load(f)
            return data.get('last_offset', 0)
    return 0

def save_last_successful_offset(offset):
    """Save the current offset to a file."""
    with open(offset_file_path, 'w') as f:
        json.dump({'last_offset': offset}, f)

def fetch_data_chunk(start_offset, chunk_size):
    """Fetch a chunk of data from the API."""
    rows = client.get(dataset_id, offset=start_offset, limit=chunk_size)
    return pd.DataFrame.from_records(rows)

def clean_data(df):
    """Perform data cleansing and quality checks."""
    # Convert columns to appropriate data types and handle missing values
    numeric_cols = ['violation_year', 'violation_month', 'age_at_violation']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    df.fillna({'gender': 'U', 'state_of_license': 'Unknown'}, inplace=True)
    return df

def save_to_csv(df):
    """Save the data chunk to a CSV file."""
    if not os.path.exists(csv_file_path):
        df.to_csv(csv_file_path, index=False, mode='w')
    else:
        df.to_csv(csv_file_path, index=False, mode='a', header=False)
    logging.info("Data chunk saved to CSV.")

def fetch_and_process_data(chunk_size=1000, max_records=50000, max_retries=3, retry_delay=5):
    """Main function to fetch data from API and process it."""
    start_offset = get_last_successful_offset()
    total_records_fetched = 0

    while start_offset < max_records:
        data_chunk = fetch_data_chunk(start_offset, chunk_size)
        if data_chunk.empty:
            logging.info("No more data to fetch.")
            break

        fetched_records = len(data_chunk)
        total_records_fetched += fetched_records
        start_offset += fetched_records
        save_last_successful_offset(start_offset)

        logging.info(f"Fetched {fetched_records} records. Total fetched: {total_records_fetched}")

        data_chunk = clean_data(data_chunk)
        save_to_csv(data_chunk)

if __name__ == '__main__':
    fetch_and_process_data()


# In[ ]:




