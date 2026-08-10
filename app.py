import streamlit as st

st.set_page_config(page_title="AfriDataMetrics | Impact Lab TOGO", layout="wide")

# Données expertes complètes pour les 15 pays de la CEDEAO
cedeao_full_data = {
    "Togo": {
        "Indicateurs": {"Inflation": "2.7%", "PIB": "5.6%", "Solde Budg.": "-3.8%", "Change": "Stable"},
        "Analyse": "La dynamique inflationniste est maîtrisée grâce à une politique monétaire prudente de la BCEAO et un approvisionnement régulier des marchés locaux. Toutefois, la vigilance s'impose sur le solde budgétaire, fortement impacté par les investissements infrastructurels, afin de préserver la viabilité de la dette à moyen terme.",
        "Points": [3.2, 3.0, 2.8, 2.5, 2.7, 2.6, 2.4]
    },
    "Côte d'Ivoire": {
        "Indicateurs": {"Inflation": "3.1%", "PIB": "6.8%", "Solde Budg.": "-4.2%", "Change": "Stable"},
        "Analyse": "L'économie ivoirienne affiche une résilience remarquable portée par le dynamisme de la filière agro-industrielle et des investissements publics. La maîtrise des prix alimentaires doit rester la priorité pour maintenir le pouvoir d'achat urbain.",
        "Points": [3.5, 3.3, 3.2, 3.0, 3.1, 3.2, 3.3]
    },
    "Sénégal": {
        "Indicateurs": {"Inflation": "2.9%", "PIB": "7.2%", "Solde Budg.": "-5.1%", "Change": "Stable"},
        "Analyse": "L'entrée en production imminente des hydrocarbures redessine les perspectives macroéconomiques. Il est recommandé d'accompagner cette transition par une stricte discipline budgétaire pour éviter les risques de surchauffe.",
        "Points": [3.0, 2.9, 2.8, 2.8, 2.9, 2.9, 2.8]
    },
    "Bénin": {
        "Indicateurs": {"Inflation": "2.8%", "PIB": "6.3%", "Solde Budg.": "-4.0%", "Change": "Stable"},
        "Analyse": "Les performances du port de Cotonou et les réformes logistiques soutiennent l'activité. La consolidation budgétaire progresse conformément aux critères de convergence de l'UEMOA.",
        "Points": [3.1, 3.0, 2.9, 2.7, 2.8, 2.7, 2.6]
    },
    "Burkina Faso": {
        "Indicateurs": {"Inflation": "3.4%", "PIB": "5.1%", "Solde Budg.": "-5.5%", "Change": "Stable"},
        "Analyse": "Malgré les défis sécuritaires, l'économie fait preuve d'une forte résilience, soutenue par le secteur aurifère. Une attention particulière doit être portée à la gestion des tensions sur les prix de première nécessité.",
        "Points": [3.8, 3.6, 3.5, 3.2, 3.4, 3.5, 3.3]
    },
    "Mali": {
        "Indicateurs": {"Inflation": "3.2%", "PIB": "4.8%", "Solde Budg.": "-4.7%", "Change": "Stable"},
        "Analyse": "L'activité économique reste contrainte par les chocs exogènes et énergétiques. La diversification des sources d'approvisionnement et le soutien à la production agricole locale sont des impératifs stratégiques.",
        "Points": [3.4, 3.3, 3.1, 3.0, 3.2, 3.1, 3.0]
    },
    "Niger": {
        "Indicateurs": {"Inflation": "3.5%", "PIB": "6.5%", "Solde Budg.": "-4.8%", "Change": "Stable"},
        "Analyse": "Le secteur extractif (pétrole) constitue le principal moteur de la croissance à court terme. Les politiques publiques doivent cibler l'optimisation des recettes intérieures pour financer le développement social.",
        "Points": [3.0, 3.1, 3.2, 3.3, 3.5, 3.6, 3.4]
    },
    "Guinée-Bissau": {
        "Indicateurs": {"Inflation": "4.0%", "PIB": "4.5%", "Solde Budg.": "-4.5%", "Change": "Stable"},
        "Analyse": "La campagne de commercialisation de l'anacarde conditionne l'équilibre macroéconomique global. Des réformes structurelles dans la gouvernance financière sont indispensables pour stabiliser le cadre budgétaire.",
        "Points": [4.5, 4.3, 4.1, 3.9, 4.0, 3.8, 3.7]
    },
    "Ghana": {
        "Indicateurs": {"Inflation": "18.5%", "PIB": "4.2%", "Solde Budg.": "-6.5%", "Change": "Dépréciation"},
        "Analyse": "Une pression inflationniste persistante nécessite des ajustements structurels rigoureux. La priorité absolue doit être accordée à la stricte consolidation budgétaire et au resserrement prudentiel pour stabiliser la monnaie nationale et ancrer les anticipations.",
        "Points": [22.0, 20.5, 19.8, 19.0, 18.5, 17.8, 17.0]
    },
    "Nigeria": {
        "Indicateurs": {"Inflation": "22.4%", "PIB": "3.3%", "Solde Budg.": "-4.6%", "Change": "Volatile"},
        "Analyse": "Les réformes audacieuses sur les subventions et le marché des changes créent des tensions inflationnistes transitoires mais assainissent les fondamentaux à long terme. Le suivi de la pauvreté et la protection des populations vulnérables s'avèrent critiques.",
        "Points": [21.0, 21.5, 21.8, 22.0, 22.4, 22.8, 23.0]
    },
    "Guinée": {
        "Indicateurs": {"Inflation": "5.2%", "PIB": "5.5%", "Solde Budg.": "-2.1%", "Change": "Stable"},
        "Analyse": "Portée par les megas-projets de bauxite et de fer, l'économie maintient un rythme satisfaisant. Le défi réside dans l'intégration locale de la chaîne de valeur minière pour maximiser les retombées socio-économiques.",
        "Points": [5.5, 5.4, 5.3, 5.2, 5.2, 5.1, 5.0]
    },
    "Sierra Leone": {
        "Indicateurs": {"Inflation": "25.1%", "PIB": "3.8%", "Solde Budg.": "-5.2%", "Change": "Dépréciation"},
        "Analyse": "L'inflation élevée pèse lourdement sur le pouvoir d'achat. Une coordination étroite entre la banque centrale et le ministère des finances est requise pour juguler la monétisation du déficit budgétaire.",
        "Points": [28.0, 27.0, 26.5, 25.8, 25.1, 24.5, 24.0]
    },
    "Libéria": {
        "Indicateurs": {"Inflation": "7.3%", "PIB": "4.7%", "Solde Budg.": "-3.9%", "Change": "Stable"},
        "Analyse": "L'amélioration de la gouvernance macroéconomique et l'apurement des arriérés intérieurs soutiennent la reprise. Des efforts accrus sont nécessaires pour renforcer l'infrastructure de base et diversifier les sources de croissance.",
        "Points": [6.8, 7.0, 7.1, 7.2, 7.3, 7.5, 7.4]
    },
    "Gambie": {
        "Indicateurs": {"Inflation": "6.0%", "PIB": "5.2%", "Solde Budg.": "-4.3%", "Change": "Stable"},
        "Analyse": "Le tourisme et les transferts de fonds de la diaspora continuent de soutenir l'activité. La viabilité de la dette publique reste un point de vigilance qui nécessite une rationalisation continue des dépenses courantes.",
        "Points": [6.5, 6.3, 6.2, 6.1, 6.0, 5.9, 5.8]
    },
    "Cap-Vert": {
        "Indicateurs": {"Inflation": "2.2%", "PIB": "4.8%", "Solde Budg.": "-3.2%", "Change": "Fixe (Euro)"},
        "Analyse": "La forte reprise du secteur touristique tire l'économie insulaire vers le haut. L'arrimage de l'escudo à l'euro garantit une stabilité des prix remarquable, bien que la vulnérabilité aux chocs extérieurs demeure élevée.",
        "Points": [2.5, 2.4, 2.3, 2.2, 2.2, 2.1, 2.0]
    }
}

