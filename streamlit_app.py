import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Competition Ready Checklist", page_icon="🏃‍♂️", layout="centered")

# Style CSS personnalisé pour coller au design "Elite"
st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    .stHeader {
        font-family: 'Inter', sans-serif;
    }
    .phase-title {
        color: #dc2626;
        font-weight: 900;
        letter-spacing: -0.05em;
        font-style: italic;
    }
    .time-badge {
        background-color: #fee2e2;
        color: #dc2626;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.7rem;
        font-weight: 800;
        text-transform: uppercase;
    }
    .pro-tip-box {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #f1f5f9;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Données de l'application
sections = [
    {
        "title": "Phase 1 : J-14 à J-7",
        "subtitle": "L'Affûtage & La Fondation",
        "pro_tip": "Le but ici est la fraîcheur. Ne cherche plus à progresser physiquement, mais à arriver reposé et ultra-précis.",
        "categories": {
            "Entraînement & Physio": [
                {"id": "taper", "label": "Phase de Taper", "time": "J-14", "details": "Réduction du volume global. On maintient l'intensité mais on diminue la durée des séances pour laisser le corps surcompenser."},
                {"id": "massage", "label": "Soins des tissus mous", "time": "J-10 Max", "details": "À faire impérativement avant J-10. Après cette limite, le risque de courbatures ou de perte de tonus musculaire est trop important."}
            ],
            "Nutrition & Hygiène": [
                {"id": "sleep_bank", "label": "Sommeil 'Banking'", "time": "J-14 à J-0", "details": "Augmenter le temps de sommeil (9h-10h) deux semaines avant. Améliore les temps de réaction et la précision."}
            ]
        }
    },
    {
        "title": "Phase 2 : J-6 à J-1",
        "subtitle": "La Semaine Critique",
        "pro_tip": "Le sevrage de caféine est difficile les 3 premiers jours, mais le boost le jour J sera ton plus grand avantage nerveux.",
        "categories": {
            "Nutrition & Hydratation": [
                {"id": "carb_load", "label": "Augmentation Glucidique", "time": "J-1", "details": "Cible : 4-5g de glucides / kg de PDC. L'objectif est de maximiser les stocks de glycogène."},
                {"id": "residues", "label": "Régime sans résidus", "time": "J-2", "details": "Élimine les fibres pour vider le tractus intestinal. Gain potentiel de 500g à 1kg de poids mort."},
                {"id": "sodium", "label": "Hyperhydratation sodée", "time": "J-3 à J-1", "details": "Le sodium aide à retenir le fluide dans le plasma sanguin, crucial pour la thermorégulation."},
                {"id": "nitrates_load", "label": "Charge Jus de Betterave", "time": "J-6 à J-1", "details": "1-2 shots/jour (300-600mg nitrates). Améliore l'économie de l'effort et l'utilisation de l'ATP Pcr."}
            ],
            "Suppléments & Logistique": [
                {"id": "cafeine_reset", "label": "Arrêt de la Caféine", "time": "J-7 à J-2", "details": "Se sevrer une semaine avant pour resensibiliser les récepteurs. Le boost du jour J sera explosif."},
                {"id": "creatine", "label": "Maintien Créatine", "time": "Quotidien", "details": "Maintenir la dose de croisière (3-5g). Ne commence surtout pas maintenant."},
                {"id": "gear_check", "label": "Check-up Matériel", "time": "J-2", "details": "Rien de nouveau le jour J. Vérifie tes chaussures, tes straps et ta nutrition."}
            ]
        }
    },
    {
        "title": "Phase 3 : Le Jour J",
        "subtitle": "Avant l'épreuve",
        "pro_tip": "Respecte scrupuleusement le timing du dernier shot de betterave. L'effet de pic est une fenêtre physiologique précise.",
        "categories": {
            "Chronologie Nutritionnelle": [
                {"id": "pre_meal", "label": "Repas Pré-compétition", "time": "H-4 à H-3", "details": "Riz blanc, compote, blanc de poulet. Facile à digérer, énergie rapide."},
                {"id": "nitrate_final", "label": "Nitrate Shot Final", "time": "H-2.5", "details": "Le pic de nitrates plasmatiques survient 2 à 3h après l'ingestion."},
                {"id": "cafeine_final", "label": "Caféine Elite", "time": "H-1", "details": "Dosage : 3 mg / kg de poids de corps. Réduction de la perception de l'effort (RPE)."},
                {"id": "tampon", "label": "Tampon Acide", "time": "H-1", "details": "Bicarbonate ou Beta-Alanine si épreuve lactique. Attention aux troubles gastriques."}
            ],
            "Échauffement (Warm-up)": [
                {"id": "racs", "label": "RACs Full-Body", "time": "H-30 min", "details": "Mobilisation articulaire complète sans créer de fatigue nerveuse."},
                {"id": "pap_cap", "label": "PAP Capsulaire", "time": "H-15 min", "details": "Contraction PAILs épaule spécifique pour préparer le grip."},
                {"id": "plio", "label": "Pliométrie extensive", "time": "H-10 min", "details": "Sauts intensité moyenne pour réveiller les tendons."},
                {"id": "pap_muscular", "label": "PAP Musculaire", "time": "H-5 min", "details": "Intensité max, volume bas (sprints/sauts) pour la potentiation nerveuse."},
                {"id": "thermal", "label": "Veste thermique", "time": "Départ", "details": "Garde tes muscles au chaud jusqu'à la dernière seconde."}
            ]
        }
    },
    {
        "title": "Phase 4 : En Course",
        "subtitle": "Gestion & Entre-runs",
        "pro_tip": "Le 'Mouth Rinsing' trompe ton cerveau en lui faisant croire que de l'énergie arrive sans peser sur ton estomac.",
        "categories": {
            "Protocole Entre 2 Runs": [
                {"id": "active_recov", "label": "Récupération Active", "time": "H + 2 min", "details": "Marche active et respiration nasale pour évacuer les déchets métaboliques."},
                {"id": "hydro_electro", "label": "Hydratation Sodée", "time": "H + 5 min", "details": "Eau riche en sodium/bicarbonates (Vichy) pour tamponner l'acidité."},
                {"id": "refuel", "label": "Apport Énergie", "time": "H + 10 min", "details": "Demi-banane ou miel seulement si nécessaire. Priorité au sang dans les muscles."},
                {"id": "mouth_rinse", "label": "Relance & Rinçage", "time": "H - 5 min", "details": "Rinçage de bouche sucré (recracher). Relance nerveuse par petits sauts."}
            ],
            "Mental": [
                {"id": "self_talk", "label": "Self-Talk Positif", "time": "Pendant", "details": "Dialogue interne instructif axé sur les consignes techniques."}
            ]
        }
    }
]

# Header
st.markdown('<h1 class="phase-title">COMPETITION READY.</h1>', unsafe_allow_html=True)
st.write("CHECKLIST ELITE PREPARATION")

# Navigation par Onglets (Tabs)
tabs = st.tabs([f"Phase {i+1}" for i in range(len(sections))])

for i, tab in enumerate(tabs):
    with tab:
        current_phase = sections[i]
        
        # Titre de la phase
        st.markdown(f"## {current_phase['title']}")
        st.markdown(f"*{current_phase['subtitle']}*")
        
        # Barre de progression fictive par phase
        progress = 0
        
        # Affichage des catégories
        for cat_name, items in current_phase['categories'].items():
            st.markdown(f"### {cat_name}")
            
            for item in items:
                col1, col2 = st.columns([0.8, 0.2])
                
                with col1:
                    # Checkbox pour l'étape
                    is_checked = st.checkbox(f"{item['label']}", key=item['id'])
                    st.markdown(f"<span class='time-badge'>{item['time']}</span>", unsafe_allow_html=True)
                
                with col2:
                    # Expander pour les détails (équivalent du bouton 'i')
                    with st.expander("Détails"):
                        st.write(item['details'])
        
        # Conseil Pro
        st.markdown(f"""
            <div class="pro-tip-box">
                <p style="color:#dc2626; font-weight:900; font-size:0.7rem; text-transform:uppercase; margin-bottom:5px;">Conseil Pro Phase {i+1}</p>
                <p style="font-size:0.85rem; font-weight:600; color:#334155;">"{current_phase['pro_tip']}"</p>
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; color:#94a3b8; font-size:0.7rem; font-weight:900; text-transform:uppercase; letter-spacing:0.2em;'>Next Athlete Performance System v1.0</p>", unsafe_allow_html=True)
