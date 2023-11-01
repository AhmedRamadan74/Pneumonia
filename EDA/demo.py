import streamlit as st
import pickle 
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
import plotly.express as px
import os
# read data
death=pd.read_csv(os.path.join(os.getcwd(),"death.csv"))
risk=pd.read_csv(os.path.join(os.getcwd(),"risk.csv"))
lower_respiratory_diseases=pd.read_csv(os.path.join(os.getcwd(),"lower_respiratory_diseases.csv"))
gdp=pd.read_csv(os.path.join(os.getcwd(),"gdp.csv"))
breastfeeding=pd.read_csv(os.path.join(os.getcwd(),"breastfeeding.csv"))
careseeking=pd.read_csv(os.path.join(os.getcwd(),"careseeking.csv"))
vaccine=pd.read_csv(os.path.join(os.getcwd(),"vaccine.csv"))

#######################################################
#layout 

st.set_page_config(page_title="Pneumonia",layout="wide")
st.title("Exploratory Analysis of Pneumonia, By [Ahmed Ramadan](https://www.linkedin.com/in/ahmed-ramadan-18b873230/)")

st.header("Some inforamtion of Pneumonia : ")
st.markdown("Pneumonia is an infection that inflames the air sacs in one or both lungs.The air sacs may fill with fluid,causing cough with phlegm or pus, fever, chills, and difficulty breathing.")
st.markdown("Pneumonia can range in seriousness from mild to life-threatening. It is most serious for infants and young children, people older than age 65, and people with health problems or weakened immune systems")

