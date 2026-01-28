import streamlit as st
import time

# --- Configuration de la page et injection de Tailwind CSS ---
st.set_page_config(page_title="Competition Ready", layout="centered", page_icon="🔥")

# On injecte Tailwind CSS via CDN pour garder le design exact
# Note : En Streamlit, les animations (transitions fluides) ne seront pas aussi lisses qu'en React 
# car Streamlit recharge la portion de code à chaque interaction.
st.markdown("""
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* On nettoie un peu le style par défaut de Streamlit pour coller au design */
        .stApp {
            background-color: #f8fafc; /* bg-slate-50 */
            color: #0f172a; /* text-slate-900 */
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 5rem;
            max-width: 32rem; /* max-w-md */
        }
        /* Cacher les styles de boutons Streamlit par défaut pour certains éléments */
        div[data-testid="stVerticalBlock"] > div > button {
             border: none;
        }
    </style>
""", unsafe_allow_html=True)

# --- Données (Identiques à l'original) ---

# Tableaux HTML complexes stockés en variables pour la lisibilité
TABLEAU_RESIDUS = """
<div class="rounded-lg border border-slate-200 overflow-hidden mb-4">
    <table class="w-full text-[10px] text-left border-collapse">
      <thead>
        <tr class="bg-red-50 text-red-800 border-b border-red-100">
          <th class="p-2 font-bold w-1/3">Catégorie (Stop)</th>
          <th class="p-2 font-bold">Exemples</th>
          <th class="p-2 font-bold">Pourquoi stopper</th>
        </tr>
      </thead>
      <tbody class="bg-white">
        <tr class="border-b border-slate-100"><td class="p-2 font-bold text-slate-700">Fibres insolubles</td><td class="p-2 text-slate-600">Légumes crus (brocoli, chou), graines</td><td class="p-2 text-slate-500">↑ volume, ballonnements</td></tr>
        <tr class="border-b border-slate-100"><td class="p-2 font-bold text-slate-700">Légumineuses</td><td class="p-2 text-slate-600">Lentilles, pois chiches</td><td class="p-2 text-slate-500">↑ gaz + digestion lente</td></tr>
        <tr class="border-b border-slate-100"><td class="p-2 font-bold text-slate-700">Céréales complètes</td><td class="p-2 text-slate-600">Riz complet, avoine complet</td><td class="p-2 text-slate-500">↑ contenu intestinal</td></tr>
      </tbody>
    </table>
</div>
<div class="rounded-lg border border-slate-200 overflow-hidden">
    <table class="w-full text-[10px] text-left border-collapse">
      <thead>
        <tr class="bg-green-50 text-green-800 border-b border-green-100">
          <th class="p-2 font-bold w-1/3">Objectif (Go)</th>
          <th class="p-2 font-bold">Aliments recommandés</th>
          <th class="p-2 font-bold">Notes pratiques</th>
        </tr>
      </thead>
      <tbody class="bg-white">
        <tr class="border-b border-slate-100"><td class="p-2 font-bold text-slate-700">Glucides digestibles</td><td class="p-2 text-slate-600">Riz blanc, pâtes blanches, banane</td><td class="p-2 text-slate-500">Énergie intacte</td></tr>
        <tr class="border-b border-slate-100"><td class="p-2 font-bold text-slate-700">Protéines faciles</td><td class="p-2 text-slate-600">Poulet, dinde, œufs, whey</td><td class="p-2 text-slate-500">Digestion rapide</td></tr>
      </tbody>
    </table>
</div>
"""

