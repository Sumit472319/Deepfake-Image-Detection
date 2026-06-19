import streamlit as st
import sqlite3

# DATABASE

conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT PRIMARY KEY,
    password TEXT,
    email TEXT
)
""")
conn.commit()

# PAGE CONFIG

st.set_page_config(
    page_title="Deepfake Detection System",
    page_icon="🔍",
    layout="wide"
)

# SESSION

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# LOGIN PAGE

if not st.session_state.logged_in:

    st.title("🔐 Deepfake Detection Login")

    menu = ["Sign Up", "Login", "Forgot Password"]
    choice = st.sidebar.selectbox("Menu", menu)

    # LOGIN

    if choice == "Login":

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            c.execute(
                "SELECT * FROM users WHERE username=? AND password=?",
                (username, password)
            )

            user = c.fetchone()

            if user:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login Successful")
                st.rerun()

            else:
                st.error("Invalid Username or Password")

    # SIGN UP

    elif choice == "Sign Up":

        new_user = st.text_input("Create Username")
        new_email = st.text_input("Email")
        new_pass = st.text_input("Create Password", type="password")

        if st.button("Create Account"):

            try:

                c.execute(
                    "INSERT INTO users VALUES (?,?,?)",
                    (new_user, new_pass, new_email)
                )

                conn.commit()

                st.success("Account Created Successfully")
                st.info("Now Login")

            except:
                st.error("Username Already Exists")

    # FORGOT PASSWORD

    elif choice == "Forgot Password":

        username = st.text_input("Username")
        email = st.text_input("Email")

        if st.button("Verify"):

            c.execute(
                "SELECT * FROM users WHERE username=? AND email=?",
                (username, email)
            )

            user = c.fetchone()

            if user:

                st.success("Verified Successfully")

                new_password = st.text_input(
                    "New Password",
                    type="password"
                )

                confirm_password = st.text_input(
                    "Confirm Password",
                    type="password"
                )

                if st.button("Reset Password"):

                    if new_password == confirm_password:

                        c.execute(
                            "UPDATE users SET password=? WHERE username=?",
                            (new_password, username)
                        )

                        conn.commit()

                        st.success("Password Updated Successfully")

                    else:
                        st.error("Passwords Do Not Match")

            else:
                st.error("Invalid Username or Email")

# HOME PAGE

else:

    st.sidebar.success(f"👤 {st.session_state.username}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    st.image("logo.png", width=150)

    st.title("🔍 Deepfake Detection System")

    st.markdown(f"""
## Welcome {st.session_state.username} 👋

This AI-powered application helps detect whether an uploaded image is **Real** or **Fake (Deepfake)** using a trained Deep Learning model.

### 🎯 Project Objectives
- Detect manipulated images
- Improve digital media authenticity
- Provide quick AI-based analysis
- Generate downloadable reports

### 🚀 Key Features
✅ Real/Fake Image Detection

📊 Dashboard Analytics

📜 Detection History

📄 PDF Report Generation

🔐 Login & Forgot Password

### 🛠 Technologies Used
- Python
- TensorFlow / Keras
- Streamlit
- NumPy
- Pandas

### 📌 How to Use

1. Open Detection Page
2. Upload an Image
3. View Prediction
4. Download Report
5. Check History
""")