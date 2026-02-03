import streamlit as st
import pandas as pd


name = st.text_input("student Name: ")
std = st.text_input("student in std: ")
st.subheader("Enter subject scores")
subjects = { "maths":st.number_input("maths",min_value=0,max_value=100,value=0, step=1),
           "English":st.number_input("English",min_value=0,max_value=100),
           "chichewa":st.number_input("chichewa",min_value=0,max_value=100),
           "B/K":st.number_input("B/K",min_value=0,max_value=100),
           "expressive arts":st.number_input("Expressive Arts",min_value=0,max_value=100),
           "social":st.number_input("social",min_value=0,max_value=100),
           "Agriculture":st.number_input("Agriculture",min_value=0,max_value=100),
           "life skills":st.number_input("life skills",min_value=0,max_value=100),
           "science":st.number_input("science",min_value=0,max_value=100),}

if st.button("Generate Report"):
  total = sum(subjects.values())
  st.subheader("student report")
  report = f"PUPIL'S NAME: {name}\n"
  report += f"std : {std}\n"
  report +="2026 Academic year\n\n"
  
  for subject, score in subjects.items():
        report += f"{subject:10} : {score}\n"
  report += f"Total:{total}\n"
  if total >= 350:
    report += "pass\n"
    report +="Grade 4\n" 
  else:
    report += "Fail\n"
    report +="try a gain next term\n"

  st.write(report)
  st.download_button(label="Download school report",data=report , file_name=f"{name}_report.txt",mime="text/plain") 