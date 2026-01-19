import streamlit as st
import json
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="COMPETITION READY - Next Athlete",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personnalisé
st.markdown("""
<style>
    body {
        background-color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    .main {
        max-width: 600px;
        margin: 0 auto;
    }
    .header-title {
        font-size: 2.5rem;
        font-weight: 900;
        color: #dc2626;
        text-align: center;
        font-style: italic;
        letter-spacing: -1px;
        margin-bottom: 0.5rem;
    }
    .header-subtitle {
        font-size: 0.85rem;
        font-weight: 700;
        color: #9ca3af;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 0.15em;
    }
</style>
""", unsafe_allow_html=True)

# Initialisation de la session
if 'checked_items' not in st.session_state:
    st.session_state.checked_items = {}
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 0
if 'expanded_sections' not in st.session_state:
    st.session_state.expanded_sections = {"0-0": True, "1-0": True, "2-0": True, "3-0": True}
if 'open_details' not in st.session_state:
    st.session_state.open_details = {}

# Données des phases
sections = [
    {
        "title": "Phase 1 : J-14 à J-7",
        "subtitle": "L'Affûtage & La Fondation",
        "icon": "🏃",
        "proTip": "Le but ici est la fraîcheur. Ne cherche plus à progresser physiquement, mais à arriver reposé et ultra-précis.",
        "categories": [
            {
                "name": "Entraînement & Physio",
          items: [
                    {
                        "id": "taper",
                        "label": "Phase de Taper",
                        "time": "J-14",
                        "desc": "Réduction drastique du volume d'entraînement.",
                        "details": "Réduction du volume global. On maintient l'intensité mais on diminue la durée des séances pour laisser le corps surcompenser."
                    },
                    {
                        "id": "massage",
                        "label": "Soins des tissus mous",
                        "time": "J-10 Max",
                        "desc": "Dernier massage profond (Deep Tissue).",
                        "details": "À faire impérativement avant J-10. Après cette limite, le risque de courbatures ou de perte de tonus musculaire (effet 'jambes molles') est trop important."
},
            {
                "id": "sleep_bank",
                "label": "Sommeil 'Banking'",
                "time": "J-14 à J-0",
                "desc": "Cherche à 'stocker' du sommeil.",
                "details": "Augmenter le temps de sommeil (9h-10h) deux semaines avant. Améliore les temps de réaction et la précision sur les obstacles techniques."
            }
                ]
            }
        ]
    },
    {
        "title": "Phase 2 : J-6 à J-1",
        "subtitle": "La Semaine Critique",
        "icon": "⚡",
        "proTip": "Le sevrage de caféine est difficile les 3 premiers jours, mais le boost le jour J sera ton plus grand avantage nerveux.",
        "categories": [
            {
                "name": "Nutrition & Hydratation",
                "items": [
                    {
                        "id": "carb_load",
                        "label": "Augmentation Glucidique",
                        "time": "J-1",
                        "desc": "Cible : 4-5g de glucides / kg de PDC.",
                        "details": "L'objectif est de maximiser les stocks de glycogène musculaire et hépatique pour avoir un réservoir d'énergie plein."
                    },
                    {
                        "id": "residues",
                        "label": "Régime sans résidus",
                        "time": "J-2",
                        "desc": "Élimine les fibres (légumes crus, grains entiers).",
                        "details": "Vider le tractus intestinal pour éviter les troubles digestifs. Gain potentiel de 500g à 1kg sur la balance (poids mort intestinal)."
                    },
                    {
                        "id": "sodium",
                        "label": "Hyperhydratation sodée",
                        "time": "J-3 à J-1",
                        "desc": "Eau riche en sodium ou électrolytes.",
                        "details": "Le sodium aide à retenir le fluide dans le plasma sanguin (expansion du volume plasmatique), crucial pour la thermorégulation et le débit cardiaque."
                    },
                    {
                        "id": "nitrates_load",
                        "label": "Charge Jus de Betterave",
                        "time": "J-6 à J-1",
                        "desc": "Saturer le corps en nitrates (1-2 shots/jour).",
                        "details": "70-140 ml (300-600mg nitrates). Vasodilatateur puissant, améliore l'économie de l'effort et l'utilisation de l'ATP Pcr."
                    }
                ]
            },
            {
                "name": "Suppléments & Logistique",
                "items": [
                    {
                        "id": "cafeine_reset",
                        "label": "Arrêt de la Caféine",
                        "time": "J-7 à J-2",
                        "desc": "'Caffeine reset' pour la sensibilité.",
                        "details": "Se sevrer une semaine avant pour resensibiliser les récepteurs à l'adénosine. Le boost du jour J sera explosif."
                    },
                    {
                        "id": "creatine",
                        "label": "Maintien Créatine",
                        "time": "Quotidien",
                        "desc": "Maintenir la dose de croisière (3-5g).",
                        "details": "Si tu en prends déjà, continue. Ne commence surtout pas maintenant pour éviter une rétention d'eau imprévue."
                    },
                    {
                        "id": "gear_check",
                        "label": "Check-up Matériel",
                        "time": "J-2",
                        "desc": "Vérification complète : chaussures, straps, magnésie.",
                        "details": "Rien de nouveau le jour de la compétition. Teste tes straps et ta nutrition une dernière fois."
                    }
                ]
            }
        ]
    },
    {
        "title": "Phase 3 : Le Jour J",
        "subtitle": "Avant l'épreuve",
        "icon": "🔥",
        "proTip": "Respecte scrupuleusement le timing du dernier shot de betterave. L'effet de pic est une fenêtre physiologique précise.",
        "categories": [
            {
                "name": "Chronologie Nutritionnelle",
                "items": [
                    {
                        "id": "pre_meal",
                        "label": "Repas Pré-compétition",
                        "time": "H-4 à H-3",
                        "desc": "Glucides ++, pauvre en lipides/fibres.",
                        "details": "Exemple : Riz blanc, compote, blanc de poulet ou protéine en poudre. Facile à digérer, énergie rapide."
                    },
                    {
                        "id": "nitrate_final",
                        "label": "Nitrate Shot Final",
                        "time": "H-2.5",
                        "desc": "Dernier shot de betterave concentré.",
                        "details": "Le pic de nitrates plasmatiques survient 2 à 3h après l'ingestion. C'est le moment clé pour l'oxyde nitrique."
                    },
                    {
                        "id": "cafeine_final",
                        "label": "Caféine Elite",
                        "time": "H-1",
                        "desc": "Dosage : 3 mg / kg de poids de corps.",
                        "details": "Effet : Réduction de la perception de l'effort (RPE) et mobilisation des acides gras. À prendre avant le run le plus important."
                    },
                    {
                        "id": "tampon",
                        "label": "Tampon Acide",
                        "time": "H-1",
                        "desc": "Bicarbonate ou Beta-Alanine.",
                        "details": "Si l'épreuve est très lactique (1-8 min). Attention : peut causer des troubles gastriques majeurs. À tester impérativement avant."
                    }
                ]
            },
            {
                "name": "Échauffement (Warm-up)",
                "items": [
                    {
                        "id": "racs",
                        "label": "RACs Full-Body",
                        "time": "H-30 min",
                        "desc": "Mobilisation articulaire complète.",
                        "details": "Réveiller chaque articulation sans créer de fatigue nerveuse."
                    },
                    {
                        "id": "pap_cap",
                        "label": "PAP Capsulaire",
                        "time": "H-15 min",
                        "desc": "Effort max sur contraction PAILs.",
                        "details": "Flexion d'épaule et Rotation externe d'épaule spécifique pour préparer le grip et les suspensions."
                    },
                    {
                        "id": "plio",
                        "label": "Pliométrie extensive",
                        "time": "H-10 min",
                        "desc": "Volume bas sur sauts intensité moyenne.",
                        "details": "Réveiller les tendons sans entamer les réserves d'énergie."
                    },
                    {
                        "id": "pap_muscular",
                        "label": "PAP Musculaire & Sprints",
                        "time": "H-5 min",
                        "desc": "Intensité max, volume très bas.",
                        "details": "Quelques sauts max ou sprints courts pour la potentiation nerveuse finale."
                    },
                    {
                        "id": "thermal",
                        "label": "Veste thermique",
                        "time": "Départ",
                        "desc": "Garder le corps au chaud jusqu'au bout.",
                        "details": "Ne laisse pas tes muscles se refroidir pendant l'attente sur la ligne de départ."
                    }
                ]
            }
        ]
    },
    {
        "title": "Phase 4 : En Course",
        "subtitle": "Gestion & Entre-runs",
        "icon": "🧠",
        "proTip": "Le 'Mouth Rinsing' (rinçage de bouche) trompe ton cerveau en lui faisant croire que de l'énergie arrive, sans peser sur ton estomac.",
        "categories": [
            {
                "name": "Protocole Entre 2 Runs",
                "items": [
                    {
                        "id": "active_recov",
                        "label": "Récupération Active",
                        "time": "H + 2 min",
                        "desc": "Marche active. Ne t'assois pas.",
                        "details": "Respiration nasale profonde pour faire redescendre le rythme cardiaque et évacuer les déchets métaboliques."
                    },
                    {
                        "id": "hydro_electro",
                        "label": "Hydratation Sodée",
                        "time": "H + 5 min",
                        "desc": "200-300ml d'eau avec électrolytes.",
                        "details": "Une eau type Vichy Célestins est parfaite pour tamponner l'acidité produite par le premier run."
                    },
                    {
                        "id": "refuel",
                        "label": "Apport Énergie",
                        "time": "H + 10 min",
                        "desc": "Demi-banane ou miel si nécessaire.",
                        "details": "Si tu te sens bien, ne mange rien de solide. Le sang doit rester dans tes muscles, pas dans ton estomac."
                    },
                    {
                        "id": "mouth_rinse",
                        "label": "Relance & Rinçage",
                        "time": "H - 5 min",
                        "desc": "Rinçage de bouche sucré (recracher).",
                        "details": "Dernière relance : petits sauts et rotations articulaires pour préparer le second run."
                    }
                ]
            },
            {
                "name": "Mental In-Game",
                "items": [
                    {
                        "id": "self_talk",
                        "label": "Self-Talk Positif",
                        "time": "Pendant",
                        "desc": "Dialogue interne instructif.",
                        "details": "Focus sur les consignes techniques et l'instant présent plutôt que sur le résultat final."
                    }
                ]
            }
        ]
    }
]

