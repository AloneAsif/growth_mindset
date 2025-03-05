import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="Data Sweeper", layout="wide")
st.title("Data Sweeper")
st.write("Transform your files between CSV and Excel")

uploaded_files = st.file_uploader("Upload your file (CSV or Excel)", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read file based on extension
        try:
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file, engine="openpyxl")
            else:
                st.warning(f"Unsupported file format: {file.name}")
                continue
        except Exception as e:
            st.error(f"Error reading {file.name}: {e}")
            continue

        # File size calculation (for BytesIO objects)
        file.seek(0, os.SEEK_END)
        file_size_kb = file.tell() / 1024
        file.seek(0)  # Reset file pointer after size calculation

        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file_size_kb:.2f} KB")

        st.write("### Preview (first 5 rows)")
        st.dataframe(df.head())

        # st.subheader("Data Cleaning Options")
        # if st.checkbox(f"Clean data for {file.name}"):
        #     col1, col2 = st.columns(2)
            
        #     with col1:
        #         if st.button(f"Remove duplicates from {file.name}"):
        #             df.drop_duplicates(inplace=True)
        #             st.write("✅ Duplicates removed")
            
        #     with col2:
        #         if st.button(f"Fill missing values in {file.name}"):
        #             numeric_cols = df.select_dtypes(include=['number']).columns
        #             df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        #             st.write("✅ Missing values filled with column mean")

        #     st.subheader("Select Columns to Convert")
        #     columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        #     df = df[columns]

        # st.subheader("Data Visualization")
        # if st.checkbox(f"Show visualization for {file.name}"):
        #     numeric_df = df.select_dtypes(include='number')
        #     if not numeric_df.empty:
        #         st.bar_chart(numeric_df.iloc[:, :2])  # Show first 2 numeric columns
        #     else:
        #         st.warning("No numeric data available for visualization.")
