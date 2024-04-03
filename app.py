import streamlit as st
import pandas as pd
import duckdb as db

st.write("Hello world")

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.dataframe(df)
    query = st.text_area(label="Entrez votre requete")
    st.write(f" Voici la requete entré: {query}")
    query_result = db.query(query).df()
    st.write(query_result)

# st.header("A Cat")
# st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("A Dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("A Owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
