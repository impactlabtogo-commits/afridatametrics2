import streamlit as st
import os
from datetime import datetime

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="AfriDataMetrics | Impact Lab TOGO", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MASQUAGE TOTAL DES ÉLÉMENTS STREAMLIT (SaaS Look & Feel Top 1) ---
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppToolbar {visibility: hidden;}
    div[data-testid="stDecoration"] {visibility: hidden;}
    div.viewerBadge_container__1QSob {display: none !important;}
    .viewerBadge_link__1S1_7 {display: none !important;}
    button[kind="header"] {visibility: hidden;}
    #manage-app-button {display: none !important;}
    .stAppDeployButton {display: none !important;}
    iframe[title="streamlit_badge"] {display: none !important;}
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

# --- 3. BARRE DE NAVIGATION SUPÉRIEURE (SaaS Pro Tabs) ---
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #E5E7EB; padding-bottom: 10px; margin-bottom: 20px;">
        <div>
            <span style="font-size: 20px; font-weight: bold; color: #1D4ED8;">🌍 AfriDataMetrics</span>
            <span style="font-size: 12px; color: #6B7280; margin-left: 10px;">Impact Lab TOGO &bull; Intelligence Économique CEDEAO</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Utilisation d'onglets horizontaux professionnels
tab_dashboard, tab_pro, tab_daas, tab_conseil = st.tabs([
    "📊 Tableau de Bord (15 Pays)", 
    "💼 Abonnements Pro (SaaS)", 
    "📈 Data & Rapports (DaaS)", 
    "🎯 Conseil Stratégique"
])

# --- ONGLOT 1 : TABLEAU DE BORD ---
with tab_dashboard:
    st.markdown("### 🌐 Sélection du Territoire Économique")
    # Sélecteur de pays bien visible au centre ou en haut de la page
    pays = st.selectbox("Choisissez un pays membre de la CEDEAO :", list(cedeao_full_data.keys()), key="pays_select")
    
    st.markdown("---")
    st.markdown(f"## 📊 Analyse Macroéconomique : **{pays}**")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Inflation Actuelle", cedeao_full_data[pays]["Indicateurs"]["Inflation"])
    c2.metric("Croissance PIB", cedeao_full_data[pays]["Indicateurs"]["PIB"])
    c3.metric("Solde Budgétaire", cedeao_full_data[pays]["Indicateurs"]["Solde Budg."])
    c4.metric("Tendance Change", cedeao_full_data[pays]["Indicateurs"]["Change"])
    
    st.divider()
    st.subheader("💡 Analyse & Recommandations Stratégiques")
    st.info(cedeao_full_data[pays]["Analyse"])
    
    st.subheader("📉 Modélisation Prédictive & Trajectoire des Prix")
    points = cedeao_full_data[pays]["Points"]
    chart_html = f"""
    <div style="background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #E5E7EB;">
        <canvas id="macroChart" width="400" height="120"></canvas>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
    new Chart(document.getElementById('macroChart').getContext('2d'), {{
        type: 'line',
        data: {{ 
            labels: ['2025-Q1', '2025-Q2', '2025-Q3', '2025-Q4', '2026-Q1', '2026-Q2 (Prév.)', '2026-Q3 (Prév.)'], 
            datasets: [{{ 
                label: 'Inflation (Glissement annuel %)', 
                data: {points}, 
                borderColor: '#1D4ED8', 
                backgroundColor: 'rgba(29, 78, 216, 0.08)',
                borderWidth: 3,
                fill: true, 
                tension: 0.35 
            }}] 
        }},
        options: {{ responsive: true }}
    }});
    </script>
    """
    st.components.v1.html(chart_html, height=350)

