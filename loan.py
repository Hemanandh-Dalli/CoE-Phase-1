import streamlit as st
st.title("Sudheer Babu EMI Calculator")
loan_amount=st.number_input("Enter loan amount :")
interest_rate=st.slider("Interest Rate :",1,40)
duration=st.number_input("Enter duration in terms of months:")
if st.button("Calculate"):
    intr=loan_amount*interest_rate/100
    emi=(intr+loan_amount)/duration
    st.success(f"The Interest Amount is : {intr}")
    st.success(f"EMI is : {emi}")
st.radio("Select your option :",["Monthly","Daily"])
st.selectbox("Select your option :",["Monthly","Daily"])