import reflex as rx
from typing import Dict, List, Any

# --- Données statiques (identiques à l'original) ---
SECTIONS = [
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
                        "details_text": "Réduction du volume global en maintenant l'intensité",
                        "type": "text"
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
                        "details_content": [
                            "Cherche à stocker du sommeil.",
                            "Vise +45 à +90 min/nuit.",
                            "La régularité > Quantité absolue."
                        ],
                        "type": "list"
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
                        "details_content": [
                            "70-140 ml/jour pour augmenter l'oxyde nitrique.",
                            "Améliore l'économie de l'effort et l'utilisation de l'ATP Pcr.",
                            ("Attention : Éviter bains de bouche antiseptiques.", "text-red-600 font-semibold")
                        ],
                        "type": "list"
                    },
                    {
                        "id": "sodium",
                        "label": "Hyperhydratation sodée",
                        "time": "J-3 à J-1",
                        "desc": "Eau riche en sodium ou électrolytes.",
                        "details_text": "Bois de l'eau riche en sodium ou ajoute des électrolytes à ton hydratation si tu ne le fais pas quotidiennement.",
                        "type": "text"
                    },
                    {
                        "id": "residues",
                        "label": "Régime sans résidus",
                        "time": "J-2",
                        "desc": "Élimine les fibres (légumes crus, grains entiers).",
                        "type": "residues_table" # Type spécial pour le tableau complexe
                    },
                    {
                        "id": "carb_load",
                        "label": "Augmentation Glucidique Contrôlée",
                        "time": "J-1",
                        "desc": "Cible : 4-5g de glucides / kg de PDC.",
                        "details_content": [
                            "Cible : 4-5g de glucides / kg de PDC, à répartir sur la journée.",
                            "Dernier gros apport ≥6 h avant coucher."
                        ],
                        "type": "list"
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
                        "details_content": [
                            "Se sevrer une semaine avant pour resensibiliser les récepteurs.",
                            "Ajustement recommandé si grand consommateur de café pour éviter les troubles : Réduire à ≤50 mg/j, pas arrêt total."
                        ],
                        "type": "list"
                    },
                    {
                        "id": "creatine",
                        "label": "Maintien Créatine et Beta-Alanine",
                        "time": "Quotidien",
                        "desc": "Maintenir la dose de croisière (3-5g).",
                        "details_content": [
                            "Si tu en prends déjà, maintenir la dose de croisière.",
                            ("Ne commence surtout pas maintenant si tu n'en consommes pas.", "text-red-600 font-semibold")
                        ],
                        "type": "list"
                    },
                    {
                        "id": "gear_check",
                        "label": "Check-up Matériel",
                        "time": "J-1",
                        "desc": "Vérification complète : chaussures, straps, magnésie.",
                        "details_content": [
                            "Chaussures, straps, nutrition glucidique, électrolytes.",
                            "Rien de nouveau le jour de la compétition."
                        ],
                        "type": "list"
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
                        "details_content": [
                            "Riche en glucides, modéré en protéines (0,25-0,3g/kg max), très pauvre en lipides et fibres.",
                            "Exemple : Riz blanc, compote, blanc de poulet ou protéine en poudre.",
                            "Facile à digérer, énergie rapide."
                        ],
                        "type": "list"
                    },
                    {
                        "id": "nitrate_final",
                        "label": "Dernier shot de betterave",
                        "time": "H-2.5",
                        "desc": "Dernier shot de betterave concentré.",
                        "details_content": [
                            "Dernier shot de betterave.",
                            "Le pic de nitrates plasmatiques survient 2 à 3h après ingestion."
                        ],
                        "type": "list"
                    },
                    {
                        "id": "cafeine_final",
                        "label": "Caféine Elite",
                        "time": "H-1",
                        "desc": "Dosage : 3 mg / kg de poids de corps.",
                        "details_content": [
                            "2 à 3 mg/kg fractionné en 2 prises par exemple sur des parcours différents (c'est beaucoup, teste-le avant !).",
                            "Effet : Réduction de la perception de l'effort (RPE) et meilleure réactivité."
                        ],
                        "type": "list"
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
                        "details_text": "Échauffement articulaire complet.",
                        "type": "text"
                    },
                    {
                        "id": "pap_cap",
                        "label": "PAP Capsulaire",
                        "time": "H-15 min",
                        "desc": "Effort max sur contraction PAILs.",
                        "details_content": [
                            "Effort max sur contraction PAILs (Flexion d'épaule et Rotation externe d'épaule + fonction spécifique).",
                            ("Attention : Volume minimal pour ne pas cramer le système nerveux.", "font-semibold text-red-600")
                        ],
                        "type": "list"
                    },
                    {
                        "id": "plio",
                        "label": "Pliométrie extensive",
                        "time": "H-10 min",
                        "desc": "Volume bas sur sauts intensité moyenne.",
                        "details_text": "Volume sans aller à la fatigue sur des sauts d'intensité basse/moyenne.",
                        "type": "text"
                    },
                    {
                        "id": "pap_muscular",
                        "label": "PAP Musculaire, Sprints et sauts",
                        "time": "H-5 min",
                        "desc": "Intensité max, volume très bas.",
                        "details_text": "Intensité max, volume bas.",
                        "type": "text"
                    },
                    {
                        "id": "thermal",
                        "label": "Veste thermique",
                        "time": "Départ",
                        "desc": "Garder le corps au chaud jusqu'au bout.",
                        "details_text": "Garder le corps au chaud jusqu'au bout.",
                        "type": "text"
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
                        "details_content": [
                            "Marche active. Ne t'assois pas.",
                            "Respire par le nez pour faire redescendre le rythme cardiaque."
                        ],
                        "type": "list"
                    },
                    {
                        "id": "hydro_electro",
                        "label": "Hydratation",
                        "time": "H + 5 min",
                        "desc": "200-300ml d'eau avec électrolytes.",
                        "details_content": [
                            "Bois 200-300ml d'eau avec des électrolytes.",
                            "Si tu n'en as pas, une eau minérale type Vichy Célestins est parfaite.",
                            ("Attention pour la Vichy si estomac sensible.", "text-red-600")
                        ],
                        "type": "list"
                    },
                    {
                        "id": "refuel",
                        "label": "Apport Énergie",
                        "time": "H + 10 min",
                        "desc": "Demi-banane ou miel si nécessaire.",
                        "details_content": [
                            "Si tu te sens vide : Une demi-banane ou une petite gorgée de miel dilué avec de l'eau.",
                            "Si tu te sens bien : Ne mange rien de solide."
                        ],
                        "type": "list"
                    },
                    {
                        "id": "mouth_rinse",
                        "label": "Relance",
                        "time": "H - 5 min",
                        "desc": "Rinçage de bouche sucré (recracher).",
                        "details_content": [
                            "Un dernier rinçage de bouche avec une boisson sucrée (dilué à l'eau), puis recrache si possible.",
                            "Remets-toi en mouvement (petits sauts, rotations articulaires)."
                        ],
                        "type": "list"
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
                        "details_content": [
                            "Dialogue interne instructif.",
                            "Focus sur les consignes techniques et l'instant présent plutôt que sur le résultat final."
                        ],
                        "type": "list"
                    }
                ]
            }
        ]
    }
]

