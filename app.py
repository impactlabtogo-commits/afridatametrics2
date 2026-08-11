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
    "Togo": {"Indicateurs": {"Inflation": 2.7, "PIB": "5.6%", "Solde Budg.": "-3.8%", "Change": "Stable"}, "Analyse": "La dynamique inflationniste est maîtrisée grâce à une politique monétaire prudente de la BCEAO et un approvisionnement régulier des marchés locaux. Toutefois, la vigilance s'impose sur le solde budgétaire, fortement impacté par les investissements infrastructurels, afin de préserver la viabilité de la dette à moyen terme.", "Points": [3.2, 3.0, 2.8, 2.5, 2.7, 2.6, 2.4]},
    "Côte d'Ivoire": {"Indicateurs": {"Inflation": 3.1, "PIB": "6.8%", "Solde Budg.": "-4.2%", "Change": "Stable"}, "Analyse": "L'économie ivoirienne affiche une résilience remarquable portée par le dynamisme de la filière agro-industrielle et des investissements publics. La maîtrise des prix alimentaires doit rester la priorité pour maintenir le pouvoir d'achat urbain.", "Points": [3.5, 3.3, 3.2, 3.0, 3.1, 3.2, 3.3]},
    "Sénégal": {"Indicateurs": {"Inflation": 2.9, "PIB": "7.2%", "Solde Budg.": "-5.1%", "Change": "Stable"}, "Analyse": "L'entrée en production imminente des hydrocarbures redessine les perspectives macroéconomiques. Il est recommandé d'accompagner cette transition par une stricte discipline budgétaire pour éviter les risques de surchauffe.", "Points": [3.0, 2.9, 2.8, 2.8, 2.9, 2.9, 2.8]},
    "Bénin": {"Indicateurs": {"Inflation": 2.8, "PIB": "6.3%", "Solde Budg.": "-4.0%", "Change": "Stable"}, "Analyse": "Les performances du port de Cotonou et les réformes logistiques soutiennent l'activité. La consolidation budgétaire progresse conformément aux critères de convergence de l'UEMOA.", "Points": [3.1, 3.0, 2.9, 2.7, 2.8, 2.7, 2.6]},
    "Burkina Faso": {"Indicateurs": {"Inflation": 3.4, "PIB": "5.1%", "Solde Budg.": "-5.5%", "Change": "Stable"}, "Analyse": "Malgré les défis sécuritaires, l'économie fait preuve d'une forte résilience, soutenue par le secteur aurifère. Une attention particulière doit être portée à la gestion des tensions sur les prix de première nécessité.", "Points": [3.8, 3.6, 3.5, 3.2, 3.4, 3.5, 3.3]},
    "Mali": {"Indicateurs": {"Inflation": 3.2, "PIB": "4.8%", "Solde Budg.": "-4.7%", "Change": "Stable"}, "Analyse": "L'activité économique reste contrainte par les chocs exogènes et énergétiques. La diversification des sources d'approvisionnement et le soutien à la production agricole locale sont des impératifs stratégiques.", "Points": [3.4, 3.3, 3.1, 3.0, 3.2, 3.1, 3.0]},
    "Niger": {"Indicateurs": {"Inflation": 3.5, "PIB": "6.5%", "Solde Budg.": "-4.8%", "Change": "Stable"}, "Analyse": "Le secteur extractif (pétrole) constitue le principal moteur de la croissance à court terme. Les politiques publiques doivent cibler l'optimisation des recettes intérieures pour financer le développement social.", "Points": [3.0, 3.1, 3.2, 3.3, 3.5, 3.6, 3.4]},
    "Guinée-Bissau": {"Indicateurs": {"Inflation": 4.0, "PIB": "4.5%", "Solde Budg.": "-4.5%", "Change": "Stable"}, "Analyse": "La campagne de commercialisation de l'anacarde conditionne l'équilibre macroéconomique global. Des réformes structurelles dans la gouvernance financière sont indispensables pour stabiliser le cadre budgétaire.", "Points": [4.5, 4.3, 4.1, 3.9, 4.0, 3.8, 3.7]},
    "Ghana": {"Indicateurs": {"Inflation": 18.5, "PIB": "4.2%", "Solde Budg.": "-6.5%", "Change": "Dépréciation"}, "Analyse": "Une pression inflationniste persistante nécessite des ajustements structurels rigoureux. La priorité absolue doit être accordée à la stricte consolidation budgétaire et au resserrement prudentiel pour stabiliser la monnaie nationale et ancrer les anticipations.", "Points": [22.0, 20.5, 19.8, 19.0, 18.5, 17.8, 17.0]},
    "Nigeria": {"Indicateurs": {"Inflation": 22.4, "PIB": "3.3%", "Solde Budg.": "-4.6%", "Change": "Volatile"}, "Analyse": "Les réformes audacieuses sur les subventions et le marché des changes créent des tensions inflationnistes transitoires mais assainissent les fondamentaux à long terme. Le suivi de la pauvreté et la protection des populations vulnérables s'avèrent critiques.", "Points": [21.0, 21.5, 21.8, 22.0, 22.4, 22.8, 23.0]},
    "Guinée": {"Indicateurs": {"Inflation": 5.2, "PIB": "5.5%", "Solde Budg.": "-2.1%", "Change": "Stable"}, "Analyse": "Portée par les megas-projets de bauxite et de fer, l'économie maintient un rythme satisfaisant. Le défi réside dans l'intégration locale de la chaîne de valeur minière pour maximiser les retombées socio-économiques.", "Points": [5.5, 5.4, 5.3, 5.2, 5.2, 5.1, 5.0]},
    "Sierra Leone": {"Indicateurs": {"Inflation": 25.1, "PIB": "3.8%", "Solde Budg.": "-5.2%", "Change": "Dépréciation"}, "Analyse": "L'inflation élevée pèse lourdement sur le pouvoir d'achat. Une coordination étroite entre la banque centrale et le ministère des finances est requise pour juguler la monétisation du déficit budgétaire.", "Points": [28.0, 27.0, 26.5, 25.8, 25.1, 24.5, 24.0]},
    "Libéria": {"Indicateurs": {"Inflation": 7.3, "PIB": "4.7%", "Solde Budg.": "-3.9%", "Change": "Stable"}, "Analyse": "L'amélioration de la gouvernance macroéconomique et l'apurement des arriérés intérieurs soutiennent la reprise. Des efforts accrus sont nécessaires pour renforcer l'infrastructure de base et diversifier les sources de croissance.", "Points": [6.8, 7.0, 7.1, 7.2, 7.3, 7.5, 7.4]},
    "Gambie": {"Indicateurs": {"Inflation": 6.0, "PIB": "5.2%", "Solde Budg.": "-4.3%", "Change": "Stable"}, "Analyse": "Le tourisme et les transferts de fonds de la diaspora continuent de soutenir l'activité. La viabilité de la dette publique reste un point de vigilance qui nécessite une rationalisation continue des dépenses courantes.", "Points": [6.5, 6.3, 6.2, 6.1, 6.0, 5.9, 5.8]},
    "Cap-Vert": {"Indicateurs": {"Inflation": 2.2, "PIB": "4.8%", "Solde Budg.": "-3.2%", "Change": "Fixe (Euro)"}, "Analyse": "La forte reprise du secteur touristique tire l'économie insulaire vers le haut. L'arrimage de l'escudo à l'euro garantit une stabilité des prix remarquable, bien que la vulnérabilité aux chocs extérieurs demeure élevée.", "Points": [2.5, 2.4, 2.3, 2.2, 2.2, 2.1, 2.0]}
}

