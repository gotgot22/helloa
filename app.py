import streamlit as st

# ชื่อแอปพลิเคชัน
st.title("AI Project App")
st.text_input("HELP.txt")

# คำอธิบายของแอป
st.write("This is a simple Streamlit app for the AI project.")

# ส่วนอื่น ๆ ของแอป (Input, Display, Graphs, ฯลฯ)
user_input = st.text_input("Enter something:")
st.write(f"You entered: {user_input}")
