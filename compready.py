import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Competition Ready Checklist",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Masquer les éléments d'interface par défaut de Streamlit pour un look application
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0;}
    </style>
""", unsafe_allow_html=True)

# Le code HTML complet incluant React, Tailwind CSS et Lucide Icons
html_code = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
        body { font-family: 'Inter', sans-serif; background-color: #f8fafc; }
        .animate-in { animation: fadeIn 0.5s ease-out forwards; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
    <div id="root"></div>

    <script type="text/babel">
        const { useState, useEffect } = React;
        
        // Configuration des icônes Lucide
        const Icon = ({ name, className, size = 20 }) => {
            useEffect(() => {
                lucide.createIcons();
            }, [name, className]);
            return <i data-lucide={name} className={className} style={{width: size, height: size}}></i>;
        };

        const App = () => {
            const [activeTab, setActiveTab] = useState(0);
            const [checkedItems, setCheckedItems] = useState({});
            const [expandedSections, setExpandedSections] = useState({ "0-0": true, "1-0": true, "2-0": true, "3-0": true });
            const [openDetails, setOpenDetails] = useState({});

            const sections = [
                {
                    title: "Phase 1 : J-14 à J-7",
                    subtitle: "L'Affûtage & La Fondation",
                    icon: "activity",
                    proTip: "Le but ici est la fraîcheur. Ne cherche plus à progresser physiquement, mais à arriver reposé et ultra-précis.",
                    categories: [
                        {
                            name: "Entraînement & Physio",
                            items: [
                                { id: "taper", label: "Phase de Taper", time: "J-14", details: "Réduction du volume global. On maintient l'intensité mais on diminue la durée des séances." },
                                { id: "massage", label: "Soins des tissus mous", time: "J-10 Max", details: "Dernier massage profond (Deep Tissue) à J-10 max pour éviter les courbatures le jour J." }
                            ]
                        },
                        {
                            name: "Nutrition & Hygiène",
                            items: [
                                { id: "sleep_bank", label: "Sommeil 'Banking'", time: "J-14 à J-0", details: "Augmenter le sommeil (9h-10h) 2 semaines avant améliore les temps de réaction." }
                            ]
                        }
                    ]
                },
                {
                    title: "Phase 2 : J-6 à J-1",
                    subtitle: "La Semaine Critique",
                    icon: "zap",
                    proTip: "Le sevrage de caféine est difficile les 3 premiers jours, mais le boost le jour J sera ton plus grand avantage nerveux.",
                    categories: [
                        {
                            name: "Nutrition & Hydratation",
                            items: [
                                { id: "carb_load", label: "Augmentation Glucidique", time: "J-1", details: "Cible : 4-5g de glucides/kg. Maximiser les stocks de glycogène." },
                                { id: "residues", label: "Régime sans résidus", time: "J-2", details: "Éliminer les fibres pour vider le tractus et gagner du 'poids mort' (500g-1kg)." },
                                { id: "sodium", label: "Hyperhydratation sodée", time: "J-3 à J-1", details: "Sodium pour retenir le fluide plasmatique, crucial pour la thermorégulation." },
                                { id: "nitrates_load", label: "Charge Jus de Betterave", time: "J-6 à J-1", details: "Saturer le corps en nitrates pour l'économie d'effort." }
                            ]
                        },
                        {
                            name: "Suppléments & Logistique",
                            items: [
                                { id: "cafeine_reset", label: "Arrêt de la Caféine", time: "J-7 à J-2", details: "Caffeine reset pour resensibiliser les récepteurs à l'adénosine." },
                                { id: "creatine", label: "Maintien Créatine", time: "Quotidien", details: "Maintenir 3-5g. Ne pas commencer maintenant pour éviter la rétention d'eau." },
                                { id: "gear_check", label: "Check-up Matériel", time: "J-2", details: "Vérification chaussures, straps, nutrition. Rien de nouveau le jour J." }
                            ]
                        }
                    ]
                },
                {
                    title: "Phase 3 : Le Jour J",
                    subtitle: "Avant l'épreuve",
                    icon: "flame",
                    proTip: "Respecte scrupuleusement le timing du dernier shot de betterave. L'effet de pic est une fenêtre physiologique précise.",
                    categories: [
                        {
                            name: "Chronologie Nutritionnelle",
                            items: [
                                { id: "pre_meal", label: "Repas Pré-compétition", time: "H-4 à H-3", details: "Riz blanc, poulet, compote. Pauvre en fibres et lipides." },
                                { id: "nitrate_final", label: "Nitrate Shot Final", time: "H-2.5", details: "Le pic survient 2 à 3h après l'ingestion." },
                                { id: "cafeine_final", label: "Caféine Elite", time: "H-1", details: "3 mg/kg. Réduction de la perception de l'effort (RPE)." },
                                { id: "tampon", label: "Tampon Acide", time: "H-1", details: "Bicarbonate/Beta-Alanine. Attention aux troubles gastriques." }
                            ]
                        },
                        {
                            name: "Échauffement",
                            items: [
                                { id: "racs", label: "RACs Full-Body", time: "H-30 min", details: "Mobilisation articulaire complète sans fatigue." },
                                { id: "pap_cap", label: "PAP Capsulaire", time: "H-15 min", details: "Contraction PAILs épaule pour préparer le grip." },
                                { id: "pap_muscular", label: "PAP Musculaire", time: "H-5 min", details: "Sprints et sauts. Intensité max, volume bas." },
                                { id: "thermal", label: "Veste thermique", time: "Départ", details: "Garder le corps chaud jusqu'à la dernière seconde." }
                            ]
                        }
                    ]
                },
                {
                    title: "Phase 4 : En Course",
                    subtitle: "Gestion & Entre-runs",
                    icon: "brain",
                    proTip: "Le 'Mouth Rinsing' trompe ton cerveau en lui faisant croire que de l'énergie arrive, sans peser sur ton estomac.",
                    categories: [
                        {
                            name: "Protocole Entre 2 Runs",
                            items: [
                                { id: "active_recov", label: "Récupération Active", time: "H + 2 min", details: "Marche active, respiration nasale pour redescendre le cardio." },
                                { id: "hydro_electro", label: "Hydratation Sodée", time: "H + 5 min", details: "200-300ml eau + électrolytes (Vichy Célestins idéal)." },
                                { id: "mouth_rinse", label: "Relance & Rinçage", time: "H - 5 min", details: "Rinçage bouche sucré (recracher) + petits sauts de relance." }
                            ]
                        }
                    ]
                }
            ];

            const toggleItem = (id) => setCheckedItems(p => ({ ...p, [id]: !p[id] }));
            const toggleDetails = (e, id) => { e.stopPropagation(); setOpenDetails(p => ({ ...p, [id]: !p[id] })); };
            const toggleSection = (key) => setExpandedSections(p => ({ ...p, [key]: !p[key] }));

            const calculateProgress = (idx) => {
                let total = 0, checked = 0;
                sections[idx].categories.forEach(c => c.items.forEach(i => { total++; if (checkedItems[i.id]) checked++; }));
                return total === 0 ? 0 : (checked / total) * 100;
            };

            return (
                <div className="min-h-screen p-4 pb-20 max-w-md mx-auto">
                    <header className="mb-6 text-center">
                        <h1 className="text-3xl font-black text-red-600 italic tracking-tighter">READY.</h1>
                        <h2 className="text-[10px] font-bold text-slate-400 uppercase tracking-[0.3em]">Checklist Elite</h2>
                    </header>

                    <div className="flex justify-between mb-8 bg-white/60 backdrop-blur-xl p-1.5 rounded-2xl border border-white shadow-sm">
                        {sections.map((s, i) => (
                            <button key={i} onClick={() => setActiveTab(i)} className={`flex-1 py-3 rounded-xl flex flex-col items-center transition-all ${activeTab === i ? 'bg-white shadow-md text-red-600 scale-[1.05]' : 'text-slate-300'}`}>
                                <Icon name={s.icon} size={20} className={activeTab === i ? 'text-red-600' : ''} />
                                <span className="text-[8px] mt-1 font-black uppercase tracking-widest">Phase {i+1}</span>
                            </button>
                        ))}
                    </div>

                    <div className="mb-6 px-2">
                        <div className="flex justify-between items-end mb-2">
                            <div>
                                <h3 className="text-2xl font-black text-slate-800 tracking-tight leading-none">{sections[activeTab].title}</h3>
                                <p className="text-red-500 font-bold text-xs uppercase mt-1 tracking-wider">{sections[activeTab].subtitle}</p>
                            </div>
                            <span className="text-xs font-black text-slate-300">{Math.round(calculateProgress(activeTab))}%</span>
                        </div>
                        <div className="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden">
                            <div className="h-full bg-red-600 transition-all duration-700" style={{ width: `${calculateProgress(activeTab)}%` }} />
                        </div>
                    </div>

                    <div className="space-y-4">
                        {sections[activeTab].categories.map((cat, catIdx) => {
                            const key = `${activeTab}-${catIdx}`;
                            return (
                                <div key={catIdx} className="bg-white/80 backdrop-blur-md border border-white rounded-[1.5rem] shadow-sm overflow-hidden">
                                    <button onClick={() => toggleSection(key)} className="w-full p-4 flex justify-between items-center">
                                        <span className="font-black text-[10px] uppercase tracking-[0.15em] text-slate-400">{cat.name}</span>
                                        <Icon name={expandedSections[key] ? "chevron-up" : "chevron-down"} size={14} className="text-slate-300" />
                                    </button>
                                    {expandedSections[key] && (
                                        <div className="p-3 pt-0 space-y-2">
                                            {cat.items.map(item => (
                                                <div key={item.id} className="rounded-2xl border border-slate-50 overflow-hidden">
                                                    <div onClick={() => toggleItem(item.id)} className={`flex items-start gap-3 p-3 cursor-pointer transition-all ${checkedItems[item.id] ? 'bg-red-50/50' : 'bg-white'}`}>
                                                        <div className="mt-1">
                                                            <Icon name={checkedItems[item.id] ? "check-circle-2" : "circle"} size={20} className={checkedItems[item.id] ? "text-red-600" : "text-slate-200"} />
                                                        </div>
                                                        <div className="flex-1">
                                                            <div className="flex justify-between items-start">
                                                                <div className="flex flex-col">
                                                                    <span className="text-[9px] font-black text-red-500 uppercase mb-0.5">{item.time}</span>
                                                                    <p className={`font-bold text-sm leading-tight ${checkedItems[item.id] ? 'text-red-700' : 'text-slate-800'}`}>{item.label}</p>
                                                                </div>
                                                                <button onClick={(e) => toggleDetails(e, item.id)} className={`p-1.5 rounded-lg ${openDetails[item.id] ? 'bg-red-600 text-white' : 'bg-slate-50 text-slate-300'}`}>
                                                                    <Icon name="info" size={14} />
                                                                </button>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    {openDetails[item.id] && (
                                                        <div className="p-4 bg-white/80 border-t border-slate-50 text-[11px] text-slate-600 font-medium leading-relaxed">
                                                            {item.details}
                                                        </div>
                                                    )}
                                                </div>
                                            ))}
                                        </div>
                                    )}
                                </div>
                            );
                        })}
                    </div>

                    <div className="mt-8 p-5 bg-white rounded-3xl border border-slate-100 shadow-xl flex gap-4 animate-in">
                        <div className="bg-red-600 p-2.5 rounded-2xl text-white self-start"><Icon name="shield-check" size={20} /></div>
                        <div>
                            <h4 className="font-black text-[10px] uppercase text-red-600">Conseil Pro Phase {activeTab + 1}</h4>
                            <p className="text-[11px] leading-relaxed mt-1 font-bold text-slate-700 italic">"{sections[activeTab].proTip}"</p>
                        </div>
                    </div>
                </div>
            );
        };

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
</body>
</html>
"""

# Affichage du composant dans Streamlit
# On utilise une hauteur fixe suffisante pour le scroll interne
components.html(html_code, height=900, scrolling=True)
