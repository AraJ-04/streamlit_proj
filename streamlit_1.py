import streamlit as st

st.title("Streamlit Program")

st.header("Aryan Raj")
st.subheader("Date-19-04-25")

st.text("Hello This Is My First Streamlit Program")

st.markdown("This Is A Markdown")

st.success("Passed")
st.info("You have Passed This Is Used To Add A Inforamtion")
st.warning("This Is To Warn You")
st.error("This Is Used To Give An Error")
#exp = ZeroDivisionError("Trying to divide by Zero")
#st.exception(exp)

st.write("This Is Used To Write")
# st.write(range(10))

from PIL import Image
img = Image.open("loading-bar.png")
st.image(img, width=200)

#st.checkbox("Show/Hide")

if st.checkbox("Show/Hide"):
    st.text("This Will Show")