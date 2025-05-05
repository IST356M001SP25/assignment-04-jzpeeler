'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

# TODO Write code here to complete the unibrow.py
file = st.file_uploader("Upload a CSV, Excel, or JSON file", type=['csv', 'xlsx', 'json'])

def load_file(file, ext):
    if ext == 'csv':
        return pd.read_csv(file)
    elif ext == 'xlsx':
        return pd.read_excel(file)
    elif ext == 'json':
        return pd.read_json(file)
    else:
        raise ValueError("Unsupported file type")
    
if file:
    ext = file.name.split('.')[-1].lower()
    df = load_file(file, ext)
    st.subheader("Raw Data")
    st.write(df)


    selected_columns = st.multiselect("Select Columns to display", options=df.columns.tolist(), default=list(df.columns))
    df_filtered = df[selected_columns]

    if st.toggle("Add a filter"):
        object_columns = df.select_dtypes(include='object').columns.tolist()
        if object_columns:
            filter_column = st.selectbox("Select a column to filter", options=object_columns)
            unique_values = df[filter_column].unique().tolist()
            selected_value = st.selectbox("Select a value to filter on", options=unique_values)
            df_filtered = df_filtered[df[filter_column] == selected_value]
        else:
            st.warning("No object columns available for filtering")
    st.subheader("Filtered Data")
    st.dataframe(df_filtered)

    # --- Describe Statistics ---
    st.subheader("Descriptive Statistics")
    st.write(df_filtered.describe(include='all'))


