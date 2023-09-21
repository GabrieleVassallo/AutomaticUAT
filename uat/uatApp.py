import streamlit as st

import uatLogic

#Creating the web interface
st.title("AUAT")
st.subheader("Autogeneration of UAT")

uat = uatLogic.UATLogic()

user_input = st.text_area(label='Use Case:', value="", height=200)

# Send request and produce the UATs.
if st.button("Submit"):
    res =""
    markdown = True
    ans = uat.generateUAT(user_input)
    st.text(ans)

        