# --- État de l'Application (Logic) ---
class AppState(rx.State):
    active_tab: int = 0
    checked_items: Dict[str, bool] = {}
    expanded_sections: Dict[str, bool] = {"0-0": True, "1-0": True, "2-0": True, "3-0": True}
    open_details: Dict[str, bool] = {}

    def set_tab(self, i: int):
        self.active_tab = i

    def toggle_item(self, id: str):
        self.checked_items[id] = ~self.checked_items.get(id, False)

    def toggle_details(self, id: str):
        self.open_details[id] = ~self.open_details.get(id, False)

    def toggle_section(self, key: str):
        self.expanded_sections[key] = ~self.expanded_sections.get(key, False)

    @rx.var
    def current_phase_data(self) -> Dict:
        return SECTIONS[self.active_tab]

    @rx.var
    def progress(self) -> int:
        phase = SECTIONS[self.active_tab]
        total = 0
        checked = 0
        # Calculer le progrès en Python
        for cat in phase["categories"]:
            for item in cat["items"]:
                total += 1
                if self.checked_items.get(item["id"], False):
                    checked += 1
        return int((checked / total) * 100) if total > 0 else 0

# --- Composants UI ---

def render_table_row(label, ex, why, border=True):
    return rx.el.tr(
        rx.el.td(label, class_name="p-2 font-bold text-slate-700"),
        rx.el.td(ex, class_name="p-2 text-slate-600"),
        rx.el.td(why, class_name="p-2 text-slate-500"),
        class_name=f"border-b border-slate-100" if border else ""
    )