# --- ONGLOT 2 : ABONNEMENTS PRO ---
with tab_pro:
    st.title("💼 Offres d'Abonnement Professionnel (SaaS)")
    st.markdown("Débloquez la puissance complète de nos modèles économétriques et de nos outils de simulation prédictive pour vos équipes.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🚀 Offre Standard Pro")
        st.markdown("**Pour les analystes et chercheurs indépendants**")
        st.markdown("- Accès complet aux tableaux de bord historiques\n- Modélisation avancée\n- Export des graphiques et données")
        st.markdown("### **50 000 FCFA / mois**")
        if st.button("Souscrire à l'Offre Pro"):
            st.success("Redirection vers le paiement sécurisé... (Contactez impactlabtogo@gmail.com pour finaliser)")

    with col2:
        st.markdown("### 🏛️ Licence Institutionnelle")
        st.markdown("**Pour les Banques, Fonds & Cabinets**")
        st.markdown("- Accès multi-utilisateurs illimité\n- Modélisation avancée (System GMM & DSGE)\n- Accès API dédié et rapports automatisés")
        st.markdown("### **Sur Devis / Annuel**")
        if st.button("Demander une Licence Institutionnelle"):
            save_lead("Demande_Licence_Pro", "Institutionnel", "SaaS B2B")
            st.success("Demande enregistrée. Notre équipe commerciale vous contactera sous 24h.")

# --- ONGLOT 3 : DATA & RAPPORTS ---
with tab_daas:
    st.title("📊 Vente de Données & Rapports (Data-as-a-Service)")
    st.markdown("Téléchargez des bases de données macroéconomiques nettoyées, structurées et prêtes à l'emploi, ainsi que nos notes d'orientation stratégique sectorielles.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 📑 Note d'Orientation : ZLECAf & Corridors")
        st.markdown("Analyse prospective des mégatendances continentales et des impacts sur les chaînes de valeur.")
        st.markdown("**Prix : 25 000 FCFA**")
        if st.button("Commander le Rapport PDF"):
            st.info("Envoyez un mail à impactlabtogo@gmail.com avec la référence #ZLECAf pour recevoir le lien de téléchargement.")
            
    with col2:
        st.markdown("#### 🗃️ Base de Données Panel CEDEAO (Clean)")
        st.markdown("Jeu de données Stata/R (1995-2025) prêt pour régressions économétriques.")
        st.markdown("**Prix : 75 000 FCFA**")
        if st.button("Commander la Base de Données"):
            st.info("Envoyez un mail à impactlabtogo@gmail.com pour l'acquisition des tables de données.")

# --- ONGLOT 4 : CONSEIL ---
with tab_conseil:
    st.title("🎯 Conseil Stratégique & Études sur Mesure")
    st.markdown("Vous avez besoin d'une étude d'impact spécifique, d'une modélisation macroéconomique sur-mesure ou d'une analyse de risque pour votre implantation dans la région ?")
    
    with st.form("consulting_form"):
        c_name = st.text_input("Nom de l'organisation / Entreprise")
        c_email = st.text_input("E-mail de contact")
        c_project = st.text_area("Décrivez votre besoin ou votre projet d'étude")
        c_submit = st.form_submit_button("Envoyer la demande de mission")
        
        if c_submit:
            if c_email and c_project:
                save_lead(c_email, c_name, "Mission Conseil Sur-Mesure")
                st.success("✅ Votre demande de mission a été transmise à notre équipe d'associés. Nous vous répondrons sous 48h.")
            else:
                st.error("Veuillez renseigner au moins l'e-mail et les détails du projet.")

# --- BARRE LATÉRALE DISCRÈTE (Capture de leads & stats internes) ---
st.sidebar.title("🌍 AfriDataMetrics")
st.sidebar.caption("Impact Lab TOGO")
st.sidebar.markdown("---")
st.sidebar.subheader("📬 Veille Stratégique")

with st.sidebar.form("lead_capture_form"):
    visitor_name = st.text_input("Votre Nom")
    visitor_email = st.text_input("E-mail Pro *")
    submitted = st.form_submit_button("S'inscrire")

    if submitted:
        if visitor_email and "@" in visitor_email:
            save_lead(visitor_email, visitor_name if visitor_name else "Anonyme", "Veille Générale")
            st.sidebar.success("✅ Validé !")
        else:
            st.sidebar.error("❌ E-mail invalide.")

st.sidebar.markdown("---")
st.sidebar.caption(f"📊 Trafic plateforme : **{st.session_state.visitor_count}** visites")
