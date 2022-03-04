import streamlit as st

st.title("My App")

name = st.sidebar.radio("Pick a name", ["Jeff", "Jenny", "Jack"])

"---"

col1, col2, col3 = st.columns(3)

col1.write("This is French")
col1.image("https://upload.wikimedia.org/wikipedia/commons/e/e7/BAN_19_LOGO_SOCIAL_ROUGE.png")

col2.write("This is Chinese")
col2.image("https://upload.wikimedia.org/wikipedia/commons/1/1c/HSK-logo.jpg")

col3.write("This is Kazakh")
col3.image("https://upload.wikimedia.org/wikipedia/commons/9/94/Logo_nl_c_small.jpg")

"---"

with st.expander("See a big picture"):
    st.write("This is a Scarlet darter (Crocothemis erythraea) female, near Rila Monastery, Bulgaria.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/8/81/Scarlet_darter_%28Crocothemis_erythraea%29_female_Bulgaria.jpg")

