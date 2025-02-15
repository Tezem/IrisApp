import streamlit as st

#from sklearn.model_selection import train_test_split
st.sidebar.title("Menu")
st.sidebar.header("Analyse des données")
#st.sidebar.text("selectionner un des menus suivants pour continuer")
st.title("TP 1 IA ENS")
st.header("Partie 1")

#Ajout d'un message defilant
st.markdown(
    """
    <marquee behavior="scroll" direction="left" scrollamount="5">
          Bienvenue sur notre application de traitement de données !  
    </marquee>
    """,
    unsafe_allow_html=True
)

#Ajouter un élément à la page d'accueil
#st.write("Hello world !")

# Ici je vais inserer les menus interactifs dans ma barre de menu
menu = st.sidebar.radio(
    "Sélectionnez une page:", 
    ["Accueil", "Description des données", "Visualisation des données", "Interogation des données", "Contacts"]
)

# Affichage du contenu selon le choix
if menu == "Accueil":
    st.subheader("Bienvenue dans le module d'analyse des données")
    st.write("Pour effectuer une tache, retourner sur le menu correspondant")

if menu == "Description des données":
    st.subheader("Bienvenu dans le menu de description des données")
    st.write("Ici vous pouvez afficher ou calculer les caracteristiques de de dispersion des données")

elif menu == "Visualisation des données":
    st.subheader("Bienvenue dans la page de visualisation des données")
    st.write("Cette page vous offre la possibilité de faire des representations ")

elif menu == "Interogation des données":
    st.subheader("Bienvenue dans la page d'Interrogation des données")
    st.write("Je vous offre ici la possibilité d'interroger des données à votre convenancer")
    st.write("Selectionne la longueur de sepal")
    longueurSepal = st.sidebar.slider(
        "Choisissez une valeur :", 
        min_value=0, 
        max_value=20,                
        value=50, 
        step=5
    )
    st.write(f"La longueur du sepal sélectionnée : {longueurSepal}")

if menu == "Contacts":
    st.subheader("Contactez-nous:")
    st.write("Téléphone: +237 697 848 562")
    st.write("WhatsApp : +237 697 848 562")
    st.write("Email    : tezemfrederic@gmail.com")
