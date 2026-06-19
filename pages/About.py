import streamlit as st

if "logged_in" not in st.session_state:
    st.warning("Please Login First")
    st.stop()

if not st.session_state.logged_in:
    st.warning("Please Login First")
    st.stop()
st.title("ℹ️ About Project")

st.write("""
This project detects whether an image is Real or Fake using Deep Learning.

Technology Used:
- Python
- TensorFlow
- Streamlit
- CNN
""")