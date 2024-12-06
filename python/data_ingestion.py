#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sodapy import Socrata
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define constants
DATA_URL = 'data.ny.gov'
DATASET_ID = 'iq85-sdzs'
APP_TOKEN = 'rW5rcLZfhjn60pNPRR4iEVhBG'
OUTPUT_CSV_FILE = 'Real_Property_Tax_Rates_Levy_Data.csv'

def fetch_data():
    """Fetch data using the Socrata client and return as a DataFrame."""
    # Create a client instance
    client = Socrata(DATA_URL, APP_TOKEN, timeout=100)
    
    try:
        # Fetch data from the API
        logging.info("Starting data fetch...")
        results = client.get(DATASET_ID, limit=5000)  # Adjust limit as needed
        logging.info(f"Data fetched successfully: {len(results)} records")
        
        # Convert results to DataFrame
        df = pd.DataFrame.from_records(results)
        return df
    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error
    finally:
        # Always close the client
        client.close()

def save_data(df):
    """Save the DataFrame to a CSV file."""
    if not df.empty:
        df.to_csv(OUTPUT_CSV_FILE, index=False)
        logging.info(f"Data saved to {OUTPUT_CSV_FILE}")
    else:
        logging.info("No data to save.")

def main():
    """Main function to handle the data fetching and saving process."""
    df = fetch_data()
    if not df.empty:
        save_data(df)
    else:
        logging.info("No data was fetched to process.")

if __name__ == "__main__":
    main()


# In[ ]:




