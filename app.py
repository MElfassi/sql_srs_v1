import streamlit as st
import pandas as pd
import duckdb as db
import io



csv = '''
beverage,price
orange juice,2.5
Expresso,2
Tea,3
'''

beverages= pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
'''

food_items = pd.read_csv(io.StringIO(csv2))

answer = """
select * from beverages
cross join food_items
"""

solution = db.sql(answer).df()

st.write("""
#SQL SRS
Space Repetition System SQL Practicce
""")

option = st.selectbox(
    "What would you like to review",
    ["Joins", "GroupBy", "Windows Functions"],
    index=None,
    placeholder="Select a Theme"
    )
st.write('You selected: ', option)

st.header("enter your code: ")
query = st.text_area(label="votre code sql ici", key="user_input")

tab2, tab3 = st.tabs(["Tables", "Solution"])



with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution)

with tab3:
    st.write(answer)


