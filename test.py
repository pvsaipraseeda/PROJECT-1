import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("test.csv")
st.dataframe(df.head(10))
#sample metric
st.subheader("sample metric ")
st.metric("Accuracy", value=0.85, delta=-0.05)

sample_code = """
def calculate_accuracy(predictions, actual):
    correct = sum(1 for p, a in zip(predictions, actual) if p == a)
    return correct / len(actual)
"""
st.code(sample_code, language="python")

data=pd.DataFrame(np.random.randn(10, 2), columns=['Column 1', 'Column 2'])
st.line_chart(data)
st.bar_chart(data)
st.area_chart(data)