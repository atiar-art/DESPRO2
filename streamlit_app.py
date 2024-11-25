import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta


st.set_page_config(page_title="Speed and Crowd Monitoring", page_icon="activity")

selected = option_menu(
    menu_title= "Dashboard", 
    options=["Home", "Monitoring"],
    icons=["house", "graph-up"], 
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    )

if selected == "Home":
    st.title(f"Capstone Project Group 25")
    st.write("""This website can monitor the crowds that occur at bus stops and the ethics of drivers when passing crowds at bus stops.""")
    st.subheader("⏰ Current Time (GMT+7)", divider="gray")
    place_time = st.empty()
    gmt_plus_7 = timedelta(hours=7)
    def current_time():
        return (datetime.utcnow() + gmt_plus_7).strftime("%H:%M:%S")

if selected == "Monitoring":
    st.title(f"Speed and Crowd Monitoring")
    st.subheader("⏰ Speed Monitoring", divider="gray")
    st.subheader("⏰ Crowd Monitoring", divider="gray")
    st.subheader("⏰ Crowd vs Speed Monitoring", divider="gray")
