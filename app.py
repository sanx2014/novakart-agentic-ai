import streamlit as st
import pandas as pd

from order_tools import get_order_details
from conversation_manager import generate_response
from escalation_engine import check_escalation
from sales_engine import recommend_product


orders = pd.read_csv("data/orders.csv")

st.title("NovaKart AI Customer Support")

order_id = st.selectbox(
    "Select Order ID",
    orders["order_id"]
)

order = get_order_details(order_id)

st.subheader("Order Details")

st.write(order)

query = st.text_input("Ask your question")

if st.button("Send"):

    response = generate_response(query, order)

    if check_escalation(query, response):

        st.error("Routing to Human Support Agent...")

    else:

        st.success(response)

        recommendation = recommend_product(query)

        if recommendation != "":
            st.info("Recommended Add-on: " + recommendation)