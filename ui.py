
import streamlit as st
st.title("HOTEL BAWARCHI")
st.title("Tip Generator")
st.title("This is a sample program")
num1=st.number_input("Enter num1",min_value=0,step=1)
num2=st.number_input("Enter num2")


if st.button("Submit"):
    st.write("Total: ",num1+num2)


bill=st.number_input("Enter bill amount :")
if bill<=1000:
    tip=(bill*2)/100
    st.write("The Tip is :",tip)
elif bill>=5000:
    tip=(bill*7)/100
    st.write("The Tip is :",tip)
else:
    tip=(bill*5)/100
    st.write("The Tip is :",tip)

dob=st.date_input("Enter dob :")




