---
title: "PreExtinction"
description: "D4GEN Hackathon project"

--- 

### Introduction


As part of the D4GEN Hackathon held at the Genopole from March 31st to April 2nd, 2023, our team developed the PreExtinction model.

Our objective is to predict the conservation status of unlabelled species to provide guidance for biodiversity policies and resource allocation.

During the Hackathon, we focused on producing a proof of concept for the Mollusca phylum. Mollusca is not only the largest marine phylum but also the second-largest phylum of invertebrate animals. Despite being a crucial pillar of ecosystems, the endangerment of this phylum is often neglected.


### Objective

The objective of the project was to create a database and a Machine Learning model with multile APIs to predict the endangerment of species. Our Minimum Viable Product predicts in two classes 'least concern' and 'endangered' unlabelled species of the Mollusca phylum.
The 'endangered' category merges all non 'least concern' labels.



### Processing

We merged the GBIF and IUCN data based on species name. Only species with at least one conservation status were kept. This resulted in the number of species going from 8760 to 4133.

For each timepoint with available year and location (longitude and latitude), we queried the Open Meteo API to retrieve meteorological data and sum it up in a yearly fashion. These yearly statistics avoid having seasonality-based bias.

### Model

The used data are the median of all timepoints for continuous data and the last timepoint for categorical data.
After necessary filters and normalization methods, we used XGBoost, a gradient boosting model based on decision trees.

### Results 

We obtained satisfactory results with accuracy and recall metrics approaching 80%.

### Team

Our fabulous team wad led by Nicolas Godron along with Hugues Escoffier, David Fandrei and Mélanie Brégou.

# Principal contributions 
Nicolas Godron : Project lead and GBIF database
Hugues Escoffier : IUCN database and presentation material 
David Fandrei : Model
Mélanie Brégou : Open meteo databse and Graphical interface