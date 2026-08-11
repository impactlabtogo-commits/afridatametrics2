import streamlit as st
import os
from datetime import datetime

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="AfriDataMetrics | Impact Lab TOGO", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MASQUAGE DES ÉLÉMENTS STREAMLIT (SaaS Look & Feel) ---
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppToolbar {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- 1. GESTION DES FICHIERS & DONNÉES (Backend) ---
COUNTER_FILE = 'visitor_count.txt'
LEADS_FILE = 'leads.csv'

def get_visitor_count():
    if not os.path.exists(COUNTER_FILE): count = 1
    else:
        with open(COUNTER_FILE, 'r') as f:
            try: count = int(f.read().strip()) + 1
            except: count = 1
    with open(COUNTER_FILE, 'w') as f: f.write(str(count))
    return count

def save_lead(email, name, category="Général"):
    file_exists = os.path.exists(LEADS_FILE)
    with open(LEADS_FILE, 'a', encoding='utf-8') as f:
        if not file_exists: f.write('Date,Nom,Email,Categorie\n')
        f.write(f'"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}","{name}","{email}","{category}"\n')

if 'visitor_counted' not in st.session_state:
    st.session_state.visitor_count = get_visitor_count()
    st.session_state.visitor_counted = True

# --- 2. DONNÉES EXPERTES COMPLÈTES (15 PAYS CEDEAO) ---
cedeao_full_data = {
    "Togo": {"Indicateurs": {"Inflation": "2.7%", "PIB": "5.6%", "Solde Budg.": "-3.8%", "Change": "Stable"}, "Analyse": "La dynamique inflationniste est maîtrisée grâce à une politique monétaire prudente de la BCEAO et un approvisionnement régulier des marchés locaux. Toutefois, la vigilance s'impose sur le solde budgétaire, fortement impacté par les investissements infrastructurels, afin de préserver la viabilité de la dette à moyen terme.", "Points": [3.2, 3.0, 2.8, 2.5, 2.7, 2.6, 2.4]},
    "Côte d'Ivoire": {"Indicateurs": {"Inflation": "3.1%", "PIB": "6.8%", "Solde Budg.": "-4.2%", "Change": "Stable"}, "Analyse": "L'économie ivoirienne affiche une résilience remarquable portée par le dynamisme de la filière agro-industrielle et des investissements publics. La maîtrise des prix alimentaires doit rester la priorité pour maintenir le pouvoir d'achat urbain.", "Points": [3.5, 3.3, 3.2, 3.0, 3.1, 3.2, 3.3]},
    "Sénégal": {"Indicateurs": {"Inflation": "2.9%", "PIB": "7.2%", "Solde Budg.": "-5.1%", "Change": "Stable"}, "Analyse": "L'entrée en production imminente des hydrocarbures redessine les perspectives macroéconomiques. Il est recommandé d'accompagner cette transition par une stricte discipline budgétaire pour éviter les risques de surchauffe.", "Points": [3.0, 2.9, 2.8, 2.8, 2.9, 2.9, 2.8]},
    "Bénin": {"Indicateurs": {"Inflation": "2.8%", "PIB": "6.3%", "Solde Budg.": "-4.0%", "Change": "Stable"}, "Analyse": "Les performances du port de Cotonou et les réformes logistiques soutiennent l'activité. La consolidation budgétaire progresse conformément aux critères de convergence de l'UEMOA.", "Points": [3.1, 3.0, 2.9, 2.7, 2.8, 2.7, 2.6]},
    "Burkina Faso": {"Indicateurs": {"Inflation": "3.4%", "PIB": "5.1%", "Solde Budg.": "-5.5%", "Change": "Stable"}, "Analyse": "Malgré les défis sécuritaires, l'économie fait preuve d'une forte résilience, soutenue par le secteur aurifère. Une attention particulière doit être portée à la gestion des tensions sur les prix de première nécessité.", "Points": [3.8, 3.6, 3.5, 3.2, 3.4, 3.5, 3.3]},
    "Mali": {"Indicateurs": {"Inflation": "3.2%", "PIB": "4.8%", "Solde Budg.": "-4.7%", "Change": "Stable"}, "Analyse": "L'activité économique reste contrainte par les chocs exogènes et énergétiques. La diversification des sources d'approvisionnement et le soutien à la production agricole locale sont des impératifs stratégiques.", "Points": [3.4, 3.3, 3.1, 3.0, 3.2, 3.1, 3.0]},
    "Niger": {"Indicateurs": {"Inflation": "3.5%", "PIB": "6.5%", "Solde Budg.": "-4.8%", "Change": "Stable"}, "Analyse": "Le secteur extractif (pétrole) constitue le principal moteur de la croissance à court terme. Les politiques publiques doivent cibler l'optimisation des recettes intérieures pour financer le développement social.", "Points": [3.0, 3.1, 3.2, 3.3, 3.5, 3.6, 3.4]},
    "Guinée-Bissau": {"Indicateurs": {"Inflation": "4.0%", "PIB": "4.5%", "Solde Budg.": "-4.5%", "Change": "Stable"}, "Analyse": "La campagne de commercialisation de l'anacarde conditionne l'équilibre macroéconomique global. Des réformes structurelles dans la gouvernance financière sont indispensables pour stabiliser le cadre budgétaire.", "Points": [4.5, 4.3, 4.1, 3.9, 4.0, 3.8, 3.7]},
    "Ghana": {"Indicateurs": {"Inflation": "18.5%", "PIB": "4.2%", "Solde Budg.": "-6.5%", "Change": "Dépréciation"}, "Analyse": "Une pression inflationniste persistante nécessite des ajustements structurels rigoureux. La priorité absolue doit être accordée à la stricte consolidation budgétaire et au resserrement prudentiel pour stabiliser la monnaie nationale et ancrer les anticipations.", "Points": [22.0, 20.5, 19.8, 19.0, 18.5, 17.8, 17.0]},
    "Nigeria": {"Indicateurs": {"Inflation": "22.4%", "PIB": "3.3%", "Solde Budg.": "-4.6%", "Change": "Volatile"}, "Analyse": "Les réformes audacieuses sur les subventions et le marché des changes créent des tensions inflationnistes transitoires mais assainissent les fondamentaux à long terme. Le suivi de la pauvreté et la protection des populations vulnérables s'avèrent critiques.", "Points": [21.0, 21.5, 21.8, 22.0, 22.4, 22.8, 23.0]},
    "Guinée": {"Indicateurs": {"Inflation": "5.2%", "PIB": "5.5%", "Solde Budg.": "-2.1%", "Change": "Stable"}, "Analyse": "Portée par les megas-projets de bauxite et de fer, l'économie maintient un rythme satisfaisant. Le défi réside dans l'intégration locale de la chaîne de valeur minière pour maximiser les retombées socio-économiques.", "Points": [5.5, 5.4, 5.3, 5.2, 5.2, 5.1, 5.0]},
    "Sierra Leone": {"Indicateurs": {"Inflation": "25.1%", "PIB": "3.8%", "Solde Budg.": "-5.2%", "Change": "Dépréciation"}, "Analyse": "L'inflation élevée pèse lourdement sur le pouvoir d'achat. Une coordination étroite entre la banque centrale et le ministère des finances est requise pour juguler la monétisation du déficit budgétaire.", "Points": [28.0, 27.0, 26.5, 25.8, 25.1, 24.5, 24.0]},
    "Libéria": {"Indicateurs": {"Inflation": "7.3%", "PIB": "4.7%", "Solde Budg.": "-3.9%", "Change": "Stable"}, "Analyse": "L'amélioration de la gouvernance macroéconomique et l'apurement des arriérés intérieurs soutiennent la reprise. Des efforts accrus sont nécessaires pour renforcer l'infrastructure de base et diversifier les sources de croissance.", "Points": [6.8, 7.0, 7.1, 7.2, 7.3, 7.5, 7.4]},
    "Gambie": {"Indicateurs": {"Inflation": "6.0%", "PIB": "5.2%", "Solde Budg.": "-4.3%", "Change": "Stable"}, "Analyse": "Le tourisme et les transferts de fonds de la diaspora continuent de soutenir l'activité. La viabilité de la dette publique reste un point de vigilance qui nécessite une rationalisation continue des dépenses courantes.", "Points": [6.5, 6.3, 6.2, 6.1, 6.0, 5.9, 5.8]},
    "Cap-Vert": {"Indicateurs": {"Inflation": "2.2%", "PIB": "4.8%", "Solde Budg.": "-3.2%", "Change": "Fixe (Euro)"}, "Analyse": "La forte reprise du secteur touristique tire l'économie insulaire vers le haut. L'arrimage de l'escudo à l'euro garantit une stabilité des prix remarquable, bien que la vulnérabilité aux chocs extérieurs demeure élevée.", "Points": [2.5, 2.4, 2.3, 2.2, 2.2, 2.1, 2.0]}
}

# --- 3. FONCTIONS D'AFFICHAGE ---
def run_main_dashboard():
    pays = st.sidebar.selectbox("Sélectionnez un pays :", list(cedeao_full_data.keys()))
    st.markdown(f'<div style="background-color: #EFF6FF; color: #1D4ED8; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; margin-bottom: 20px; border: 1px solid #BFDBFE; display: inline-block;">🚀 AfriDataMetrics &bull; Intelligence Économique par Impact Lab TOGO</div>', unsafe_allow_html=True)
    st.title(f"📊 Analyse : {pays}")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Inflation", cedeao_full_data[pays]["Indicateurs"]["Inflation"])
    c2.metric("Croissance PIB", cedeao_full_data[pays]["Indicateurs"]["PIB"])
    c3.metric("Solde Budg.", cedeao_full_data[pays]["Indicateurs"]["Solde Budg."])
    c4.metric("Change", cedeao_full_data[pays]["Indicateurs"]["Change"])
    st.divider()
    st.subheader("💡 Analyse & Recommandations")
    st.info(cedeao_full_data[pays]["Analyse"])
    
    points = cedeao_full_data[pays]["Points"]
    chart_html = f"""
    <div style="background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #E5E7EB;">
        <canvas id="macroChart" width="400" height="130"></canvas>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
    new Chart(document.getElementById('macroChart').getContext('2d'), {{
        type: 'line',
        data: {{ labels: ['25-01', '25-04', '25-07', '25-10', '26-01', '26-04', '26-07'], datasets: [{{ label: 'Inflation %', data: {points}, borderColor: '#1D4ED8', fill: true, tension: 0.3 }}] }},
        options: {{ responsive: true }}
    }});
    </script>
    """
    st.components.v1.html(chart_html, height=350)

# --- 4. NAVIGATION & SIDEBAR ---
st.sidebar.title("🌍 AfriDataMetrics")
menu = st.sidebar.radio("Navigation", ["Tableau de Bord", "Abonnements Pro", "Data & Rapports", "Conseil Sur-Mesure"])

with st.sidebar.form("lead_capture"):
    n, e = st.text_input("Nom"), st.text_input("E-mail Pro")
    if st.form_submit_button("S'inscrire à la veille"):
        save_lead(e, n, "Veille")
        st.success("Enregistré !")

# --- 5. LOGIQUE PAGES ---
if menu == "Tableau de Bord": run_main_dashboard()
elif menu == "Abonnements Pro":
    st.title("💼 Offres Pro (SaaS)")
    c1, c2 = st.columns(2)
    with c1: st.markdown("### Standard Pro\n50 000 FCFA/mois")
    with c2: st.markdown("### Institutionnel\nSur Devis")
elif menu == "Data & Rapports":
    st.title("📊 Data-as-a-Service")
    st.write("Catalogue des bases de données et rapports disponibles.")
elif menu == "Conseil Sur-Mesure":
    st.title("🎯 Conseil & Stratégie")
    if st.form_submit_button("Envoyer"): save_lead("N/A", "N/A", "Conseil")
