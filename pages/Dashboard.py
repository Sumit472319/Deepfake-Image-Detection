import streamlit as st

if "logged_in" not in st.session_state:
    st.warning("Please Login First")
    st.stop()

if not st.session_state.logged_in:
    st.warning("Please Login First")
    st.stop()
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.title("📊 Dashboard")

if os.path.exists("history.csv"):

    df = pd.read_csv("history.csv")

    total = len(df)
    real_count = len(df[df["Result"] == "Real"])
    fake_count = len(df[df["Result"] == "Fake"])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Predictions", total)

    with col2:
        st.metric("Real Images", real_count)

    with col3:
        st.metric("Fake Images", fake_count)

    st.subheader("📈 Prediction Summary")
    st.bar_chart(df["Result"].value_counts())

    st.subheader("🥧 Real vs Fake Distribution")

    fig, ax = plt.subplots()

    ax.pie(
        [real_count, fake_count],
        labels=["Real", "Fake"],
        autopct="%1.1f%%"
    )

    st.pyplot(fig)

else:
    st.warning("No data available. Upload images first.")
    st.subheader("📈 Accuracy Graph")
    st.line_chart(df["Score"])
    st.subheader("📋 Recent Predictions")
    st.dataframe(df.tail(5))    