# Fonction pour calculer la progression
def calculate_progress(phase_idx):
    phase = sections[phase_idx]
    total = 0
    checked = 0
    for category in phase["categories"]:
        for item in category["items"]:
            total += 1
            if st.session_state.checked_items.get(item["id"], False):
                checked += 1
    return int((checked / total) * 100) if total > 0 else 0

# En-tête
st.markdown('<div class="header-title">COMPETITION READY.</div>', unsafe_allow_html=True)
st.markdown('<div class="header-subtitle">Checklist</div>', unsafe_allow_html=True)
st.markdown("---")

# Navigation par onglets (Phases)
col1, col2, col3, col4 = st.columns(4)

phases_icons = ["🏃", "⚡", "🔥", "🧠"]
phases_labels = ["Phase 1", "Phase 2", "Phase 3", "Phase 4"]

with col1:
    if st.button(f"{phases_icons[0]}\n{phases_labels[0]}", use_container_width=True, key="tab0"):
        st.session_state.active_tab = 0

with col2:
    if st.button(f"{phases_icons[1]}\n{phases_labels[1]}", use_container_width=True, key="tab1"):
        st.session_state.active_tab = 1

with col3:
    if st.button(f"{phases_icons[2]}\n{phases_labels[2]}", use_container_width=True, key="tab2"):
        st.session_state.active_tab = 2

