import streamlit as st
from PIL import Image

# ========================
# Configurations de la page
# ========================
st.set_page_config(page_title="Portfolio - Soufiane Rabhiui", page_icon=":bar_chart:", layout="wide")

# ========================
# Barre latérale
# ========================
# ---- Barre latérale ----
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Sommaire",
    ["Accueil", "MON CV", "Mes Projets", "Contact"]
)


# ========================
# Page d'accueil
# ========================
if page == "Accueil":
    st.title("Portfolio de Soufiane RABHIUI")
    st.write(" ")
    st.write("✨ Les données sont des ressources précieuses pour une entreprise, et c'est l'analyse qui transforme cette richesse en moteur de décision.✨")
    st.write("Passionné par l'exploitation des données pour éclairer et optimiser la prise de décision, je possède une expertise technique en SQL, Python (Pandas, NumPy) et Power BI, ainsi qu'une solide expérience dans la création de tableaux de bord interactifs et l'automatisation des analyses.")
    st.write("Mon objectif est de traduire des données complexes en insights clairs et actionnables, alignés sur les besoins stratégiques des entreprises pour maximiser leur impact et leur efficacité.")
    st.write("Motivé par l'apprentissage continu, je suis déterminé à appliquer mes connaissances en analyse de données et visualisation pour contribuer efficacement à des projets dans un environnement professionnel stimulant.")
    
    accueil_image = Image.open("Data-Analytics.jpg")
    col1, col2, col3 = st.columns([1, 2, 1])  # Colonnes pour centrer
    with col2:
        st.image(accueil_image, use_container_width=True)

    st.write("---")

    st.header("Compétences Techniques et Méthodologiques")
    
    # Section des compétences en colonnes
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Langages et outils")
        st.write("- Python, SQL, HTML, CSS, DAX, Git")
        st.write("- Analyse et visualisation : Pandas, Numpy, Matplotlib, Seaborn, Plotly, Streamlit")
        st.write("- Machine Learning : Scikit-learn, NLP, clustering, régressions, classification")
        st.write("- Géodonnées et cartes : Folium, géocodage")

    with col2:
        st.subheader("Données et automatisation")
        st.write("- Web scraping : BeautifulSoup, Scrapy")
        st.write("- Intégration via API REST")
        st.write("- Nettoyage et transformation des données")
        st.write("- Visualisation et reporting : Tableaux de bord Power BI, rapports automatisés avec Excel")

    # Séparateur
    st.write("---")

    st.header("Outils et technologies utilisés")
    st.markdown("""
    <div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" alt="Python" width="50" height="50" />
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/azuresqldatabase/azuresqldatabase-original.svg" alt="Azure SQL Database" width="50" height="50" />
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original-wordmark.svg" alt="Pandas" width="50" height="50" />
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/matplotlib/matplotlib-original-wordmark.svg" alt="Matplotlib" width="50" height="50" />
    <img src="https://user-images.githubusercontent.com/315810/92254613-279c8000-ee9f-11ea-9b73-5622a7d95f3f.png" alt="Description de l'icône" width="50" height="50" />
    <img src="https://github.com/devicons/devicon/blob/master/icons/plotly/plotly-original-wordmark.svg" alt="Plotly" width="50" height="50" />
    <img src="https://upload.wikimedia.org/wikipedia/fr/6/62/MySQL.svg" alt="MySQL" width="50" height="50" />
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg" alt="scikit-learn" width="50" height="50" />
    <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" width="50" height="50" />
    <img src="https://github.com/microsoft/PowerBI-Icons/raw/main/PNG/Power-BI.png" alt="Power BI" width="38" height="38" />
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/streamlit/streamlit-original-wordmark.svg" alt="Streamlit" width="50" height="50" />
    <img src="https://upload.wikimedia.org/wikipedia/commons/9/9a/Visual_Studio_Code_1.35_icon.svg" alt="Visual Studio Code" width="50" height="50" />
    <img src="https://upload.wikimedia.org/wikipedia/en/8/8c/Trello_logo.svg" alt="Trello" width="50" height="50" />
    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Airtable_Logo.svg" alt="Airtable" width="50" height="50" />
    <img src="https://upload.wikimedia.org/wikipedia/fr/4/4f/Discord_Logo_sans_texte.svg" alt="Discord" width="50" height="50" />
    </div>
    """, unsafe_allow_html=True)
# ========================
# Page MON CV
# ========================
elif page == "MON CV":
    st.title("Mon CV")
    st.write("Voici un aperçu de mon CV :")
    
    # Affichage du CV
    cv_image = Image.open("cv_capture.jpg")
    st.image(cv_image)
    st.markdown(" Téléchargez mon CV  : [ICI](https://github.com/Soufiane-R/portfolio/raw/bb16596c64ba4d5f03bdc97c99862674ba1dee21/CV_22-01-2025.pdf)")
    st.write("")
    
    