def render_residues_table():
    """Rendu spécifique pour le tableau du régime sans résidus"""
    return rx.vstack(
        rx.text("Élimine les fibres (légumes crus, grains entiers) pour vider le tractus intestinal. Cela évite les troubles digestifs et peut te faire gagner 500g à 1kg sur la balance (\"poids mort\" intestinal).", class_name="mb-4"),
        
        # Tableau 1: À Éviter
        rx.box(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th("Catégorie (Stop)", class_name="p-2 font-bold w-1/3"),
                        rx.el.th("Exemples", class_name="p-2 font-bold"),
                        rx.el.th("Pourquoi stopper", class_name="p-2 font-bold"),
                        class_name="bg-red-50 text-red-800 border-b border-red-100"
                    )
                ),
                rx.el.tbody(
                    render_table_row("Fibres insolubles", "Légumes crus (brocoli, chou), graines, pain complet", "↑ volume, ↑ fermentation → ballonnements"),
                    render_table_row("Légumineuses", "Lentilles, pois chiches, haricots", "↑ gaz + digestion lente"),
                    render_table_row("Céréales complètes", "Riz complet, quinoa, avoine complet", "↑ fibre insoluble → contenu intestinal élevé"),
                    render_table_row("Fruits riches en fibres", "Framboises, poires, pommes avec peau", "↑ fibre insoluble, fermentation"),
                    render_table_row("Noix / fruits secs", "Amandes, noix, pruneaux", "Gras ralentit vidange, difficile à digérer"),
                    render_table_row("Boissons gazeuses", "Soda, eau gazeuse", "Ballonnements, CO₂", border=False),
                    class_name="bg-white"
                ),
                class_name="w-full text-[10px] text-left border-collapse"
            ),
            class_name="rounded-lg border border-slate-200 overflow-hidden w-full"
        ),

        # Tableau 2: Recommandé
        rx.box(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th("Objectif (Go)", class_name="p-2 font-bold w-1/3"),
                        rx.el.th("Aliments recommandés", class_name="p-2 font-bold"),
                        rx.el.th("Notes pratiques", class_name="p-2 font-bold"),
                        class_name="bg-green-50 text-green-800 border-b border-green-100"
                    )
                ),
                rx.el.tbody(
                    render_table_row("Glucides digestibles", "Riz blanc, pâtes blanches, pomme de terre, banane mûre", "Maintient glycogène → énergie intacte"),
                    render_table_row("Protéines faciles", "Blanc de poulet, dinde, œufs, whey", "Pas de fibre → digestion rapide"),
                    render_table_row("Lipides", "Très modérés (huile d'olive crue)", "Légers pour le repas, pas de friture"),
                    render_table_row("Liquides & sodium", "Eau plate, Vichy plate, bouillon", "Maintien hydratation et sodium", border=False),
                    class_name="bg-white"
                ),
                class_name="w-full text-[10px] text-left border-collapse"
            ),
            class_name="rounded-lg border border-slate-200 overflow-hidden w-full mt-2"
        ),
        class_name="space-y-4 text-[11px] text-slate-600 leading-relaxed font-medium"
    )