# --- 3. BARRE DE NAVIGATION SUPÉRIEURE (SaaS Pro Tabs) ---
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #E5E7EB; padding-bottom: 10px; margin-bottom: 20px;">
        <div>
            <span style="font-size: 20px; font-weight: bold; color: #1D4ED8;">🌍 AfriDataMetrics</span>
            <span style="font-size: 12px; color: #6B7280; margin-left: 10px;">Impact Lab TOGO &bull; Intelligence Économique CEDEAO</span>
        </div>
        <div>
            <span style="font-size: 13px; color: #1D4ED8; font-weight: 600;">📧 Contact : impactlabtogo@gmail.com</span>
        </div>
    </div>
""", unsafe_allow_html=True)

tab_dashboard, tab_pro, tab_daas, tab_formations, tab_work, tab_conseil = st.tabs([
    "📊 Tableau de Bord", 
    "💼 Abonnements Pro", 
    "📈 Data & Rapports", 
    "🎓 Formations", 
    "🤝 Travailler avec nous",
    "🎯 Conseil Stratégique"
])

# --- ONGLET 1 : TABLEAU DE BORD (AVEC AJOUTS PERCUTANTS) ---
with tab_dashboard:
    # 1. Fil d'actualité Live (Live Intelligence Feed)
    st.markdown("""
        <div style="background-color: #EFF6FF; border-left: 4px solid #1D4ED8; padding: 10px 15px; border-radius: 4px; margin-bottom: 20px;">
            <span style="font-weight: bold; color: #1E40AF; font-size: 13px;">🔴 LIVE INTELLIGENCE FEED :</span> 
            <span style="font-size: 13px; color: #1E293B;"> Publication de la note de prospective sur l'impact des corridors de libre-échange &bull; Point conjoncturel BCEAO mis à jour.</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🌐 Sélection du Territoire Économique")
    pays = st.selectbox("Choisissez un pays membre de la CEDEAO :", list(cedeao_full_data.keys()), key="pays_select")
    
    st.markdown("---")
    st.markdown(f"## 📊 Analyse Macroéconomique : **{pays}**")
    
    base_infl = cedeao_full_data[pays]["Indicateurs"]["Inflation"]
    
    # 2. Module de Simulateur de Chocs (Stress Test Interactif)
    with st.expander("⚡ Simulateur de Stress Test & Chocs Macroéconomiques (Nouveau)", expanded=False):
        st.markdown("Simulez l'impact instantané de chocs exogènes sur l'inflation du pays sélectionné :")
        col_s1, col_s2, col_s3 = st.columns(3)
        with col_s1:
            choc_petrole = st.slider("Choc Pétrolier (%)", -30, 30, 0, 5)
        with col_s2:
            choc_change = st.slider("Dépréciation Monétaire (%)", 0, 25, 0, 5)
        with col_s3:
            choc_taux = st.slider("Variation Taux Directeur (pts)", -2.0, 2.0, 0.0, 0.5)
        
        # Calcul de l'inflation simulée par modélisation simplifiée
        delta_infl = (choc_petrole * 0.05) + (choc_change * 0.15) - (choc_taux * 0.3)
        simulated_infl = round(base_infl + delta_infl, 1)
        st.info(f"📊 **Résultat de la simulation de choc :** L'inflation projetée passe de **{base_infl}%** à **{simulated_infl}%** sous l'effet cumulé des paramètres choisis.")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Inflation Actuelle", f"{base_infl}%", delta=f"{round(simulated_infl - base_infl, 1)}% (Simul.)" if (simulated_infl != base_infl) else None)
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

    # 3. Comparateur Multi-Pays Instantané (Benchmarking côte à côte)
    st.divider()
    st.subheader("⚖️ Comparateur Multi-Pays (Benchmarking Régional)")
    st.markdown("Sélectionnez plusieurs pays pour comparer instantanément leurs indicateurs macroéconomiques :")
    
    selected_bench_pays = st.multiselect(
        "Pays à comparer :", 
        list(cedeao_full_data.keys()), 
        default=["Togo", "Côte d'Ivoire", "Ghana", "Nigeria"]
    )
    
    if selected_bench_pays:
        bench_data = []
        for p in selected_bench_pays:
            bench_data.append({
                "Pays": p,
                "Inflation (%)": cedeao_full_data[p]["Indicateurs"]["Inflation"],
                "Croissance PIB": cedeao_full_data[p]["Indicateurs"]["PIB"],
                "Solde Budgétaire": cedeao_full_data[p]["Indicateurs"]["Solde Budg."]
            })
        st.dataframe(bench_data, use_container_width=True)

