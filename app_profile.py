#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:22:41 2025

@author: christianvdm
"""

import streamlit as st
import pandas as pd


# Set page title
st.set_page_config(page_title="Researcher Profile", layout="wide")
# Title of the app
st.title("Researcher Overview")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Research", "Publications", "Contact"],
)

name = "Mr. Christian J.T. van der Merwe"
field = "Computational Astrophysics"
institution = "University of Cape Town | South African Astronomical Observatory"
email = "christianvdm@saao.ac.za"

if menu == "Researcher Profile":
    
    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")

    st.image('./astronaut.jpg',caption='Random caption beacuase I can')

elif menu == "Research":
    st.header("Research")
    st.subheader("3D hydrodynamic simulations of white dwarf-main-sequence star collisions")

    video_file = open('./q05_dmin025_split.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.caption='Another random caption appears!'

# Add a section for publications
elif menu == "Publications":
    st.header("Publications")
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)
    
        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")
    
    # Add a section for visualizing publication trends
    st.header("Publication Trends")
    if uploaded_file:
        if "Year" in publications.columns:
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
elif menu == "Contact":
    st.header("Contact Information")
    st.write(f"You can reach {name} at {email}.")
