import diamond_analysis as da
import streamlit as st

# TODO: don't hardcode the data
data = [ 1547.0363321799307, 1596.311451495259, 1696.0653524748232, 1721.8043047669353, 1919.747154588676, 1807.5567362428842, 1903.0045837917125, ]

st.bar_chart(data)

col1, col2 = st.columns(2)

with col1:
    st.slider("Carats", min_value=0.0, max_value=5.02, value=(0.0, 1.0))
with col2:
    st.selectbox("Group", ["cut", "color", "clarity"])
