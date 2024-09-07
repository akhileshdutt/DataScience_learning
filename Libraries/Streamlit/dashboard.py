# streamlit is a library based upon react and on backend it uses python
import streamlit as st
import pandas as pd
st.title("Startup Dashboard")
st.header("I am learning streamlit")
st.subheader("I am loving it")
st.write("Barack Obama, the 44th President of the United States, was born in Honolulu, Hawaii, on August 4, 1961. He graduated from Harvard Law School and later served as a senator from Illinois. In 2009, he won the Nobel Peace Prize. Obama currently resides in Washington, D.C., with his wife, Michelle Obama. In recent years, he has focused on humanitarian work through the Obama Foundation")
st.markdown("""
### My favourite movies
    - Interstellar
    - Cars 3""")
st.code("""
        def foo(input):
            return foo**2
        
        x = foo(4)
        """)
st.latex("x^2 + y^2 + 2 = 0")

# Display Elements

df = pd.DataFrame({
    "name":["Swaym","Swarup","barik"],
    "marks":[50,60,70]
})
st.dataframe(df)

st.metric("Revenue","Rs 5L","-110%")
st.json({
    "name":["Swaym","Swarup","barik"],
    "marks":[50,60,70]
})
st.image("image.png")
# st.video()
