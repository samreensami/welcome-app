import streamlit as st 

# Page title
st.title("🎉 Welcome 🎉")
st.header("🐍 to the SAM SAMI Python Journey! 🐍")
st.info("**Lead Teacher** : **HAMZAH SYED**")
st.success("🚀 Congratulations... 🚀")

# Welcome message
st.write("Congratulations on reaching Quarter 3! Keep up the great learning. 🚀")
st.warning("Never give up! Keep learning and practicing. 🚀")

# User interactions
feeling = st.select_slider("How are you feeling today?", options=["Bad", "Good", "Excellent"])
study_hours = st.slider("How many hours did you study today?", min_value=0, max_value=10, value=5)
name = st.text_input("What is your name?")
like = st.checkbox("Like")
favorite_color = st.radio("What is your favorite color?", options=["Red", "Blue", "Green"])

# Sidebar
st.sidebar.button("Click me!")
email = st.sidebar.text_input("Enter your email")

# Show balloons 🎈
st.balloons()
