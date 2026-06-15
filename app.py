import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎵 Spain Top 50 Spotify Analysis Dashboard")

df = pd.read_csv(r"C:\Users\SWATI\Desktop\Atlantic_Spain.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Top 10 Artists")

top_artists = df['artist'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(8,5))
top_artists.plot(kind='bar', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("Popularity Distribution")

fig2, ax2 = plt.subplots(figsize=(8,5))
df['popularity'].hist(ax=ax2)
st.pyplot(fig2)