import streamlit as st
import math

# Title of the app
st.title('Trading Success Probability Calculator')

# Getting user input for success probability and confidence level
success_probability = st.number_input('Enter your success probability (e.g., 0.40 for 40%):', min_value=0.0, max_value=1.0, value=0.40)
confidence_level = st.number_input('Enter your desired confidence level (e.g., 0.95 for 95%):', min_value=0.0, max_value=1.0, value=0.95)

# Calculate the required number of trades (k)
if st.button('Calculate Number of Trades'):
    k = math.ceil(math.log(1 - confidence_level) / math.log(1 - success_probability))
    st.write(f"Number of trades required to be {confidence_level*100}% confident of at least one success: {k}")