def render_details_content(item: Dict):
    """Logique pour afficher le bon contenu dans l'accordéon"""
    return rx.cond(
        item["type"] == "residues_table",
        render_residues_table(),
        rx.cond(
            item["type"] == "text",
            rx.text(item["details_text"], class_name="text-[11px] text-slate-600 leading-relaxed font-medium"),
            # Cas liste
            rx.vstack(
                rx.foreach(
                    item["details_content"],
                    lambda line: rx.cond(
                        # Si la ligne est un tuple (texte, classe), on l'applique
                        isinstance(line, list), 
                        rx.text(line[0], class_name=f"mt-1 {line[1]}"),
                        rx.text(line, class_name="mt-1")
                    )
                ),
                class_name="text-[11px] text-slate-600 leading-relaxed font-medium items-start"
            )
        )
    )

def render_item(item: Dict):
    return rx.box(
        rx.box(
            rx.hstack(
                rx.box(
                    rx.cond(
                        AppState.checked_items[item["id"]],
                        rx.icon(tag="check-circle-2", class_name="text-red-600 w-5 h-5"),
                        rx.icon(tag="circle", class_name="text-slate-200 w-5 h-5 group-hover:text-red-200")
                    ),
                    class_name="mt-1 flex-shrink-0"
                ),
                rx.box(
                    rx.hstack(
                        rx.vstack(
                            rx.text(item["time"], class_name="text-[9px] font-black text-red-500 uppercase tracking-tighter mb-0.5"),
                            rx.text(
                                item["label"], 
                                class_name=rx.cond(
                                    AppState.checked_items[item["id"]],
                                    "font-bold text-sm leading-tight transition-colors text-red-700",
                                    "font-bold text-sm leading-tight transition-colors text-slate-800"
                                )
                            ),
                            align_items="start",
                            spacing="0"
                        ),
                        rx.button(
                            rx.icon(tag="info", size=14),
                            on_click=lambda: AppState.toggle_details(item["id"]),
                            class_name=rx.cond(
                                AppState.open_details[item["id"]],
                                "p-1.5 rounded-lg transition-all bg-red-600 text-white",
                                "p-1.5 rounded-lg transition-all bg-slate-50 text-slate-300"
                            ),
                            padding="0"
                        ),
                        justify="between",
                        align="start",
                        width="100%"
                    ),
                    class_name="flex-1"
                ),
                class_name=rx.cond(
                    AppState.checked_items[item["id"]],
                    "flex items-start gap-3 p-3 cursor-pointer transition-all bg-red-50/50",
                    "flex items-start gap-3 p-3 cursor-pointer transition-all bg-white hover:bg-slate-50"
                ),
                on_click=lambda: AppState.toggle_item(item["id"])
            ),
            # Detailed Description Drawer
            rx.box(
                rx.box(
                   render_details_content(item),
                   class_name="p-4 border-t border-slate-50"
                ),
                class_name=rx.cond(
                    AppState.open_details[item["id"]],
                    "transition-all duration-300 ease-in-out overflow-hidden bg-white/80 max-h-[800px]",
                    "transition-all duration-300 ease-in-out overflow-hidden bg-white/80 max-h-0 opacity-0"
                )
            )
        ),
        class_name="rounded-2xl border border-slate-50 overflow-hidden transition-all"
    )

def render_category(cat: Dict, index: int):
    section_key = f"{AppState.active_tab}-{index}" # Ne fonctionne pas directement dans l'indexation, on utilise une logique simplifiée
    # Pour simplifier en Reflex, on va reconstruire la clé dynamiquement dans le composant si besoin, 
    # mais ici on utilise une clé statique basée sur l'itération extérieure qui est complexe.
    # On va assumer que la clé est passée ou gérée par l'index de la boucle foreach.
    
    return rx.box(
        rx.button(
            rx.text(cat["name"], class_name="font-black text-[10px] uppercase tracking-[0.15em] text-slate-400"),
            rx.cond(
                AppState.expanded_sections[section_key],
                rx.icon(tag="chevron-up", size=14, class_name="text-red-400"),
                rx.icon(tag="chevron-down", size=14, class_name="text-slate-300")
            ),
            on_click=lambda: AppState.toggle_section(section_key),
            class_name="w-full p-4 flex justify-between items-center hover:bg-white/40 transition-colors"
        ),
        rx.box(
            rx.box(
                rx.foreach(
                    cat["items"],
                    render_item
                ),
                class_name="p-3 pt-0 space-y-2"
            ),
            class_name=rx.cond(
                AppState.expanded_sections[section_key],
                "transition-all duration-300 ease-in-out max-h-[1500px] overflow-hidden",
                "transition-all duration-300 ease-in-out max-h-0 overflow-hidden"
            )
        ),
        class_name="bg-white/80 backdrop-blur-md border border-white rounded-[1.5rem] shadow-sm overflow-hidden"
    )