# --- ONGLET 2 : ABONNEMENTS PRO ---
with tab_pro:
    st.title("💼 Offres d'Abonnement Professionnel (SaaS)")
    st.markdown("Débloquez la puissance complète de nos modèles économétriques et de nos outils de simulation prédictive pour vos équipes.")
    st.markdown("💬 **Contact direct souscriptions & devis :** `impactlabtogo@gmail.com`")
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🚀 Offre Standard Pro")
        st.markdown("**Pour les analystes et chercheurs indépendants**")
        st.markdown("- Accès complet aux tableaux de bord historiques\n- Modélisation avancée\n- Export des graphiques et données")
        st.markdown("### **50 000 FCFA / mois**")
        if st.button("Souscrire à l'Offre Pro"):
            st.success("Redirection... Veuillez confirmer votre souscription en écrivant à impactlabtogo@gmail.com")

    with col2:
        st.markdown("### 🏛️ Licence Institutionnelle")
        st.markdown("**Pour les Banques, Fonds & Cabinets**")
        st.markdown("- Accès multi-utilisateurs illimité\n- Modélisation avancée (System GMM & DSGE)\n- Accès API dédié et rapports automatisés")
        st.markdown("### **Sur Devis / Annuel**")
        if st.button("Demander une Licence Institutionnelle"):
            save_lead("Demande_Licence_Pro", "Institutionnel", "SaaS B2B")
            st.success("Demande enregistrée. Notre équipe vous contactera rapidement ou écrivez-nous sur impactlabtogo@gmail.com")

