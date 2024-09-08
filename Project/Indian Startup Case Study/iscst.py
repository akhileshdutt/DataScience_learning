import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("startup_funding_cleaned.csv")

#data cleaning
df["Investors"] = df["Investors"].fillna("Undisclosed")

# st.dataframe(df)
def load_investor_details(selected_investor):
    st.title(selected_investor)

    # last 5 round of investments done by the investor
    last5_rounds= df[df["Investors"].str.contains(selected_investor)].head()[["Date","Startup","Vertical","City","Round","Amount"]]
    st.subheader("Most Recent Investments")
    st.dataframe(last5_rounds)

    # biggest investments done by the investor
    biggest_investment = df[df["Investors"].str.contains(selected_investor)].groupby("Startup")["Amount"].sum().sort_values(ascending=False).head()
    st.subheader("Biggest Investments")
    fig,ax = plt.subplots()
    ax.bar(biggest_investment.index,biggest_investment.values)
    st.pyplot(fig)

st.sidebar.title("Startup Funding Analysis")

option = st.sidebar.selectbox("Select One",["Overall Analysis","Startup","Investor"])

if option == "Overall Analysis":
    st.title("Overall Analysis")

elif option == "Startup":
    st.sidebar.selectbox("Select Startup",sorted(df["Startup"].unique().tolist()))
    btn1= st.sidebar.button("startup details")
    st.title("Startup Analysis")

else:
    selected_investor = st.sidebar.selectbox("Select Investor",(set(sorted(df["Investors"].str.split(",").sum()))))
    btn2 = st.sidebar.button("investor details")
    if btn2:
        load_investor_details(selected_investor)
    # st.title("Investor Analysis")





