import streamlit as st
import datetime
import phonenumbers

st.set_page_config(page_title="Nitro Racing Colombo", page_icon="wave", layout="wide")

st.header("Event Registration Form")

today = datetime.date.today()
year = today.year
numofevents = 0

if 'count' not in st.session_state:
    st.session_state['count'] = 0

if 'enable' not in st.session_state:
    st.session_state.enable = False

def test():
    st.session_state['count'] += 1



with st.form(key='personal'):
    name = str(st.text_input("Enter Your Name", placeholder='eg: John Smith'))

    contact = st.text_input("Contact Number", placeholder='eg: +94123456789')

    dob = st.date_input(label='Date of Birth', min_value=(datetime.date(1900, 1, 1)))
    splitdate = str(dob).split('-')
    

    st.session_state['count'] = 0

    st.write("Select Events")
    st.write('*All events are subject to a split in class of A & B depending on the number of entries and timings | Truggy event might be held a common event if entry count is low*')
    st.write("Rs/: 1500 per event")
    ev1 = st.checkbox("1/10 Onroad (will be split into A / B depending on entry count and timings)")
    ev2 = st.checkbox("1/8 Nitro Buggy")
    ev3 = st.checkbox("1/8 Nitro Truggy")
    ev4 = st.checkbox("1/8 Electric Buggy")
    ev5 = st.checkbox("1/8 Electric Truggy")

    st.write('Events for under 10\'s')
    ev6 = st.checkbox("1/10 Onroad Junior (10 and Under)")
    ev7 = st.checkbox("1/8 & 1/10 Offroad Junior Open (10 and Under)")

    submit_button = st.form_submit_button('register')


    if submit_button:
        if ev1:
            st.session_state['count'] += 1
        if ev2:
            st.session_state['count'] += 1
        if ev3:
            st.session_state['count'] += 1
        if ev4:
            st.session_state['count'] += 1
        if ev5:
            st.session_state['count'] += 1
        if ev6:
            st.session_state['count'] += 1
        if ev7:
            st.session_state['count'] += 1

        st.write(st.session_state['count'])
        with st.expander("Payment Details", expanded=True):
            st.write("Bank : ")
            value = st.session_state['count'] * 1500
            st.write(value)
