import streamlit as st
from helper import generate_approach

st.set_page_config(
    page_title = "DSA Saathi AI"
)
st.title("DSA Saathi AI")
st.write("Get help with your DSA problems using AI. Just enter your problem statement and get a solution.")
prob_statement = st.text_area("Enter your problem statement here:", height = 300)

if st.button("Get Approach"):
    if prob_statement.strip() == "":
        st.warning("Please enter a problem statement.")
    else:
        with st.spinner("Generating approach..."):
            result = generate_approach(prob_statement)
        # Here you would typically call your AI model to generate the approach based on the problem statement.
        # For demonstration purposes, we'll just display a placeholder message.
        st.success("Approach generated successfully!")
        st.markdown(f"Here is a sample approach to solve your DSA problem: {result}")
if st.button("Get Code"):
    if prob_statement.strip() == "":
        st.warning("Please enter a problem statement.")
    else:
        with st.spinner("Generating code..."):
            result = "def two_pointer_solution():\n    # Your code here"
        # Here you would typically call your AI model to generate the code based on the problem statement.
        # For demonstration purposes, we'll just display a placeholder message.
        st.success("Code generated successfully!")
        st.code(result, language='python')
