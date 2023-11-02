import streamlit as st
import pickle 
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
import plotly.express as px
import os
from PIL import Image

# read data
death=pd.read_csv(os.path.join(os.getcwd(),"EDA/death.csv"))
risk=pd.read_csv(os.path.join(os.getcwd(),"EDA/risk.csv"))
lower_respiratory_diseases=pd.read_csv(os.path.join(os.getcwd(),"EDA/lower_respiratory_diseases.csv"))
gdp=pd.read_csv(os.path.join(os.getcwd(),"EDA/gdp.csv"))
breastfeeding=pd.read_csv(os.path.join(os.getcwd(),"EDA/breastfeeding.csv"))
careseeking=pd.read_csv(os.path.join(os.getcwd(),"EDA/careseeking.csv"))
vaccine=pd.read_csv(os.path.join(os.getcwd(),"EDA/vaccine.csv"))

#######################################################
#layout 

st.set_page_config(page_title="Pneumonia",layout="wide")
st.title("Exploratory Analysis of Pneumonia, By [Ahmed Ramadan](https://www.linkedin.com/in/ahmed-ramadan-18b873230/)")

st.header("Some inforamtion of Pneumonia : ")
image = Image.open(os.path.join(os.getcwd(),"EDA/_تنزيل.jpeg")
st.image(image, caption='Pneumonia')
st.markdown("Pneumonia is an infection that inflames the air sacs in one or both lungs.The air sacs may fill with fluid,causing cough with phlegm or pus, fever, chills, and difficulty breathing.")
st.markdown("Pneumonia can range in seriousness from mild to life-threatening. It is most serious for infants and young children, people older than age 65, and people with health problems or weakened immune systems")

st.markdown("-"*50)
st.subheader("I worked in dataset related Pneumonia to Exploratory Analysis for this dataset and get some important information like risk factors , rate of death from this disease  for some countries,etl.")
st.markdown("To show how i worked , understand and clean data press Github.")
st.markdown("[Github](https://github.com/AhmedRamadan74/Pneumonia/tree/main)")
st.markdown("[Link of dataset](https://www.kaggle.com/datasets/programmerrdai/pneumonia)")
st.header("Let's explore !!")
st.markdown("The data i worked on it have about 228 countries. ")
st.markdown(f"I will show EDA In two phases, First phase is EDA of all countries together, second phase is EDA for all countries Separately.")
#####################################################################
# visualztion
col1,col2=st.columns(2)
death_descending=death.groupby("Entity")[["rate_death_under_5",
                            "rate_death_under_5-14_years",
                            "rate_death_aged_15-49_years",
                            "rate_death_aged_50-69_years",
                            "rate_death_aged_70+_years",
                            "rate_death_each_all_age"]].mean().reset_index().sort_values(by="rate_death_each_all_age",ascending=False)
death_descending.index=range(len(death_descending.index)) #to reset rank of index from 0 : len(index)

with col1:
    # top 10 country have higer rate of death
    #pandas
    df=death_descending.head(10)
    # Convert the DataFrame from wide to long format
    df_melt = df.melt(id_vars='Entity', var_name='age', value_name='rate')
    # Create the grouped bar chart
    fig = px.bar(df_melt, x='Entity', y='rate', color='age', barmode='group',text_auto="0.2s",
                width=1250,
                height=600,
                labels={"Entity":"Countries"})
    # Show the plot
    fig.update_traces(textfont_size=12,textposition="outside")
    fig.update_layout(title_text="Top 10 country have higer rate of death",title_x=0.3)
    st.plotly_chart(fig)
    st.markdown("- The highest death rate is for those over the age of __70__ and then for those __under 5__ years of age")
    st.markdown("- The country has the highest death rate for people under 5 years old is __[Niger](https://en.wikipedia.org/wiki/Niger)__ ")
    st.markdown("- The country has the highest death rate for people between 5-14 years old is __[Guinea](https://en.wikipedia.org/wiki/Guinea)__ ")
    st.markdown("- The country has the highest death rate for people between 15-49 years old is __[Solomon Islands](https://en.wikipedia.org/wiki/Solomon_Islands)__	 ")
    st.markdown("- The country has the highest death rate for people between 50-69 years old is __[Solomon Islands](https://en.wikipedia.org/wiki/Solomon_Islands)__ ")
    st.markdown("- The country has the highest death rate for people 70+ years old is __[Guinea-Bissau](https://en.wikipedia.org/wiki/Guinea-Bissau)__ ")
    st.markdown("- The country with the highest death rate is __[Solomon Islands](https://en.wikipedia.org/wiki/Solomon_Islands)__")
    
