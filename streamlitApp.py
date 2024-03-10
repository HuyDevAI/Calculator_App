from calculate import *
import streamlit as st

def main():
    st.title("May tinh dung streamlit")
    number_a = st.number_input("Nhap so a = ",
                               min_value=0,
                               max_value=900)
    number_b = st.number_input("Nhap so b = ",
                               min_value=0,
                               max_value=900)
    if st.button("Giai Thua"):
        res = fact(number_a)
        st.write(f"{number_a}! = {res}")
    if st.button("Cong"):
        res = sum(number_a, number_b)
        st.write(f"{number_a} + {number_b} = {res}")
    if st.button("Tru"):
        res = subtract(number_a, number_b)
        st.write(f"{number_a} - {number_b} = {res}")
    if st.button("Nhan"):
        res = times(number_a, number_b)
        st.write(f"{number_a} * {number_b} = {res}")
    if st.button("Chia"):
        res = devide(number_a, number_b)
        st.write(f"{number_a} / {number_b} = {res}")
    if st.button("Luy thua"):
        res = pow(number_a, number_b)
        st.write(f"{number_a} ^ {number_b} = {res}")



if __name__ == "__main__":
    main()