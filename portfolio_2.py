import streamlit as st
from PIL import Image
from pathlib import Path
import base64
from st_on_hover_tabs import on_hover_tabs

# ========================
# Configurations de la page
# ========================
st.set_page_config(page_title="Portfolio - Soufiane Rabhiui", page_icon=":bar_chart:", layout="wide")

# ========================
# Ajout d'un arrière-plan via CSS
# ========================
image_path = Path("image-background.png")
if image_path.is_file():
    with open(image_path, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode()
else:
    st.error(f"L'image '{image_path.name}' est introuvable dans le dossier : {image_path.parent}")

css = f'''
<style>
    .stApp {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
    }}
    section[data-testid='stSidebar'] {{
        background-color: #111;
        min-width: unset !important;
        width: unset !important;
        flex-shrink: unset !important;
    }}
    @media(hover) {{
        section[data-testid='stSidebar'] > div {{
            height: 100%;
            width: 95px;
            position: relative;
            z-index: 1;
            top: 0;
            left: 0;
            background-color: #111;
            overflow-x: hidden;
            transition: 0.5s ease;
            padding-top: 60px;
            white-space: nowrap;
        }}
        section[data-testid='stSidebar'] > div:hover {{
            width: 388px;
        }}
    }}
    @media(max-width: 272px) {{
        section[data-testid='stSidebar'] > div {{
            width: 15rem;
        }}
    }}
</style>
'''
st.markdown(css, unsafe_allow_html=True)

# ========================
# Barre latérale avec menu interactif
# ========================
with st.sidebar:
    tabs = on_hover_tabs(
        tabName=['Accueil', 'MON CV', 'Mes Projets', 'Contact'],
        iconName=['house', 'person', 'folder', 'envelope'],
        default_choice=0
    )

# ========================
# Gestion des pages
# ========================
if tabs == 'Accueil':
    st.title("Portfolio de Soufiane RABHIUI")
    st.write("✨ Les données sont des ressources précieuses pour une entreprise, et c'est l'analyse qui transforme cette richesse en moteur de décision.✨")
    st.write("Passionné par l'exploitation des données pour éclairer et optimiser la prise de décision, je possède une expertise technique en SQL, Python (Pandas, NumPy) et Power BI, ainsi qu'une solide expérience dans la création de tableaux de bord interactifs et l'automatisation des analyses.")
    st.write("Mon objectif est de traduire des données complexes en insights clairs et actionnables, alignés sur les besoins stratégiques des entreprises pour maximiser leur impact et leur efficacité.")

    accueil_image = Image.open("Data-Analytics.jpg")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(accueil_image, use_container_width=True)

    st.write("---")
    st.header("Compétences Techniques et Méthodologiques")

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

elif tabs == 'MON CV':
    st.title("Mon CV")
    st.write("Voici un aperçu de mon CV :")

    cv_image = Image.open("cv_capture.jpg")
    st.image(cv_image)
    st.markdown("[Téléchargez mon CV ici](https://github.com/Soufiane-R/portfolio/raw/bb16596c64ba4d5f03bdc97c99862674ba1dee21/CV_22-01-2025.pdf)")

elif tabs == 'Mes Projets':
    st.title("Mes Projets")

    # Exemple de projet
    st.header("Projet : Toys and Models")
    st.write("🔍 **Contexte du projet :**")
    st.write("Ce projet avait pour objectif de concevoir un outil d'automatisation de la visualisation des indicateurs clés pour faciliter le pilotage stratégique de l'entreprise.")
    st.write("📊 **Étapes clés réalisées :**")
    st.write("- Analyse des données et création d'un tableau de bord interactif avec Power BI")

    projet1_image = Image.open("projet_1_dashboard.png")
    st.image(projet1_image)

elif tabs == 'Contact':
    st.title("Contact")
    st.write("Vous pouvez me contacter via les plateformes suivantes :")
    st.markdown("""
    - **Email** : [rabhiui.soufiane@gmail.com](mailto:rabhiui.soufiane@gmail.com)
    - **LinkedIn** : [linkedin.com/in/soufiane-rabhiui](https://www.linkedin.com/in/soufiane-rabhiui-72a314309/)
    - **GitHub** : [github.com/Soufiane-R](https://github.com/Soufiane-R)
    """)

st.sidebar.write("---")
st.sidebar.write("© 2025 Soufiane Rabhiui. Tous droits réservés.")
