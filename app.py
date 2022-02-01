import streamlit as st
import random


def filter_gray(data, c):
    return [x for x in data if not c in x]


def filter_yellow(data, c, i):
    return [x for x in data if c in x and c != x[i]]


def filter_green(data, c, i):
    return [x for x in data if c == x[i]]


def filter_data(data, word, mask):
    d = data.copy()
    for i in range(5):
        if mask[i] == "_":
            d = filter_gray(d, word[i])
        elif mask[i].lower() == "o":
            d = filter_yellow(d, word[i], i)
        elif mask[i].lower() == "x":
            d = filter_green(d, word[i], i)
    return d


with open("words-5.txt") as f:
    data = f.readlines()
d1 = [x.strip() for x in data]

i1, i2, i3, i4, i5, i6 = "", "", "", "", "", ""
o1, o2, o3, o4, o5, o6 = "", "", "", "", "", ""

st.subheader("Wordle Solver für Kevin")
st.write("_ für Grau")
st.write("o für Gelb")
st.write("x für Grün")

i1 = st.text_input("Type first guess")
o1 = st.text_input("Type first feedback")

if len(i1 + o1) == 10:
    d2 = filter_data(d1, i1, o1)
    st.write("Try " + d2[0] + " or " + d2[-1])
    i2 = st.text_input("Type second guess")
    o2 = st.text_input("Type second feedback")

if len(i2 + o2) == 10:
    d3 = filter_data(d2, i2, o2)
    st.write("Try " + d3[0] + " or " + d3[-1])
    i3 = st.text_input("Type third guess")
    o3 = st.text_input("Type third feedback")

if len(i3 + o3) == 10:
    d4 = filter_data(d3, i3, o3)
    st.write("Try " + d4[0] + " or " + d4[-1])
    i4 = st.text_input("Type fourth guess")
    o4 = st.text_input("Type fourth feedback")

if len(i4 + o4) == 10:
    d5 = filter_data(d4, i4, o4)
    st.write("Try " + d5[0] + " or " + d5[-1])
    i5 = st.text_input("Type fifth guess")
    o5 = st.text_input("Type fifth feedback")

if len(i5 + o5) == 10:
    d6 = filter_data(d5, i5, o5)
    st.write("Try " + d6[0] + " or " + d6[-1])
