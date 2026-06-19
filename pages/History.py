import streamlit as st
import pandas as pd
import os

if "logged_in" not in st.session_state:
    st.warning("Please Login First")
    st.stop()

if not st.session_state.logged_in:
    st.warning("Please Login First")
    st.stop()

st.title("📜 Detection History")

if os.path.exists("history.csv"):

    df = pd.read_csv("history.csv")

    # Current User History Only
    user_df = df[
        df["Username"] == st.session_state.username
    ]

    st.subheader(
        f"History of {st.session_state.username}"
    )

    st.dataframe(
        user_df,
        use_container_width=True
    )

    csv = user_df.to_csv(index=False)

    st.download_button(
        "⬇ Download My History",
        csv,
        f"{st.session_state.username}_history.csv",
        "text/csv"
    )

else:
    st.warning("No History Available")