# --- ONGLET 3 : DATA & RAPPORTS ---
with tab_daas:
    st.title("📊 Vente de Données & Rapports (Data-as-a-Service)")
    st.markdown("Téléchargez des bases de données macroéconomiques nettoyées, structurées et prêtes à l'emploi, ainsi que nos notes d'orientation stratégique sectorielles.")
    st.markdown("💬 **Commandes directes :** `impactlabtogo@gmail.com`")
    st.divider()
    
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

# --- ONGLET 4 : FORMATIONS ---
with tab_formations:
    st.title("🎓 Catalogue des Formations (En ligne & Présentiel)")
    st.markdown("Du renforcement de compétences pour étudiants jusqu'aux certifications méthodologiques avancées pour professionnels, experts et chercheurs.")
    st.markdown("💬 **Inscriptions & Formations sur-mesure pour institutions :** `impactlabtogo@gmail.com`")
    st.divider()

    st.subheader("📌 1. Niveau Junior & Étudiants (Fondations & Outils)")
    f1, f2 = st.columns(2)
    with f1:
        st.markdown("#### 🟢 Maîtrise des Outils de Collecte & Enquêtes de Terrain")
        st.markdown("- **Cible :** Étudiants, assistants de recherche, enquêteurs.")
        st.markdown("- **Format :** Hybride (En ligne & Ateliers pratiques Lomé/Kara).")
        st.markdown("- **Programme :** Conception de masques sur ODK, KoboToolbox, XLSForms, apurement et traitement sous R/Stata.")
        st.markdown("### **Coût : 35 000 FCFA**")
    with f2:
        st.markdown("#### 🟢 Initiation à la Programmation Économétrique (R & Stata)")
        st.markdown("- **Cible :** Étudiants en Master 1/2, jeunes diplômés en économie/statistique.")
        st.markdown("- **Format :** En ligne (modules vidéo + tutorat asynchrone).")
        st.markdown("- **Programme :** Manipulation de dataframes, statistiques descriptives, graphiques avancés (ggplot2).")
        st.markdown("### **Coût : 45 000 FCFA**")

    st.divider()
    st.subheader("📌 2. Niveau Intermédiaire & Chercheurs (Modélisation Empirique)")
    f3, f4 = st.columns(2)
    with f3:
        st.markdown("#### 🟡 Économétrie des Données de Panel & Séries Temporelles")
        st.markdown("- **Cible :** Chercheurs, doctorants, analystes juniors.")
        st.markdown("- **Format :** Présentiel intensif (Week-end) ou Virtuel en direct.")
        st.markdown("- **Programme :** Modèles à effets fixés/aléatoires, Panel ARDL, tests de cointégration, corrections d'endogénéité.")
        st.markdown("### **Coût : 90 000 FCFA**")
    with f4:
        st.markdown("#### 🟡 Évaluation d'Impact des Politiques Publiques")
        st.markdown("- **Cible :** Cadres d'administrations, chargés de projets, ONG, chercheurs.")
        st.markdown("- **Format :** En ligne & Ateliers pratiques sur cas réels.")
        st.markdown("- **Programme :** Méthodes Contrefactuelles, Propensity Score Matching (PSM), Difference-in-Differences (DiD).")
        st.markdown("### **Coût : 110 000 FCFA**")

    st.divider()
    st.subheader("📌 3. Niveau Avancé & Professionnel (Experts & Hautes Institutions)")
    f5, f6 = st.columns(2)
    with f5:
        st.markdown("#### 🔴 Modélisation Avancée : System GMM & Équations Simultanées")
        st.markdown("- **Cible :** Économistes seniors, chercheurs affiliés, banquiers centraux.")
        st.markdown("- **Format :** Présentiel exclusif sur 3 jours (ou Masterclass en ligne).")
        st.markdown("- **Programme :** Traitement de la dynamique des panels, instruments valides, tests de Sargan/Hansen, GMM en système.")
        st.markdown("### **Coût : 200 000 FCFA**")
    with f6:
        st.markdown("#### 🔴 Modélisation DSGE & Prévision Macroéconomique")
        st.markdown("- **Cible :** Modélisateurs de banques centrales, ministères des finances, grands cabinets.")
        st.markdown("- **Format :** Présentiel sur mesure / Bootcamp intensif.")
        st.markdown("- **Programme :** Équilibre Général Stochastique Statique et Dynamique, étalonnage, simulations de chocs exogènes.")
        st.markdown("### **Coût : Sur Devis (À partir de 350 000 FCFA)**")

    st.markdown("---")
    if st.button("📩 S'inscrire à une session de formation"):
        save_lead("Demande_Formation", "Candidat Formation", "Formations")
        st.success("Votre intérêt pour nos formations a été enregistré. Écrivez-nous à impactlabtogo@gmail.com pour recevoir la brochure détaillée et les plannings.")

