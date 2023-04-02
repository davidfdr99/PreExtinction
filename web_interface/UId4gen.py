# Test de StreamLit

import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
from PIL import Image



###########  Fonctions ###########

preextinction = xgb.XGBClassifier()
preextinction.load_model("/Users/Melanie/PreExtinction/model/preextinction.json")

data_df = pd.read_csv("/Users/Melanie/PreExtinction/model/mat.csv", index_col=False)
i2species_df = pd.read_csv("/Users/Melanie/PreExtinction/model/i2species.csv", index_col=False)

def make_prediction(model, i2species, df, species):
    idx = i2species.index[i2species["scientific_name"]==species]
    pred_arr = df.iloc[idx]
    return(model.predict(pred_arr))

pred = make_prediction(preextinction, i2species_df, data_df, "Conus cingulatus")






###########  Interface ###########
#st.title('PreExtinction')


logo = Image.open('/Users/Melanie/UI_HackD4gen/Logo.png')

st.image(logo)

#logo = Image.open('/Users/Melanie/Downloads/Logo.svg')

#st.image(logo)

# Introduction

st.write('As part of the **D4GEN Hackathon** held at the Genopole from March 31st to April 2nd, 2023, our team developed the **PreExtinction model**.')
st.write ('Our objective is to **predict the conservation status of unlabelled species** to provide guidance for biodiversity policies and resource allocation.')

st.write('During the Hackathon, we focused on producing a **proof of concept for the Mollusca phylum**. Mollusca is not only the largest marine phylum but also the second-largest phylum of invertebrate animals. Despite being a crucial pillar of ecosystems, the endangerment of this phylum is often neglected.')

st.write('Our fabulous team wad led by **Nicolas Godron** along with **Hugues Escoffier**, **David Fandrei** and **Mélanie Brégou**')



#Raw-data
st.subheader('Raw data')
st.write('We first created a database with different APIs : **Historical IUCN Red List of Threatened Species**, **GBIF** and **Open Meteo**.')



st.subheader('Number of species by extinction category')



classes = Image.open('/Users/Melanie/UI_HackD4gen/classes.png')
st.image(classes)

st.subheader('Des stats ?')

image = Image.open('/Users/Melanie/UI_HackD4gen/images.png')

st.image(image, caption='Graphs')



#hour_to_filter = 17
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
#st.subheader(f'Map of all pickups at {hour_to_filter}:00')
#st.map(filtered_data)

#x = st.slider('x')  
#st.write(x, 'squared is', x * x)

st.subheader('Results')


shap_summary = Image.open('/Users/Melanie/UI_HackD4gen/shap_summary.png')

st.image(shap_summary)

shap_values = Image.open('/Users/Melanie/UI_HackD4gen/shap_values.png')

st.image(shap_values)

box_var = Image.open('/Users/Melanie/UI_HackD4gen/box_var.png')

st.image(box_var)

cm = Image.open('/Users/Melanie/UI_HackD4gen/cm.png')


st.image(cm)


st.subheader('Predict Model')

st.write('Prediction of one species')



df = pd.DataFrame({
    'species with Na': ['Octopus vulgaris', '']
    })


# espece = st.selectbox(
#     'Which specie do you want to predict is extinct status of?',
#      df['species with Na'])

espece = st.text_input(label="species", value="")

'You selected: ', espece

pred = make_prediction(preextinction, i2species_df, data_df, espece)
if pred==1:
    st.write(f"The species {espece} is endangered according to our model")
elif pred==0:
    st.write(f"The species {espece} is not endangered according to our model")
else:
    st.write("No species selected")




#st.write('Des infos sur l\'espèce')