SECTIONS = [
    {
        "title": "Phase 1 : J-14 à J-7",
        "subtitle": "L'Affûtage & La Fondation",
        "icon": "Activity",
        "proTip": "Le but ici est la fraîcheur. On ne cherche plus à progresser physiquement, mais à arriver reposé et ultra-performant.",
        "categories": [
            {"name": "Entraînement & Physio", "items": [{"id": "taper", "label": "Phase de Taper", "time": "J-14 ou J-7", "desc": "Réduction drastique du volume d'entraînement.", "details": "Réduction du volume global en maintenant l'intensité"}]},
            {"name": "Nutrition & Hygiène", "items": [{"id": "sleep_bank", "label": "Sommeil 'Banking'", "time": "J-14 à J-0", "desc": "Cherche à 'stocker' du sommeil.", "details": "<p>Cherche à stocker du sommeil.</p><p class='mt-1'>Vise +45 à +90 min/nuit.</p><p class='mt-1'>La régularité > Quantité absolue.</p>"}]}
        ]
    },
    {
        "title": "Phase 2 : J-6 à J-1",
        "subtitle": "La Semaine Critique",
        "icon": "Zap",
        "proTip": "Tout le monde est prêt physiquement. Ceux qui gagnent sont ceux qui optimisent les détails que les autres négligent.",
        "categories": [
            {
                "name": "Nutrition & Hydratation",
                "items": [
                    {"id": "nitrates_load", "label": "Charge de Jus de Betterave", "time": "J-6 à J-1", "desc": "Saturer le corps en nitrates (1-2 shots/jour).", "details": "<p>70-140 ml/jour pour augmenter l'oxyde nitrique.</p><p class='mt-1 text-red-600 font-semibold'>Attention : Éviter bains de bouche antiseptiques.</p>"},
                    {"id": "sodium", "label": "Hyperhydratation sodée", "time": "J-3 à J-1", "desc": "Eau riche en sodium ou électrolytes.", "details": "Bois de l'eau riche en sodium ou ajoute des électrolytes à ton hydratation."},
                    {"id": "residues", "label": "Régime sans résidus", "time": "J-2", "desc": "Élimine les fibres (légumes crus, grains entiers).", "details": f"<p class='mb-4'>Élimine les fibres pour vider le tractus intestinal. Gain possible : 500g à 1kg.</p>{TABLEAU_RESIDUS}"},
                    {"id": "carb_load", "label": "Augmentation Glucidique Contrôlée", "time": "J-1", "desc": "Cible : 4-5g de glucides / kg de PDC.", "details": "<p>Cible : 4-5g de glucides / kg de PDC.</p><p class='mt-1'>Dernier gros apport ≥6 h avant coucher.</p>"},
                ]
            },
            {
                "name": "Suppléments & Logistique",
                "items": [
                    {"id": "cafeine_reset", "label": "Arrêt de la Caféine", "time": "J-7 à J-2", "desc": "'Caffeine reset' pour la sensibilité.", "details": "<p>Se sevrer une semaine avant.</p><p class='mt-1'>Réduire à ≤50 mg/j si nécessaire, pas arrêt total.</p>"},
                    {"id": "creatine", "label": "Maintien Créatine", "time": "Quotidien", "desc": "Maintenir la dose de croisière (3-5g).", "details": "<p>Si tu en prends déjà, maintenir la dose.</p><p class='mt-1 text-red-600 font-semibold'>Ne pas commencer maintenant si tu n'en consommes pas.</p>"},
                    {"id": "gear_check", "label": "Check-up Matériel", "time": "J-1", "desc": "Vérification complète.", "details": "<p>Chaussures, straps, nutrition. Rien de nouveau le jour J.</p>"}
                ]
            }
        ]
    },
    {
        "title": "Phase 3 : Le Jour J",
        "subtitle": "Avant l'épreuve",
        "icon": "Flame",
        "proTip": "L'objectif de l'échauffement est l'excitation neuronale, pas la fatigue.",
        "categories": [
            {
                "name": "Chronologie Nutritionnelle",
                "items": [
                    {"id": "pre_meal", "label": "Repas Pré-compétition", "time": "H-4 à H-3", "desc": "Glucides ++, pauvre en lipides/fibres.", "details": "<p>Riche glucides, modéré protéines, très pauvre lipides.</p><p class='mt-1'>Ex: Riz blanc, compote, poulet.</p>"},
                    {"id": "nitrate_final", "label": "Dernier shot de betterave", "time": "H-2.5", "desc": "Dernier shot concentré.", "details": "<p>Pic de nitrates plasmatiques 2 à 3h après ingestion.</p>"},
                    {"id": "cafeine_final", "label": "Caféine Elite", "time": "H-1", "desc": "Dosage : 3 mg / kg de poids de corps.", "details": "<p>Effet : Réduction de la perception de l'effort (RPE).</p>"}
                ]
            },
            {
                "name": "Échauffement (Warm-up)",
                "items": [
                    {"id": "racs", "label": "RACs Full-Body", "time": "H-30 min", "desc": "Mobilisation articulaire complète.", "details": "Échauffement articulaire complet."},
                    {"id": "pap_cap", "label": "PAP Capsulaire", "time": "H-15 min", "desc": "Effort max sur contraction PAILs.", "details": "<p>Effort max contraction.</p><p class='mt-1 font-semibold text-red-600'>Attention : Volume minimal pour ne pas cramer le système nerveux.</p>"},
                    {"id": "plio", "label": "Pliométrie extensive", "time": "H-10 min", "desc": "Sauts intensité moyenne.", "details": "Volume sans aller à la fatigue."},
                    {"id": "pap_muscular", "label": "PAP Musculaire", "time": "H-5 min", "desc": "Intensité max, volume très bas.", "details": "Intensité max, volume bas (sprints)."},
                    {"id": "thermal", "label": "Veste thermique", "time": "Départ", "desc": "Garder le corps au chaud.", "details": "Garder le corps au chaud jusqu'au bout."}
                ]
            }
        ]
    },
    {
        "title": "Phase 4 : En Course",
        "subtitle": "Gestion & Entre-runs",
        "icon": "Brain",
        "proTip": "Quand l’épreuve s’étire, la différence se joue dans la gestion entre les runs.",
        "categories": [
            {
                "name": "Protocole Entre 2 Runs",
                "items": [
                    {"id": "active_recov", "label": "Récupération Active", "time": "H + 2 min", "desc": "Marche active. Ne t'assois pas.", "details": "<p>Marche active.</p><p class='mt-1'>Respire par le nez.</p>"},
                    {"id": "hydro_electro", "label": "Hydratation", "time": "H + 5 min", "desc": "200-300ml d'eau + électrolytes.", "details": "<p>Eau + électrolytes ou Vichy Célestins.</p>"},
                    {"id": "refuel", "label": "Apport Énergie", "time": "H + 10 min", "desc": "Demi-banane ou miel si nécessaire.", "details": "<p>Si vide : demi-banane. Si bien : rien de solide.</p>"},
                    {"id": "mouth_rinse", "label": "Relance", "time": "H - 5 min", "desc": "Rinçage de bouche sucré.", "details": "<p>Rinçage sucré (recracher). Remise en mouvement.</p>"}
                ]
            },
            {
                "name": "Mental In-Game",
                "items": [
                    {"id": "self_talk", "label": "Self-Talk Positif", "time": "Pendant", "desc": "Dialogue interne instructif.", "details": "<p>Focus sur les consignes techniques et l'instant présent.</p>"}
                ]
            }
        ]
    }
]

