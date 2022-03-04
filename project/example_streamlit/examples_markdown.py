import streamlit as st

"# Header 1"
"## Header 2"
"### Header3"
"---"  # This is an horizontal line
"*this is italic (one star)* and **this is bold (two stars)**"
"https://docs.streamlit.io/library/api-reference"  # Links are clickable

"""```python
print("hello")
```"""

{1: "one", 2: "two", 3: "three"}


st.markdown("---")  # for an horizontal line

st.title("Header 1 [with st.title]")
st.header("Header 2 [with st.header]")
st.subheader("Header 3 [with st.subheader]")

st.code("print('hello')")
st.json({1: "one", 2: "two", 3: "three"})