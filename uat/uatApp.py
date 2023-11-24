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
    
    for uat in ans:
        st.subheader("TEST: "+uat["ID"])
        st.subheader("DESCRIZIONE: "+uat["DESCRIZIONE"])
        st.subheader("PRECONDIZIONE: "+uat["PRECONDIZIONE"])
        if type(uat["ATTORI"] is list):
            s = ",".join([str(item) for item in uat["ATTORI"]])
            st.subheader("ATTORI: "+s)
        else:    
            st.subheader("ATTORI: "+uat["ATTORI"])
        table = {}
        table["Step"]=[]
        table["Input"] =[]
        table["Output"] = []
        for row in uat["TEST"]:
            table["Step"].append(row["STEP"])
            table["Input"].append(row["INPUT"])
            table["Output"].append(row["RISULTATO"])
        st.table(table)
        st.subheader("\n")

        