# --- Gestion de l'état (State Management) ---

if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 0
if 'checked_items' not in st.session_state:
    st.session_state.checked_items = {}
if 'expanded_sections' not in st.session_state:
    # Par défaut, tout est ouvert comme dans le code original
    st.session_state.expanded_sections = {f"{i}-{j}": True for i, phase in enumerate(SECTIONS) for j, cat in enumerate(phase['categories'])}
if 'open_details' not in st.session_state:
    st.session_state.open_details = {}

# Fonctions Helper
def toggle_check(item_id):
    st.session_state.checked_items[item_id] = not st.session_state.checked_items.get(item_id, False)

def toggle_details(item_id):
    st.session_state.open_details[item_id] = not st.session_state.open_details.get(item_id, False)

def toggle_section(key):
    st.session_state.expanded_sections[key] = not st.session_state.expanded_sections.get(key, False)

def calculate_progress(phase_idx):
    phase = SECTIONS[phase_idx]
    total = 0
    checked = 0
    for cat in phase['categories']:
        for item in cat['items']:
            total += 1
            if st.session_state.checked_items.get(item['id'], False):
                checked += 1
    return int((checked / total) * 100) if total > 0 else 0

# --- Rendu de l'Interface ---

# Header
st.markdown("""
    <div class="mb-6 text-center">
      <h1 class="text-3xl font-black tracking-tighter text-red-600 italic leading-none">COMPETITION READY.</h1>
      <h2 class="text-sm font-bold text-slate-400 uppercase tracking-[0.3em]">Checklist</h2>
    </div>
""", unsafe_allow_html=True)

# Navigation (Tabs)
cols = st.columns(4)
for i, section in enumerate(SECTIONS):
    is_active = st.session_state.active_tab == i
    # Icônes (simulation texte/emoji pour simplifier sans SVG externe complexe)
    icons = {"Activity": "📉", "Zap": "⚡", "Flame": "🔥", "Brain": "🧠"}
    icon = icons.get(section['icon'], "•")
    
    with cols[i]:
        # Astuce : On utilise un bouton vide pour le clic, mais on style avec Markdown
        btn_label = f"{icon}\nPhase {i+1}"
        if st.button(btn_label, key=f"tab_{i}", use_container_width=True, type="primary" if is_active else "secondary"):
            st.session_state.active_tab = i
            st.rerun()

# Vue de la phase active
active_data = SECTIONS[st.session_state.active_tab]
progress = calculate_progress(st.session_state.active_tab)