with col4:
    if st.button(f"{phases_icons[3]}\n{phases_labels[3]}", use_container_width=True, key="tab3"):
        st.session_state.active_tab = 3

st.markdown("---")

# Phase actuelle
active_phase = sections[st.session_state.active_tab]
progress = calculate_progress(st.session_state.active_tab)

col_title, col_progress = st.columns([3, 1])
with col_title:
    st.markdown(f"## {active_phase['title']}")
    st.markdown(f"**{active_phase['subtitle']}**")

with col_progress:
    st.markdown(f"### {progress}%")

st.progress(progress / 100, text=f"Progression: {progress}%")

# Affichage des catégories et éléments
for cat_idx, category in enumerate(active_phase["categories"]):
    section_key = f"{st.session_state.active_tab}-{cat_idx}"

    with st.expander(f"📋 {category['name']}", expanded=st.session_state.expanded_sections.get(section_key, True)):
        for item in category["items"]:
            is_checked = st.session_state.checked_items.get(item["id"], False)

            col1, col2 = st.columns([10, 1])

            with col1:
                checked = st.checkbox(
                    f"**[{item['time']}]** {item['label']}",
                    value=is_checked,
                    key=item["id"]
                )
                st.session_state.checked_items[item["id"]] = checked
                st.caption(item["desc"])

            with col2:
                if st.button("ℹ️", key=f"info_{item['id']}", use_container_width=True):
                    st.session_state.open_details[item["id"]] = not st.session_state.open_details.get(item["id"], False)

            if st.session_state.open_details.get(item["id"], False):
                st.info(item["details"])

st.markdown("---")

# Conseil Pro
st.markdown(f"""
### 💡 Conseil Pro Phase {st.session_state.active_tab + 1}
> *"{active_phase['proTip']}"*
""")

st.markdown("---")
st.markdown('<p style="text-align: center; color: #9ca3af; font-size: 0.8rem;">Next Athlete Performance System v1.0</p>', unsafe_allow_html=True)
