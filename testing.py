import streamlit as st
from html import escape

st.set_page_config(page_title="COMPETITION READY.", layout="centered")

# --- Styles (approximation du design Tailwind) ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap');
    html, body, [class*="st-"]  {
        font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
    }
    .app-container{min-height:100vh; background:#f8fafc; padding:24px 16px 96px; color:#0f172a}
    .card{background: rgba(255,255,255,0.95); border-radius:18px; padding:12px; box-shadow: 0 4px 14px rgba(2,6,23,0.06); border:1px solid rgba(255,255,255,0.8)}
    .tabs{display:flex; gap:8px; margin-bottom:16px}
    .tab{flex:1; padding:10px; border-radius:12px; text-align:center; cursor:pointer}
    .tab.active{background:#fff; color:#dc2626; transform:scale(1.03); box-shadow:0 6px 18px rgba(0,0,0,0.06)}
    .phase-title{font-weight:900; font-size:20px; margin:0}
    .phase-sub{color:#ef4444; font-weight:700; font-size:11px; text-transform:uppercase}
    .progress-wrap{background:#e6edf2; height:10px; border-radius:8px; overflow:hidden}
    .progress-bar{height:100%; background:#dc2626; transition:width 0.7s ease-out}
    .category{margin-top:12px}
    .category-header{display:flex; justify-content:space-between; align-items:center; padding:12px; cursor:pointer}
    .item-row{display:flex; gap:10px; padding:10px; align-items:flex-start; border-radius:14px; margin-bottom:6px}
    .item-row.checked{background:rgba(254,226,226,0.6)}
    .info-btn{border-radius:8px; padding:6px}
    .pro-tip{display:flex; gap:12px; padding:18px; margin-top:18px; border-radius:24px}
    .muted{color:#94a3b8}
    table {width:100%; border-collapse:collapse; font-size:12px}
    th, td {padding:8px; border-bottom:1px solid #f1f5f9}
    thead tr{background:#fef2f2}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Data (conserve tous les textes d'origine) ---
sections = [
    {
      "title": "Phase 1 : J-14 à J-7",
      "subtitle": "L'Affûtage & La Fondation",
      "icon": "activity",
      "proTip": "Le but ici est la fraîcheur. On ne cherche plus à progresser physiquement, mais à arriver reposé et ultra-performant.",
      "categories": [
        {
          "name": "Entraînement & Physio",
          "items": [
            { 
              "id": "taper", 
              "label": "Phase de Taper", 
              "time": "J-14 ou J-7",
              "desc": "Réduction drastique du volume d'entraînement.",
              "details": "Réduction du volume global en maintenant l'intensité"
            },
          ]
        },
        {
          "name": "Nutrition & Hygiène",
          "items": [
            { 
              "id": "sleep_bank", 
              "label": "Sommeil 'Banking'", 
              "time": "J-14 à J-0",
              "desc": "Cherche à 'stocker' du sommeil.",
              "details": """
<p>Cherche à stocker du sommeil.</p>
<p class=\"mt-1\">Vise +45 à +90 min/nuit.</p>
<p class=\"mt-1\">La régularité {'>'} Quantité absolue.</p>
"""
            }
          ]
        }
      ]
    },
    {
      "title": "Phase 2 : J-6 à J-1",
      "subtitle": "La Semaine Critique",
      "icon": "zap",
      "proTip": "Tout le monde est prêt physiquement. Ceux qui gagnent sont ceux qui optimisent les détails que les autres négligent.",
      "categories": [
        {
          "name": "Nutrition & Hydratation",
          "items": [
             { 
              "id": "nitrates_load", 
              "label": "Charge de Jus de Betterave", 
              "time": "J-6 à J-1",
              "desc": "Saturer le corps en nitrates (1-2 shots/jour).",
              "details": """
<p>70-140 ml/jour pour augmenter l'oxyde nitrique.</p>
<p class=\"mt-1\">Améliore l'économie de l'effort et l'utilisation de l'ATP Pcr.</p>
<p class=\"mt-1 text-red-600 font-semibold\">Attention : Éviter bains de bouche antiseptiques.</p>
"""
            },
            { 
              "id": "sodium", 
              "label": "Hyperhydratation sodée", 
              "time": "J-3 à J-1",
              "desc": "Eau riche en sodium ou électrolytes.",
              "details": "Bois de l'eau riche en sodium ou ajoute des électrolytes à ton hydratation si tu ne le fais pas quotidiennement."
            },
             { 
              "id": "residues", 
              "label": "Régime sans résidus", 
              "time": "J-2",
              "desc": "Élimine les fibres (légumes crus, grains entiers).",
              "details": """
<div class=\"space-y-4\"> 
  <p>
    Élimine les fibres (légumes crus, grains entiers) pour vider le tractus intestinal. Cela évite les troubles digestifs et peut te faire gagner 500g à 1kg sur la balance (\"poids mort\" intestinal).
  </p>
  
  <div class=\"rounded-lg border border-slate-200 overflow-hidden\"> 
    <table class=\"w-full text-[10px] text-left border-collapse\"> 
      <thead>
        <tr class=\"bg-red-50 text-red-800 border-b border-red-100\"> 
          <th class=\"p-2 font-bold w-1/3\">Catégorie (Stop)</th>
          <th class=\"p-2 font-bold\">Exemples</th>
          <th class=\"p-2 font-bold\">Pourquoi stopper</th>
        </tr>
      </thead>
      <tbody class=\"bg-white\"> 
        <tr class=\"border-b border-slate-100\"> 
          <td class=\"p-2 font-bold text-slate-700\">Fibres insolubles</td>
          <td class=\"p-2 text-slate-600\">Légumes crus (brocoli, chou), graines, pain complet</td>
          <td class=\"p-2 text-slate-500\">↑ volume, ↑ fermentation → ballonnements</td>
        </tr>
        <tr class=\"border-b border-slate-100\"> 
          <td class=\"p-2 font-bold text-slate-700\">Légumineuses</td>
          <td class=\"p-2 text-slate-600\">Lentilles, pois chiches, haricots</td>
          <td class=\"p-2 text-slate-500\">↑ gaz + digestion lente</td>
        </tr>
        <tr class=\"border-b border-slate-100\"> 
          <td class=\"p-2 font-bold text-slate-700\">Céréales complètes</td>
          <td class=\"p-2 text-slate-600\">Riz complet, quinoa, avoine complet</td>
          <td class=\"p-2 text-slate-500\">↑ fibre insoluble → contenu intestinal élevé</td>
        </tr>
        <tr class=\"border-b border-slate-100\"> 
          <td class=\"p-2 font-bold text-slate-700\">Fruits riches en fibres</td>
          <td class=\"p-2 text-slate-600\">Framboises, poires, pommes avec peau</td>
          <td class=\"p-2 text-slate-500\">↑ fibre insoluble, fermentation</td>
        </tr>
        <tr class=\"border-b border-slate-100\"> 
          <td class=\"p-2 font-bold text-slate-700\">Noix / fruits secs</td>
          <td class=\"p-2 text-slate-600\">Amandes, noix, pruneaux</td>
          <td class=\"p-2 text-slate-500\">Gras ralentit vidange, difficile à digérer</td>
        </tr>
         <tr class=\"border-b border-slate-100\"> 
          <td class=\"p-2 font-bold text-slate-700\">Boissons gazeuses</td>
          <td class=\"p-2 text-slate-600\">Soda, eau gazeuse</td>
          <td class=\"p-2 text-slate-500\">Ballonnements, CO₂</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class=\"rounded-lg border border-slate-200 overflow-hidden\"> 
    <table class=\"w-full text-[10px] text-left border-collapse\"> 
      <thead>
        <tr class=\"bg-green-50 text-green-800 border-b border-green-100\"> 
          <th class=\"p-2 font-bold w-1/3\">Objectif (Go)</th>
          <th class=\"p-2 font-bold\">Aliments recommandés</th>
          <th class=\"p-2 font-bold\">Notes pratiques</th>
        </tr>
      </thead>
      <tbody class=\"bg-white\"> 
        <tr class=\"border-b border-slate-100\"> 
          <td class=\"p-2 font-bold text-slate-700\">Glucides digestibles</td>
          <td class=\"p-2 text-slate-600\">Riz blanc, pâtes blanches, pomme de terre, banane mûre</td>
          <td class=\"p-2 text-slate-500\">Maintient glycogène → énergie intacte</td>
        </tr>
        <tr class=\"border-b border-slate-100\"> 
          <td class=\"p-2 font-bold text-slate-700\">Protéines faciles</td>
          <td class=\"p-2 text-slate-600\">Blanc de poulet, dinde, œufs, whey</td>
          <td class=\"p-2 text-slate-500\">Pas de fibre → digestion rapide</td>
        </tr>
        <tr class=\"border-b border-slate-100\"> 
          <td class=\"p-2 font-bold text-slate-700\">Lipides</td>
          <td class=\"p-2 text-slate-600\">Très modérés (huile d'olive crue)</td>
          <td class=\"p-2 text-slate-500\">Légers pour le repas, pas de friture</td>
        </tr>
        <tr class=\"border-b border-slate-100\"> 
          <td class=\"p-2 font-bold text-slate-700\">Liquides & sodium</td>
          <td class=\"p-2 text-slate-600\">Eau plate, Vichy plate, bouillon</td>
          <td class=\"p-2 text-slate-500\">Maintien hydratation et sodium</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""
            },
            { 
              "id": "carb_load", 
              "label": "Augmentation Glucidique Contrôlée", 
              "time": "J-1",
              "desc": "Cible : 4-5g de glucides / kg de PDC.",
              "details": """
<p>Cible : 4-5g de glucides / kg de PDC, à répartir sur la journée.</p>
<p class=\"mt-1\">Dernier gros apport ≥6 h avant coucher.</p>
"""
            },
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
              "details": """
<p>Se sevrer une semaine avant pour resensibiliser les récepteurs.</p>
<p class=\"mt-1\">Ajustement recommandé si grand consommateur de café pour éviter les troubles : Réduire à ≤50 mg/j, pas arrêt total.</p>
"""
            },
            { 
              "id": "creatine", 
              "label": "Maintien Créatine et Beta-Alanine", 
              "time": "Quotidien",
              "desc": "Maintenir la dose de croisière (3-5g).",
              "details": """
<p>Si tu en prends déjà, maintenir la dose de croisière.</p>
<p class=\"mt-1 text-red-600 font-semibold\">Ne commence surtout pas maintenant si tu n'en consommes pas.</p>
"""
            },
            { 
              "id": "gear_check", 
              "label": "Check-up Matériel", 
              "time": "J-1",
              "desc": "Vérification complète : chaussures, straps, magnésie.",
              "details": """
<p>Chaussures, straps, nutrition glucidique, électrolytes.</p>
<p class=\"mt-1\">Rien de nouveau le jour de la compétition.</p>
"""
            }
          ]
        }
      ]
    },
    {
      "title": "Phase 3 : Le Jour J",
      "subtitle": "Avant l'épreuve",
      "icon": "flame",
      "proTip": "L'objectif de l'échauffement est l'excitation neuronale, pas la fatigue.",
      "categories": [
        {
          "name": "Chronologie Nutritionnelle",
          "items": [
            { 
              "id": "pre_meal", 
              "label": "Repas Pré-compétition", 
              "time": "H-4 à H-3",
              "desc": "Glucides ++, pauvre en lipides/fibres.",
              "details": """
<p>Riche en glucides, modéré en protéines (0,25-0,3g/kg max), très pauvre en lipides et fibres.</p>
<p class=\"mt-1\">Exemple : Riz blanc, compote, blanc de poulet ou protéine en poudre.</p>
<p class=\"mt-1\">Facile à digérer, énergie rapide.</p>
"""
            },
            { 
              "id": "nitrate_final", 
              "label": "Dernier shot de betterave", 
              "time": "H-2.5",
              "desc": "Dernier shot de betterave concentré.",
              "details": """
<p>Dernier shot de betterave.</p>
<p class=\"mt-1\">Le pic de nitrates plasmatiques survient 2 à 3h après ingestion.</p>
"""
            },
            { 
              "id": "cafeine_final", 
              "label": "Caféine Elite", 
              "time": "H-1",
              "desc": "Dosage : 3 mg / kg de poids de corps.",
              "details": """
<p>2 à 3 mg/kg fractionné en 2 prises par exemple sur des parcours différents (c'est beaucoup, teste-le avant !).</p>
<p class=\"mt-1\">Effet : Réduction de la perception de l'effort (RPE) et meilleure réactivité.</p>
"""
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
              "details": "Échauffement articulaire complet."
            },
            { 
              "id": "pap_cap", 
              "label": "PAP Capsulaire", 
              "time": "H-15 min",
              "desc": "Effort max sur contraction PAILs.",
              "details": """
<p>Effort max sur contraction PAILs (Flexion d'épaule et Rotation externe d'épaule + fonction spécifique).</p>
<p class=\"mt-1 font-semibold text-red-600\">Attention : Volume minimal pour ne pas cramer le système nerveux.</p>
"""
            },
            { 
              "id": "plio", 
              "label": "Pliométrie extensive", 
              "time": "H-10 min",
              "desc": "Volume bas sur sauts intensité moyenne.",
              "details": "Volume sans aller à la fatigue sur des sauts d'intensité basse/moyenne."
            },
            { 
              "id": "pap_muscular", 
              "label": "PAP Musculaire, Sprints et sauts", 
              "time": "H-5 min",
              "desc": "Intensité max, volume très bas.",
              "details": "Intensité max, volume bas."
            },
            { 
              "id": "thermal", 
              "label": "Veste thermique", 
              "time": "Départ",
              "desc": "Garder le corps au chaud jusqu'au bout.",
              "details": "Garder le corps au chaud jusqu'au bout."
            }
          ]
        }
      ]
    },
    {
      "title": "Phase 4 : En Course",
      "subtitle": "Gestion & Entre-runs",
      "icon": "brain",
      "proTip": "Quand l’épreuve s’étire, la différence entre les bons et les champions se joue dans la gestion entre les runs.",
      "categories": [
        {
          "name": "Protocole Entre 2 Runs",
          "items": [
            { 
              "id": "active_recov", 
              "label": "Récupération Active", 
              "time": "H + 2 min",
              "desc": "Marche active. Ne t'assois pas.",
              "details": """
<p>Marche active. Ne t'assois pas.</p>
<p class=\"mt-1\">Respire par le nez pour faire redescendre le rythme cardiaque.</p>
"""
            },
            { 
              "id": "hydro_electro", 
              "label": "Hydratation", 
              "time": "H + 5 min",
              "desc": "200-300ml d'eau avec électrolytes.",
              "details": """
<p>Bois 200-300ml d'eau avec des électrolytes.</p>
<p class=\"mt-1\">Si tu n'en as pas, une eau minérale type Vichy Célestins est parfaite.</p>
<p class=\"mt-1 text-red-600\">Attention pour la Vichy si estomac sensible.</p>
"""
            },
            { 
              "id": "refuel", 
              "label": "Apport Énergie", 
              "time": "H + 10 min",
              "desc": "Demi-banane ou miel si nécessaire.",
              "details": """
<p>Si tu te sens vide : Une demi-banane ou une petite gorgée de miel dilué avec de l'eau.</p>
<p class=\"mt-1\">Si tu te sens bien : Ne mange rien de solide.</p>
"""
            },
            { 
              "id": "mouth_rinse", 
              "label": "Relance", 
              "time": "H - 5 min",
              "desc": "Rinçage de bouche sucré (recracher).",
              "details": """
<p>Un dernier rinçage de bouche avec une boisson sucrée (dilué à l'eau), puis recrache si possible.</p>
<p class=\"mt-1\">Remets-toi en mouvement (petits sauts, rotations articulaires).</p>
"""
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
              "details": """
<p>Dialogue interne instructif.</p>
<p class=\"mt-1\">Focus sur les consignes techniques et l'instant présent plutôt que sur le résultat final.</p>
"""
            }
          ]
        }
      ]
    }
]

# --- Session state initialization ---
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 0
if 'checked_items' not in st.session_state:
    st.session_state.checked_items = {}
if 'expanded_sections' not in st.session_state:
    # default expand the first category of each phase (matching original keys like "0-0")
    st.session_state.expanded_sections = {f"{i}-0": True for i in range(len(sections))}
if 'open_details' not in st.session_state:
    st.session_state.open_details = {}

# --- Helper functions ---

def set_active_tab(idx):
    st.session_state.active_tab = idx


def toggle_item(item_id):
    checked = st.session_state.checked_items.get(item_id, False)
    st.session_state.checked_items[item_id] = not checked


def toggle_section(section_key):
    cur = st.session_state.expanded_sections.get(section_key, False)
    st.session_state.expanded_sections[section_key] = not cur


def toggle_details(item_id):
    cur = st.session_state.open_details.get(item_id, False)
    st.session_state.open_details[item_id] = not cur


def calculate_progress(phase_idx):
    phase = sections[phase_idx]
    total = 0
    checked = 0
    for cat in phase['categories']:
        for item in cat['items']:
            total += 1
            if st.session_state.checked_items.get(item['id']):
                checked += 1
    return (checked / total) * 100 if total > 0 else 0

# --- Page ---
st.markdown('<div class="app-container">', unsafe_allow_html=True)
st.markdown('<div class="max-width card" style="max-width:720px; margin:0 auto">', unsafe_allow_html=True)

# Header
st.markdown('<header style="text-align:center; margin-bottom:18px">', unsafe_allow_html=True)
st.markdown('<h1 style="font-size:32px; font-weight:900; color:#dc2626; font-style:italic; margin:0">COMPETITION READY.</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="font-size:12px; font-weight:800; color:#94a3b8; text-transform:uppercase; letter-spacing:0.3em; margin-top:6px">Checklist</h2>', unsafe_allow_html=True)
st.markdown('</header>', unsafe_allow_html=True)

# Tab Navigation
cols = st.columns(len(sections))
for i, section in enumerate(sections):
    with cols[i]:
        active = (st.session_state.active_tab == i)
        btn_label = f"Phase {i+1}"
        if st.button(btn_label, key=f"tab_{i}", help=section['title']):
            set_active_tab(i)
        # tiny visual indicator
        if active:
            st.markdown('<div style="text-align:center; margin-top:6px"><small style="color:#dc2626; font-weight:800">●</small></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div style="text-align:center; margin-top:6px"><small style="color:#cbd5e1">○</small></div>', unsafe_allow_html=True)

# Current Phase Overview
phase = sections[st.session_state.active_tab]
st.markdown('<div style="margin-top:16px; padding:0 8px">', unsafe_allow_html=True)
st.markdown(f'<div style="display:flex; justify-content:space-between; align-items:end; margin-bottom:8px"><div><h3 class="phase-title">{escape(phase["title"])}</h3><div class="phase-sub">{escape(phase["subtitle"])}</div></div><div style="font-weight:900; color:#94a3b8">{round(calculate_progress(st.session_state.active_tab))}%</div></div>', unsafe_allow_html=True)
progress = calculate_progress(st.session_state.active_tab)
st.markdown(f'<div class="progress-wrap"><div class="progress-bar" style="width:{progress}%"></div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Categories & Items
for cat_idx, cat in enumerate(phase['categories']):
    section_key = f"{st.session_state.active_tab}-{cat_idx}"
    is_expanded = st.session_state.expanded_sections.get(section_key, False)

    # Category container
    st.markdown(f'<div class="card category">', unsafe_allow_html=True)
    # Header with toggle
    col1, col2 = st.columns([9,1])
    with col1:
        if st.button(cat['name'], key=f"catbtn_{section_key}"):
            toggle_section(section_key)
    with col2:
        if is_expanded:
            st.markdown('<div style="text-align:right; color:#ef4444">∧</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div style="text-align:right; color:#94a3b8">∨</div>', unsafe_allow_html=True)

    if is_expanded:
        for item in cat['items']:
            checked = st.session_state.checked_items.get(item['id'], False)
            row_class = 'item-row checked' if checked else 'item-row'
            # Row clickable: we present a checkbox and a button for details
            cols_row = st.columns([0.06, 0.8, 0.14])
            with cols_row[0]:
                val = st.checkbox('', value=checked, key=f"chk_{item['id']}", on_change=toggle_item, args=(item['id'],))
            with cols_row[1]:
                st.markdown(f"<div class=\"{row_class}\"><div style=\"font-size:10px; font-weight:900; color:#ef4444\">{escape(item['time'])}</div><div style=\"font-weight:800; font-size:15px;\">{escape(item['label'])}</div><div class=\"muted\" style=\"margin-top:6px\">{escape(item.get('desc',''))}</div></div>", unsafe_allow_html=True)
            with cols_row[2]:
                if st.button('i', key=f"info_{item['id']}"):
                    toggle_details(item['id'])
                # Details drawer
            if st.session_state.open_details.get(item['id'], False):
                st.markdown('<div style="padding:12px; border-top:1px solid #f1f5f9; background:rgba(255,255,255,0.9); border-radius:8px">', unsafe_allow_html=True)
                # details might contain raw html
                details = item.get('details','')
                st.markdown(details, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Dynamic Pro Tip Footer
st.markdown('<div class="pro-tip card" style="align-items:center">', unsafe_allow_html=True)
st.markdown('<div style="background:#dc2626; padding:10px; border-radius:12px; color:white; font-weight:900">🛡️</div>', unsafe_allow_html=True)
st.markdown(f'<div><div style="font-weight:900; font-size:10px; color:#dc2626; text-transform:uppercase; letter-spacing:0.15em">Conseil Pro Phase {st.session_state.active_tab + 1}</div><div style="font-weight:800; font-size:13px; color:#0f172a; font-style:italic; margin-top:6px">"{escape(phase["proTip"])}"</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<p style="text-align:center; color:#94a3b8; font-weight:800; text-transform:uppercase; font-size:11px; margin-top:18px">Next Athlete Performance System v1.0</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- End ---