# Barre de progression et Titre Phase
st.markdown(f"""
    <div class="mb-6 px-2 mt-4">
      <div class="flex justify-between items-end mb-2">
        <div>
          <h3 class="text-2xl font-black text-slate-800 tracking-tight leading-none">{active_data['title']}</h3>
          <p class="text-red-500 font-bold text-xs uppercase mt-1 tracking-wider">{active_data['subtitle']}</p>
        </div>
        <span class="text-xs font-black text-slate-300 tracking-tighter">{progress}%</span>
      </div>
      <div class="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden">
        <div class="h-full bg-red-600 transition-all duration-700 ease-out" style="width: {progress}%"></div>
      </div>
    </div>
""", unsafe_allow_html=True)

# Catégories et Items
for cat_idx, category in enumerate(active_data['categories']):
    section_key = f"{st.session_state.active_tab}-{cat_idx}"
    is_expanded = st.session_state.expanded_sections.get(section_key, True)

    # Container de section (Styling visuel)
    with st.container():
        # En-tête de section cliquable (simulation)
        col_title, col_arrow = st.columns([8, 1])
        with col_title:
             st.markdown(f'<span class="font-black text-[10px] uppercase tracking-[0.15em] text-slate-400">{category["name"]}</span>', unsafe_allow_html=True)
        with col_arrow:
             if st.button("▼" if is_expanded else "▶", key=f"btn_sec_{section_key}"):
                 toggle_section(section_key)
                 st.rerun()

        if is_expanded:
            st.markdown('<div class="p-1 space-y-2">', unsafe_allow_html=True)
            for item in category['items']:
                is_checked = st.session_state.checked_items.get(item['id'], False)
                is_details_open = st.session_state.open_details.get(item['id'], False)
                
                # Styles dynamiques
                bg_color = "bg-red-50/50" if is_checked else "bg-white hover:bg-slate-50"
                text_color = "text-red-700" if is_checked else "text-slate-800"
                icon_check = "🔴" if is_checked else "⚪" # Remplacement visuel des icônes Lucide

                # Structure de l'item en colonnes Streamlit pour l'interactivité
                c1, c2 = st.columns([1, 6])
                
                # Rendu visuel de la carte
                with st.container():
                    # Checkbox simulée par un bouton
                    with c1:
                        if st.button(icon_check, key=f"check_{item['id']}"):
                            toggle_check(item['id'])
                            st.rerun()
                    
                    # Contenu texte + Bouton info
                    with c2:
                        sub_c1, sub_c2 = st.columns([5, 1])
                        with sub_c1:
                            st.markdown(f"""
                                <div class="flex flex-col">
                                    <span class="text-[9px] font-black text-red-500 uppercase tracking-tighter mb-0.5">{item['time']}</span>
                                    <p class="font-bold text-sm leading-tight transition-colors {text_color}">{item['label']}</p>
                                </div>
                            """, unsafe_allow_html=True)
                        with sub_c2:
                            if st.button("ℹ️", key=f"info_{item['id']}"):
                                toggle_details(item['id'])
                                st.rerun()
                
                # Détails (Accordion custom)
                if is_details_open:
                    st.markdown(f"""
                        <div class="ml-2 mt-2 p-4 bg-white/80 border-t border-slate-50 rounded-b-xl text-[11px] text-slate-600 leading-relaxed font-medium">
                            {item['details']}
                        </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("<div class='mb-3'></div>", unsafe_allow_html=True) # Espacement

            st.markdown('</div>', unsafe_allow_html=True)
            
    st.markdown("---") # Séparateur visuel entre sections

# Footer Conseil Pro
st.markdown(f"""
    <div class="mt-8 p-5 bg-white rounded-3xl border border-slate-100 shadow-xl relative overflow-hidden flex gap-4">
      <div class="bg-red-600 p-2.5 rounded-2xl text-white shadow-lg shadow-red-100 self-start" style="min-width: 40px; text-align: center;">
        🛡️
      </div>
      <div>
        <h4 class="font-black text-[10px] uppercase tracking-widest text-red-600">Conseil Pro Phase {st.session_state.active_tab + 1}</h4>
        <p class="text-[11px] leading-relaxed mt-1 font-bold text-slate-700 italic">
          "{active_data['proTip']}"
        </p>
      </div>
    </div>
    <p class="text-center text-slate-300 text-[9px] font-black uppercase tracking-[0.3em] mt-8 mb-12">
      Next Athlete Performance System v1.0
    </p>
""", unsafe_allow_html=True)
