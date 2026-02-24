import streamlit as st

whls_items = {
    "Wanga snacks": 7800,
    "balst snacks":7800,
    "tiger pipe":4000,}

st.write("mitengo ya katundu yemwe ali pa msika panopa")

for item, price in whls_items.items():
    st.write(f"nice price{item}")
