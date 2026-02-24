import streamlit as st
import pandas as pd


whls_items = {
    "Wanga snacks": 7800,
    "balst snacks":7800,
    "tiger pipe":4000,}

st.write("mitengo ya katundu yemwe ali pa msika panopa")

for item, price in whls_items.items():
    st.write(f"nice price{item}")

df = pd.DataFrame(list(whls_items.items()),columns=["item","price(mk)"])
df["price(mk)" ].df["price(mk)"].apply(lambda x: f"mk{x:,}") 

st.table(df)
                   
