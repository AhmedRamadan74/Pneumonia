import os
import cv2
import numpy as np
import streamlit as st
from PIL import Image
import pickle
import os
os.chdir(r"/mount/src/pneumonia/Streamlit")
import _pickle as cPickle
with open('model.pkl', "rb") as input_file:
    model = cPickle.load(input_file)
#model = pickle.load(open("model.pkl", "rb"))


# function to load image
def load_image(image_file):
    img = Image.open(image_file)
    return img


# function contant all steps of preprocossing
def preprocosser(load_image):
    array = np.array(load_image)
    resize = cv2.resize(array, (49152, 1), (49152,))  # to resize array to (49152,1)
    reshape = np.reshape(
        resize, (49152,)
    )  # to reshape array to (49152,) as input in model
    norm = cv2.normalize(
        reshape, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F
    )  # normalize
    reshape_norm = np.reshape(norm, (1, 49152))  # reshape to 1-D
    return reshape_norm


# function to prediction
def prediction(image):
    pre = model.predict(image)  # represtened to prediction value
    return pre[0]


# function to prediction
def prediction_pro(image):
    pre = model.predict_proba(image)  # represtened to prediction value
    return pre[0][0]


def print_results(value):
    if value == 1:  # represtened to prediction value
        return f"you have pneumonia "
    else:
        return f"you don't have pneumonia "


# layout
row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns(
    (0.1, 2.3, 0.1, 1.3, 0.1)
)

with row0_1:
    st.title("Pneumonia")
    st.markdown(
        """ <h6>
                    This app is created to detection if you have Pneumonia or not </center> </h6> """,
        unsafe_allow_html=True,
    )

st.markdown("To get result enter chest x-ray")


image_file = st.file_uploader("Upload X-ray", type=["png", "jpg", "jpeg"])
if image_file is not None:
    # To show image
    img = load_image(image_file)
    st.image(img, width=250)
    reshape = preprocosser(img)
    value = prediction(reshape)
    prod = prediction_pro(reshape)
    btn = st.button("Predict")
    if btn:
        # st.write(print_results(value))
        # st.write(f'{100 - round(prod * 100, 2)}')
        if value == 1:
            st.write(
                f"{print_results(value)} with percentage {100 - round(prod * 100, 2)} %"
            )
        else:
            st.write(f"{print_results(value)} with percentage {round(prod * 100, 2)} %")
