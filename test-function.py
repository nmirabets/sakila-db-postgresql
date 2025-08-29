import os
import dotenv
from sqlalchemy import create_engine, text
import pandas as pd
import streamlit as st

dotenv.load_dotenv()


# Define the get_supabase_data_df function (Supabase PostgreSQL)
def get_supabase_data_df(sql_query):
    """
    Fetch data from Supabase PostgreSQL Sakila database
    
    Args:
        sql_query (str): SQL query to execute
        
    Returns:
        tuple: (sql_query, dataframe) - The executed query and resulting pandas DataFrame
        
    Example:
        query = "SELECT * FROM film LIMIT 10"
        sql, df = get_supabase_data_df(query)
    """
    try:
        # Try to get full connection string first, then fallback to individual components
        supabase_connection_string = os.getenv("SUPABASE_CONNECTION_STRING")
        
        if supabase_connection_string:
            # Use the full connection string directly from Supabase
            connection_string = supabase_connection_string
        else:
            # Fallback to building from components
            supabase_url = os.getenv("SUPABASE_DB_URL")
            supabase_password = os.getenv("SUPABASE_DB_PASSWORD")
            
            if not supabase_url or not supabase_password:
                raise ValueError("Missing Supabase credentials. Please check your .env file.")
            
            # Create PostgreSQL connection string for Supabase
            # Format: postgresql://postgres:[password]@[host]:[port]/postgres
            connection_string = f"postgresql://postgres:{supabase_password}@{supabase_url}"
        
        # Create SQL engine
        engine = create_engine(connection_string)
        
        # Execute query and create dataframe
        with engine.connect() as connection:
            sql_query_obj = text(sql_query)
            result = connection.execute(sql_query_obj)
            
            # Get column names from the result
            column_names = result.keys()
            
            # Fetch all results
            rows = result.fetchall()
            
            # Create DataFrame with proper column names
            df = pd.DataFrame(rows, columns=column_names)
            
            return sql_query, df
            
    except Exception as e:
        st.error(f"Database connection error: {str(e)}")
        return sql_query, pd.DataFrame()  # Return empty DataFrame on error
    

query = "SELECT * FROM actor"
sql, df = get_supabase_data_df(query)
st.write(sql)
st.dataframe(df)