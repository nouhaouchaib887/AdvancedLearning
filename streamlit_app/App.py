import streamlit as st 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import os
from utils import display_multiple_images, plot_train_data_distribution, display_multiple_images_2, evaluation_weighted, evaluation_macro, matrice_confusion, report_to_df, training_plots_accuracy, training_plots_loss, classification_rapport

import warnings


# Ignorer tous les avertissements
warnings.filterwarnings('ignore')
data = "streamlit_app/Resultas/data_evaluation.csv"
data = pd.read_csv(data)
training = "streamlit_app/Resultas/training.csv"
history = pd.read_csv(training)
data_tl =  "streamlit_app/Resultas/data_evaluation1.csv"
data_tl = pd.read_csv(data_tl)
training_tl = "streamlit_app/Resultas/training1.csv"
history_tl = pd.read_csv(training_tl)
data_ssl = "streamlit_app/Resultas/data_evaluation2.csv"
data_ssl = pd.read_csv(data_ssl)
training_ssl = "streamlit_app/Resultas/training2.csv"
history_ssl =  pd.read_csv(training_ssl)
resultats = {"Supervised learning": {"data": data , "training": history}, "Transfer learning": {"data": data_tl , "training": history_tl}, "Self-supervised learning": {"data": data_ssl , "training": history_ssl}}
st.sidebar.title("Sommaire")

pages = ["Introduction", "Paradigmes d'apprentissage","Préparation des données","Modélisation","Résultats", "Conclusion"]
page = st.sidebar.radio("Allez vers la page", pages)
if page == pages[0]:
    st.write(" # Detection des Emotions")
    st.write("")
    st.write("")
    st.write("La détection des émotions via la vision par ordinateur est un champ prometteur de l'intelligence artificielle qui promet de transformer des secteurs variés, tels que la sécurité, la santé, et le marketing, en donnant aux machines la capacité de lire et de réagir aux émotions humaines à partir d'images et de vidéos. Cette technologie peut améliorer l'interaction homme-machine et personnaliser les services, par exemple en ajustant automatiquement les réponses des agents de service client selon l'état émotionnel des utilisateurs.")
    st.write("")
    st.write("Cependant, la détection des émotions est entravée par des défis significatifs tels que la grande variabilité des expressions émotionnelles au sein d'un même individu et les variations culturelles qui peuvent altérer la précision à travers les populations. Ces obstacles rendent difficile la généralisation des systèmes de vision par ordinateur basés sur des ensembles de données limités.")
    st.write("")
    st.write("En réponse à ces défis, notre projet se concentre sur l'évaluation de l'impact des différents paradigmes d'apprentissage—supervisé, auto-supervisé, et par transfert—sur la robustesse et les performances des modèles de détection des émotions. En optimisant les techniques d'apprentissage profond et les architectures neuronales, nous visons à améliorer la précision et la fiabilité de ces systèmes dans des conditions diverses.")
    
if page == pages[1]:
    st.write("# Paradigmes d'apprentissage en AI")
    st.write("")
    st.write("  \n\n\n L'intelligence artificielle (IA) se distingue par une multitude d'approches d'apprentissage, chacune répondant à des défis spécifiques et exploitant diverses sources de données. Cette diversité est essentielle pour progresser dans un domaine aussi complexe que l'IA, permettant une adaptation et une innovation continues.")
    st.write("Pour développer notre système de détection des émotions, nous envisageons d'utiliser les méthodes d'apprentissage suivantes :")

    st.write(" ### Apprentissage supervisé (Supervised Learning) ")
    st.write("Cette approche utilise un ensemble de données étiqueté comprenant des images représentant diverses émotions telles que la tristesse, la joie, la colère, la surprise, le dégoût, la peur et la neutralité. Nous construirons un modèle CNN qui sera entraîné sur ce jeu de données pour identifier et classer ces expressions émotionnelles.")
    st.write(" ### Apprentissage par transfert (Transfer Learning)")
    st.write("Nous utiliserons le modèle pré-entraîné DenseNet169, initialement entraîné sur le dataset ImageNet, une riche collection d'images couvrant un large éventail de catégories. Cela nous permet de capitaliser sur les caractéristiques de base extraites par ce modèle pour améliorer la généralisation sur notre tâche spécifique. Le fine-tuning sera ensuite appliqué pour ajuster le modèle à notre domaine particulier de détection des émotions.")
    st.write(" ### Auto-apprentissage (Self-supervised Learning)")
    st.write("Dans cette méthode, nous développerons un modèle en définissant une tâche prétexte qui l'encourage à apprendre des caractéristiques faciales utiles en utilisant une base de données extensive telle que WikiFace, qui contient de nombreuses images de visages variés. Les caractéristiques apprises seront ensuite transférées à notre modèle de classification finale, améliorant ainsi sa capacité à reconnaître les émotions avec précision.")
