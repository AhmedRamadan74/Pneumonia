import os
import cv2
import numpy as np
import streamlit as st
from PIL import Image
import pickle

model = pickle.load(open("model.pkl", 'rb'))

#function to load image
def load_image(image_file):
	img = Image.open(image_file)
	return img

#function contant all steps of preprocossing 
def preprocosser(load_image):
    array=np.array(load_image)
    resize=cv2.resize(array,(49152,1),(49152,)) #to resize array to (49152,1)
    reshape=np.reshape(resize,(49152,)) # to reshape array to (49152,) as input in model
    norm = cv2.normalize(reshape, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)#normalize
    reshape_norm=np.reshape(norm,(1,49152))#reshape to 1-D
    return reshape_norm

#function to prediction
def prediction(image):
    pre=model.predict(image) #represtened to prediction value
    return pre[0]

def print_results(value):
    if value ==1:#represtened to prediction value
        return(f"you have pneumonia ")
    else:
        return(f"you don't have pneumonia ")

st.title("Preduction you have Pneumonia or not")
st.markdown("To get result enter chest x-ray")


image_file = st.file_uploader("Upload X-ray", type=["png","jpg","jpeg"])
if image_file is not None:
        # To show image
        img=load_image(image_file)
        st.image(img,width=250)
        reshape=preprocosser(img)
        value=prediction(reshape)
        btn=st.button("Predict")
        if btn:
            st.write(print_results(value))