# Barre latérale
st.sidebar.title("🌍 Centre Régional CEDEAO")
pays = st.sidebar.selectbox("Sélectionnez un pays :", list(cedeao_full_data.keys()))

st.sidebar.divider()
st.sidebar.subheader("📄 Rapport Exécutif")
if st.sidebar.button("🖨️ Imprimer / Exporter en PDF"):
    st.markdown("<script>window.print();</script>", unsafe_allow_html=True)

# Rubrique Nous Contacter intégrée proprement dans la sidebar
st.sidebar.divider()
st.sidebar.subheader("📬 Nous Contacter")
st.sidebar.markdown(
    "Pour toute proposition de partenariat ou accès institutionnel :<br>"
    "📧 **impactlabtogo@gmail.com**",
    unsafe_allow_html=True
)

# Design
st.markdown("""
    <style>
    .brand-badge { display: inline-block; background-color: #EFF6FF; color: #1D4ED8; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; margin-bottom: 20px; border: 1px solid #BFDBFE; }
    @media print { .stSidebar, button { display: none !important; } }
    </style>
""", unsafe_allow_html=True)

st.markdown(f'<div class="brand-badge">🚀 AfriDataMetrics &bull; Intelligence Économique par Impact Lab TOGO</div>', unsafe_allow_html=True)
st.title(f"📊 Analyse : {pays}")

# Indicateurs macroéconomiques
c1, c2, c3, c4 = st.columns(4)
c1.metric("Inflation Actuelle", cedeao_full_data[pays]["Indicateurs"]["Inflation"])
c2.metric("Croissance PIB", cedeao_full_data[pays]["Indicateurs"]["PIB"])
c3.metric("Solde Budgétaire", cedeao_full_data[pays]["Indicateurs"]["Solde Budg."])
c4.metric("Tendance Change", cedeao_full_data[pays]["Indicateurs"]["Change"])

st.divider()

# Analyse & Recommandations stratégiques
st.subheader("💡 Analyse & Recommandations Stratégiques")
st.info(cedeao_full_data[pays]["Analyse"])

# Modélisation prédictive
st.subheader("📉 Modélisation Prédictive")
st.write("Les projections à moyen terme mettent en évidence une trajectoire de convergence progressive des indices de prix, sous réserve de la poursuite des réformes structurelles et de la stabilité des cours des matières premières sur les marchés internationaux.")

# Graphique interactif
points = cedeao_full_data[pays]["Points"]
chart_html = f"""
<div style="background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #E5E7EB;">
    <canvas id="macroChart" width="400" height="130"></canvas>
</div>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
const ctx = document.getElementById('macroChart').getContext('2d');
new Chart(ctx, {{
    type: 'line',
    data: {{
        labels: ['2025-01', '2025-04', '2025-07', '2025-10', '2026-01', '2026-04 (Prév.)', '2026-07 (Prév.)'],
        datasets: [{{
            label: 'Inflation (Glissement annuel %)',
            data: {points},
            borderColor: '#1D4ED8',
            backgroundColor: 'rgba(29, 78, 216, 0.06)',
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