if page == pages[2]:
    st.write("## Visualisations des données d'Entrainement")
    st.write("Pour notre tâche finale, nous disposons d'un dataset contenant différentes images classées selon les émotions qu'elles représentent.")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    fig = display_multiple_images()
    st.pyplot(fig)
    st.write("### Distribution des données")
    fig2 = plot_train_data_distribution()
    st.plotly_chart(fig2)
    st.write("## Visualisations des données du Pré-entrainement")
    st.write("Dans le cadre de notre projet de détection des émotions, nous avons choisi de travailler avec le dataset WIKIFace, principalement en raison de sa pertinence directe pour notre tâche finale. Le dataset WIKIFace est particulièrement riche en images de visages variés, capturant un large éventail d'expressions faciales.")
    fig3 = display_multiple_images_2()
    st.pyplot(fig3)
if page == pages[3]:
    st.write("## Modélisation")
    Learning_approach = st.selectbox (label = "Approche", options = ["Supervised learning", "Transfer learning", "Self-supervised learning"])
    if Learning_approach =="Supervised learning":
        st.image("streamlit_app/image/supervised_learning.png")
    elif Learning_approach == "Transfer learning":
        st.image("streamlit_app/image/Transfert learning.png")
    else:
        st.image("streamlit_app/image/Self supervised learning.png")

    History = resultats[Learning_approach]["training"]
    Data = resultats[Learning_approach]["data"]
    fig4 = training_plots_accuracy(History)
    st.plotly_chart(fig4)
    fig41 = training_plots_loss(History)
    st.plotly_chart(fig41)
    st.write("### Évaluation Équilibrée : Analyse des Performances par Macro-Moyenne")
    for key , value in evaluation_macro(Data).items():
        st.write(f'{key}: {value}')
    st.write("### Performances Pondérées en Fonction de la Fréquence des Classes")
    for key , value in evaluation_weighted(Data).items():
        st.write(f'{key}: {value}')
    fig5 = matrice_confusion(Data)
    st.plotly_chart(fig5)
    report = classification_rapport(Data)
    st.write("report")
    df = report_to_df(report)
    df = df.set_index("Class")
    
    st.table(df)
if page == pages[4]:

    st.write("## Résultats")
    st.write("##### Évaluation Équilibrée : Analyse des Performances par Macro-Moyenne")
    st.image("streamlit_app/image/result1.png")
    st.write("##### Performances Pondérées en Fonction de la Fréquence des Classes")
    st.image("streamlit_app/image/result2.png")
if page == pages[5]:
    st.write("## Conclusion")
    st.write("Dans notre tentative de construire un système de détection des émotions à travers différentes approches, nous avons observé des performances légèrement différentes entre les méthodes. Cependant, il est apparu que l'utilisation de l'apprentissage auto-supervisé(Self supervised learning), en particulier avec une tâche de prétexte consistant à détecter la rotation sur un dataset de 100 000 images de visages, permet d'améliorer les performances du modèle.")
    st.write("Pour poursuivre l'amélioration de ce système, des stratégies telles que l'augmentation des données et le développement d'un modèle plus volumineux avec davantage de paramètres pourraient être envisagées. Cependant, ces approches nécessitent des investissements substantiels en termes de ressources et de temps, ce qui peut représenter un défi logistique et financier.")


    