# --- ONGLET 5 : TRAVAILLER AVEC NOUS ---
with tab_work:
    st.title("🤝 Travailler avec Nous (Partenariats & Collaborations)")
    st.markdown("AfriDataMetrics et Impact Lab TOGO structurent un écosystème d'excellence ouvert aux collaborations stratégiques, académiques et institutionnelles à l'échelle régionale et continentale.")
    st.markdown("💬 **Propositions de partenariats & alliances :** `impactlabtogo@gmail.com`")
    st.divider()

    col_w1, col_w2 = st.columns(2)
    with col_w1:
        st.markdown("### 🏛️ 1. Entités Publiques & Gouvernementales")
        st.markdown("""
        * **Ministères de l'Économie & des Finances :** Assistance technique dans le suivi des cadres macroéconomiques et l'évaluation des plans de développement.
        * **Banques Centrales (BCEAO / Banques Nationales) :** Partenariats de recherche sur la politique monétaire, la stabilité financière et la modélisation prédictive.
        * **Instituts Nationaux de la Statistique (INSEED, etc.) :** Appui à la digitalisation des enquêtes et au traitement de grands volumes de données (Big Data socio-économique).
        """)

        st.markdown("### 🌍 2. Organisations Internationales & Régionales")
        st.markdown("""
        * **Communautés Économiques (CEDEAO, UEMOA, Secrétariat de la ZLECAf) :** Études sur l'intégration régionale, les corridors de libre-échange et les barrières non tarifaires.
        * **Agences de Développement (PNUD, Banque Mondiale, BAD, GIZ) :** Co-signature d'études d'impact, consultances sur-mesure et mise en place de plateformes de données.
        """)

    with col_w2:
        st.markdown("### 🎓 3. Universités, Think Tanks & Réseaux de Recherche")
        st.markdown("""
        * **Centres de Recherche & Universités d'Afrique et d'ailleurs (ex. AERC) :** Partenariats scientifiques, publications conjointes de working papers et codirection de thèses/mémoires appliqués.
        * **Think Tanks & Observatoires Économiques :** Synergies pour la rédaction de notes d'orientation politique (*Policy Briefs*) de haut niveau.
        """)

        st.markdown("### 💼 4. Secteur Privé, Banques & Cabinets de Conseil")
        st.markdown("""
        * **Banques Commerciales & Fonds d'Investissement :** Intégration de nos tableaux de bord SaaS pour l'analyse de risque pays et l'allocation d'actifs.
        * **Cabinets d'Audit & Cabinets Stratégiques :** Partenariats de sous-traitance sur des expertises quantitatives pointues et des enquêtes de terrain complexes.
        """)

    st.divider()
    st.subheader("🚀 Vous souhaitez initier une collaboration ?")
    st.markdown("Nous sommes constamment à la recherche de synergies innovantes. Que vous soyez chercheur, institution, entreprise ou expert indépendant, soumettez votre proposition.")
    
    with st.form("partnership_form"):
        p_name = st.text_input("Nom de l'institution / Organisation / Expert")
        p_email = st.text_input("E-mail professionnel de contact")
        p_type = st.selectbox("Nature de la collaboration envisagée", [
            "Partenariat institutionnel / Recherche", 
            "Consultance conjointe / Appel d'offres", 
            "Intégration technologique / SaaS B2B", 
            "Proposition académique / Publication",
            "Autre forme de collaboration"
        ])
        p_desc = st.text_area("Détails de votre proposition ou projet de collaboration")
        p_submit = st.form_submit_button("Soumettre la proposition de partenariat")
        
        if p_submit:
            if p_email and p_desc:
                save_lead(p_email, p_name, f"Partenariat: {p_type}")
                st.success("✅ Proposition transmise avec succès à la direction d'Impact Lab TOGO. Nous vous contacterons à impactlabtogo@gmail.com sous 48h.")
            else:
                st.error("Veuillez remplir au moins l'e-mail et la description du projet.")

# --- ONGLET 6 : CONSEIL STRATÉGIQUE ---
with tab_conseil:
    st.title("🎯 Conseil Stratégique & Études sur Mesure")
    st.markdown("Vous avez besoin d'une étude d'impact spécifique, d'une modélisation macroéconomique sur-mesure ou d'une analyse de risque pour votre implantation dans la région ?")
    st.markdown("💬 **Contact direct mission conseil :** `impactlabtogo@gmail.com`")
    st.divider()
    
    with st.form("consulting_form"):
        c_name = st.text_input("Nom de l'organisation / Entreprise")
        c_email = st.text_input("E-mail de contact")
        c_project = st.text_area("Décrivez votre besoin ou votre projet d'étude")
        c_submit = st.form_submit_button("Envoyer la demande de mission")
        
        if c_submit:
            if c_email and c_project:
                save_lead(c_email, c_name, "Mission Conseil Sur-Mesure")
                st.success("✅ Votre demande a été transmise. Vous pouvez aussi nous joindre directement à impactlabtogo@gmail.com")
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
st.sidebar.markdown("---")
st.sidebar.markdown("**Contact Officiel :**\nimpactlabtogo@gmail.com")