# ========================
# Page Mes Projets
# ========================
elif page == "Mes Projets":
    st.title("Mes Projets")
    
        # Projet 1 : Toys and Models
    st.header("Projet : Toys and Models")
    st.write("🔍 **Contexte du projet :**")
    st.write("Ce projet avait pour objectif de concevoir un outil d'automatisation de la visualisation des indicateurs clés pour faciliter le pilotage stratégique de l'entreprise.")

    st.write("📊 **Étapes clés réalisées :**")
    st.write("- **Analyse des données :** Étude approfondie du schéma de base de données pour identifier les relations et structures pertinentes.")
    st.write("- **Requêtes SQL :** Écriture de requêtes optimisées pour connecter différentes tables et extraire des insights pertinents.")
    st.write("- **Création d'un tableau de bord interactif :**")
    st.write("   - Conception sous **Power BI** pour visualiser les indicateurs stratégiques, incluant :")
    st.write("     - **Performance financière**")
    st.write("     - **Résultats commerciaux**")
    st.write("     - **Aspects logistiques**")
    st.write("     - **Indicateurs RH**")

    st.write("💡 **Impact :**")
    st.write("Cet outil a permis de simplifier l'accès aux données, d'accélérer la prise de décision et d'améliorer la gestion globale de l'entreprise grâce à des visualisations claires et dynamiques.")
    
  # Affichage des images côte à côte
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        projet1_image = Image.open("projet_1_dashboard.png")
        st.image(projet1_image)

    with col2:
        projet1_image_1 = Image.open("projet_1_dashboard_2.png")
        st.image(projet1_image_1, use_container_width=True)

    with col3:
        projet1_image_2 = Image.open("projet_1_dashboard_3.png")
        st.image(projet1_image_2, use_container_width=True)

    with col4:
        projet1_image_3 = Image.open("projet_1_dashboard_1.png")
        st.image(projet1_image_3, use_container_width=True)

    st.write("---")
    
    # Projet 2
    st.header("Cinéma dans la Creuse")
    st.write("🔍 **Contexte du projet :**")
    st.write("Un cinéma de la Creuse, souhaitant se digitaliser, m'a demandé de concevoir un moteur de recommandations de films basé sur des données IMDb et TMDB.")

    st.write("📊 **Étapes clés réalisées :**")
    st.write("- Étude de marché sur la consommation de cinéma dans la région pour identifier les préférences locales.")
    st.write("- Analyse des bases de données pour dégager des tendances : acteurs les plus présents, durées moyennes des films, âge moyen des acteurs, etc.")
    st.write("- Création d'un moteur de recommandations basé sur des algorithmes de machine learning pour proposer des films adaptés.")
    st.write("- Intégration des images des films (affiches) dans l'interface utilisateur pour une expérience immersive.")

    st.write("💡 **Impact :**")
    st.write("Ce projet a permis de poser les bases d'une stratégie numérique pour attirer un public plus large et offrir une expérience utilisateur moderne, personnalisée et interactive.")
      # Affichage des images côte à côte
    col1, col2, col3 = st.columns(3)

    with col1:
        projet2_image = Image.open("projet_2_1.png")
        st.image(projet2_image)

    with col2:
        projet2_image_1 = Image.open("projet_2_2.png")
        st.image(projet2_image_1, use_container_width=True)

    with col3:
        projet2_image_2 = Image.open("projet_2_3.png")
        st.image(projet2_image_2, use_container_width=True)

    st.markdown("Lien du projet : https://projet-cinema-creuse-wcs.streamlit.app/")

    

    st.write("---")
    
    # Projet 3
    st.header("Analyse des données historiques des Jeux Olympiques")

    st.write("🔍 **Contexte de l'exercice :**")
    st.write("Les Missions Data sont une méthodologie d'apprentissage immersive qui combine jeu de rôle, analyse de données et relation client. Cet exercice est conçu pour répondre à des besoins métiers spécifiques tout en développant des compétences en gestion de projet et en communication.")

    st.write("📊 **Mission confiée :**")
    st.write("Analyse des données historiques des Jeux Olympiques pour identifier les tendances clés, comme les performances des athlètes, les évolutions par pays, et les caractéristiques des disciplines sportives.")

    st.write("📊 **Étapes clés réalisées :**")
    st.write("- **Choix du dataset :** Exploration des données disponibles sur les Jeux Olympiques pour structurer l'analyse.")
    st.write("- **Rédaction d'un Brief Client :** Création d'un brief décrivant les besoins métiers fictifs, les objectifs de l'analyse, et les livrables.")
    st.write("- **Collaboration en équipe :** Travail en binômes avec des interactions client-équipe pour simuler une expérience réelle.")
    st.write("- **Analyse des données :** Exploration des performances des athlètes, visualisation des tendances historiques, et mise en évidence des insights pertinents.")

    st.write("⏳ **Durée de l'exercice :** 24 heures")

    st.write("💡 **Impact :**")
    st.write("Cette mission a permis de comprendre les attentes clients et de répondre avec des analyses précises et visuelles, tout en développant des compétences en communication et en résolution de problèmes.")
    st.write("---")

    projet3_image = Image.open("Dashboard_Mission_Data.png")
    col1, col2, col3 = st.columns([1, 2, 1])  # Colonnes pour centrer
    with col2:
        st.image(projet3_image, use_container_width=True)
    

# ========================
# Page Contact
# ========================
elif page == "Contact":
    st.title("Contact")
    st.write("Vous pouvez me contacter via les plateformes suivantes :")
    
    # Liste des contacts
    st.markdown("""
    - **Email** : [rabhiui.soufiane@gmail.com](mailto:rabhiui.soufiane@gmail.com)
    - **LinkedIn** : [linkedin.com/in/soufiane-rabhiui](https://www.linkedin.com/in/soufiane-rabhiui-72a314309/)
    - **GitHub** : [github.com/Soufiane-R](https://github.com/Soufiane-R)
    """)

# ========================
# Footer
# ========================
st.sidebar.write("---")
st.sidebar.write("© 2025 Soufiane Rabhiui. Tous droits réservés.")