def index():
    return rx.box(
        rx.box(
            # Header
            rx.box(
                rx.heading("COMPETITION READY.", class_name="text-3xl font-black tracking-tighter text-red-600 italic"),
                rx.heading("Checklist", class_name="text-sm font-bold text-slate-400 uppercase tracking-[0.3em]"),
                class_name="mb-6 text-center"
            ),
            
            # Tab Navigation
            rx.hstack(
                rx.foreach(
                    SECTIONS,
                    lambda section, i: rx.button(
                        rx.box(
                            rx.icon(tag=section["icon"]),
                            class_name=rx.cond(AppState.active_tab == i, "scale-110 transition-transform", "scale-100 transition-transform")
                        ),
                        rx.text(f"Phase {i+1}", class_name="text-[8px] mt-1 font-black uppercase tracking-widest"),
                        on_click=lambda: AppState.set_tab(i),
                        class_name=rx.cond(
                            AppState.active_tab == i,
                            "flex-1 py-3 rounded-xl flex flex-col items-center transition-all duration-300 bg-white shadow-md text-red-600 scale-[1.05]",
                            "flex-1 py-3 rounded-xl flex flex-col items-center transition-all duration-300 text-slate-300 hover:text-slate-500"
                        )
                    )
                ),
                class_name="flex justify-between mb-8 bg-white/60 backdrop-blur-xl p-1.5 rounded-2xl border border-white shadow-sm"
            ),

            # Current Phase Overview
            rx.box(
                rx.hstack(
                    rx.box(
                        rx.heading(AppState.current_phase_data["title"], class_name="text-2xl font-black text-slate-800 tracking-tight leading-none"),
                        rx.text(AppState.current_phase_data["subtitle"], class_name="text-red-500 font-bold text-xs uppercase mt-1 tracking-wider"),
                    ),
                    rx.text(f"{AppState.progress}%", class_name="text-xs font-black text-slate-300 tracking-tighter"),
                    justify="between",
                    align="end",
                    class_name="mb-2"
                ),
                rx.box(
                    rx.box(
                        class_name="h-full bg-red-600 transition-all duration-700 ease-out",
                        style={"width": f"{AppState.progress}%"}
                    ),
                    class_name="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden"
                ),
                class_name="mb-6 px-2"
            ),

            # Categories & Items
            rx.vstack(
                rx.foreach(
                    AppState.current_phase_data["categories"],
                    lambda cat, i: render_category(cat, i)
                ),
                class_name="space-y-4"
            ),

            # Dynamic Pro Tip Footer
            rx.box(
                rx.box(
                    rx.icon(tag="shield-check", size=20),
                    class_name="bg-red-600 p-2.5 rounded-2xl text-white shadow-lg shadow-red-100 self-start"
                ),
                rx.box(
                    rx.text(f"Conseil Pro Phase {AppState.active_tab + 1}", class_name="font-black text-[10px] uppercase tracking-widest text-red-600"),
                    rx.text(f"\"{AppState.current_phase_data['proTip']}\"", class_name="text-[11px] leading-relaxed mt-1 font-bold text-slate-700 italic")
                ),
                class_name="mt-8 p-5 bg-white rounded-3xl border border-slate-100 shadow-xl relative overflow-hidden flex gap-4 animate-in fade-in duration-700"
            ),
            
            rx.text("Next Athlete Performance System v1.0", class_name="text-center text-slate-300 text-[9px] font-black uppercase tracking-[0.3em] mt-8"),
            
            class_name="max-w-md mx-auto"
        ),
        class_name="min-h-screen bg-slate-50 p-4 md:p-8 font-sans text-slate-900 pb-24"
    )

app = rx.App()
app.add_page(index)
