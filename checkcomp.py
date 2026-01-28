import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Competition Ready", layout="centered", initial_sidebar_state="collapsed")

html_code = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #f8fafc; }
        .no-scrollbar::-webkit-scrollbar { display: none; }
    </style>
</head>
<body>
    <div id="root"></div>

    <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>

    <script>
        const { useState, useEffect } = React;

        // Structure des données (exactement comme ton React original)
const sections = [
    {
      title: "Phase 1 : J-14 à J-7",
      subtitle: "L'Affûtage & La Fondation",
      icon: <Activity className="w-5 h-5" />,
      proTip: "Le but ici est la fraîcheur. On ne cherche plus à progresser physiquement, mais à arriver reposé et ultra-performant.",
      categories: [
        {
          name: "Entraînement & Physio",
          items: [
            { 
              id: "taper", 
              label: "Phase de Taper", 
              time: "J-14 ou J-7",
              desc: "Réduction drastique du volume d'entraînement.",
              details: "Réduction du volume global en maintenant l'intensité"
            },
          ]
        },
        {
          name: "Nutrition & Hygiène",
          items: [
            { 
              id: "sleep_bank", 
              label: "Sommeil 'Banking'", 
              time: "J-14 à J-0",
              desc: "Cherche à 'stocker' du sommeil.",
              details: (
                <>
                  <p>Cherche à stocker du sommeil.</p>
                  <p className="mt-1">Vise +45 à +90 min/nuit.</p>
                  <p className="mt-1">La régularité {'>'} Quantité absolue.</p>
                </>
              )
            }
          ]
        }
      ]
    },
    {
      title: "Phase 2 : J-6 à J-1",
      subtitle: "La Semaine Critique",
      icon: <Zap className="w-5 h-5" />,
      proTip: "Tout le monde est prêt physiquement. Ceux qui gagnent sont ceux qui optimisent les détails que les autres négligent.",
      categories: [
        {
          name: "Nutrition & Hydratation",
          items: [
             { 
              id: "nitrates_load", 
              label: "Charge de Jus de Betterave", 
              time: "J-6 à J-1",
              desc: "Saturer le corps en nitrates (1-2 shots/jour).",
              details: (
                <>
                  <p>70-140 ml/jour pour augmenter l'oxyde nitrique.</p>
                  <p className="mt-1">Améliore l'économie de l'effort et l'utilisation de l'ATP Pcr.</p>
                  <p className="mt-1 text-red-600 font-semibold">Attention : Éviter bains de bouche antiseptiques.</p>
                </>
              )
            },
            { 
              id: "sodium", 
              label: "Hyperhydratation sodée", 
              time: "J-3 à J-1",
              desc: "Eau riche en sodium ou électrolytes.",
              details: "Bois de l'eau riche en sodium ou ajoute des électrolytes à ton hydratation si tu ne le fais pas quotidiennement."
            },
             { 
              id: "residues", 
              label: "Régime sans résidus", 
              time: "J-2",
              desc: "Élimine les fibres (légumes crus, grains entiers).",
              details: (
                <div className="space-y-4">
                  <p>
                    Élimine les fibres (légumes crus, grains entiers) pour vider le tractus intestinal. Cela évite les troubles digestifs et peut te faire gagner 500g à 1kg sur la balance ("poids mort" intestinal).
                  </p>
                  
                  {/* Tableau 1 : À Éviter */}
                  <div className="rounded-lg border border-slate-200 overflow-hidden">
                    <table className="w-full text-[10px] text-left border-collapse">
                      <thead>
                        <tr className="bg-red-50 text-red-800 border-b border-red-100">
                          <th className="p-2 font-bold w-1/3">Catégorie (Stop)</th>
                          <th className="p-2 font-bold">Exemples</th>
                          <th className="p-2 font-bold">Pourquoi stopper</th>
                        </tr>
                      </thead>
                      <tbody className="bg-white">
                        <tr className="border-b border-slate-100">
                          <td className="p-2 font-bold text-slate-700">Fibres insolubles</td>
                          <td className="p-2 text-slate-600">Légumes crus (brocoli, chou), graines, pain complet</td>
                          <td className="p-2 text-slate-500">↑ volume, ↑ fermentation → ballonnements</td>
                        </tr>
                        <tr className="border-b border-slate-100">
                          <td className="p-2 font-bold text-slate-700">Légumineuses</td>
                          <td className="p-2 text-slate-600">Lentilles, pois chiches, haricots</td>
                          <td className="p-2 text-slate-500">↑ gaz + digestion lente</td>
                        </tr>
                        <tr className="border-b border-slate-100">
                          <td className="p-2 font-bold text-slate-700">Céréales complètes</td>
                          <td className="p-2 text-slate-600">Riz complet, quinoa, avoine complet</td>
                          <td className="p-2 text-slate-500">↑ fibre insoluble → contenu intestinal élevé</td>
                        </tr>
                        <tr className="border-b border-slate-100">
                          <td className="p-2 font-bold text-slate-700">Fruits riches en fibres</td>
                          <td className="p-2 text-slate-600">Framboises, poires, pommes avec peau</td>
                          <td className="p-2 text-slate-500">↑ fibre insoluble, fermentation</td>
                        </tr>
                        <tr className="border-b border-slate-100">
                          <td className="p-2 font-bold text-slate-700">Noix / fruits secs</td>
                          <td className="p-2 text-slate-600">Amandes, noix, pruneaux</td>
                          <td className="p-2 text-slate-500">Gras ralentit vidange, difficile à digérer</td>
                        </tr>
                         <tr className="border-b border-slate-100">
                          <td className="p-2 font-bold text-slate-700">Boissons gazeuses</td>
                          <td className="p-2 text-slate-600">Soda, eau gazeuse</td>
                          <td className="p-2 text-slate-500">Ballonnements, CO₂</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>

                  {/* Tableau 2 : Recommandé */}
                  <div className="rounded-lg border border-slate-200 overflow-hidden">
                    <table className="w-full text-[10px] text-left border-collapse">
                      <thead>
                        <tr className="bg-green-50 text-green-800 border-b border-green-100">
                          <th className="p-2 font-bold w-1/3">Objectif (Go)</th>
                          <th className="p-2 font-bold">Aliments recommandés</th>
                          <th className="p-2 font-bold">Notes pratiques</th>
                        </tr>
                      </thead>
                      <tbody className="bg-white">
                        <tr className="border-b border-slate-100">
                          <td className="p-2 font-bold text-slate-700">Glucides digestibles</td>
                          <td className="p-2 text-slate-600">Riz blanc, pâtes blanches, pomme de terre, banane mûre</td>
                          <td className="p-2 text-slate-500">Maintient glycogène → énergie intacte</td>
                        </tr>
                        <tr className="border-b border-slate-100">
                          <td className="p-2 font-bold text-slate-700">Protéines faciles</td>
                          <td className="p-2 text-slate-600">Blanc de poulet, dinde, œufs, whey</td>
                          <td className="p-2 text-slate-500">Pas de fibre → digestion rapide</td>
                        </tr>
                        <tr className="border-b border-slate-100">
                          <td className="p-2 font-bold text-slate-700">Lipides</td>
                          <td className="p-2 text-slate-600">Très modérés (huile d'olive crue)</td>
                          <td className="p-2 text-slate-500">Légers pour le repas, pas de friture</td>
                        </tr>
                        <tr className="border-b border-slate-100">
                          <td className="p-2 font-bold text-slate-700">Liquides & sodium</td>
                          <td className="p-2 text-slate-600">Eau plate, Vichy plate, bouillon</td>
                          <td className="p-2 text-slate-500">Maintien hydratation et sodium</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              )
            },
            { 
              id: "carb_load", 
              label: "Augmentation Glucidique Contrôlée", 
              time: "J-1",
              desc: "Cible : 4-5g de glucides / kg de PDC.",
              details: (
                <>
                  <p>Cible : 4-5g de glucides / kg de PDC, à répartir sur la journée.</p>
                  <p className="mt-1">Dernier gros apport ≥6 h avant coucher.</p>
                </>
              )
            },
          ]
        },
        {
          name: "Suppléments & Logistique",
          items: [
            { 
              id: "cafeine_reset", 
              label: "Arrêt de la Caféine", 
              time: "J-7 à J-2",
              desc: "'Caffeine reset' pour la sensibilité.",
              details: (
                <>
                  <p>Se sevrer une semaine avant pour resensibiliser les récepteurs.</p>
                  <p className="mt-1">Ajustement recommandé si grand consommateur de café pour éviter les troubles : Réduire à ≤50 mg/j, pas arrêt total.</p>
                </>
              )
            },
            { 
              id: "creatine", 
              label: "Maintien Créatine et Beta-Alanine", 
              time: "Quotidien",
              desc: "Maintenir la dose de croisière (3-5g).",
              details: (
                <>
                  <p>Si tu en prends déjà, maintenir la dose de croisière.</p>
                  <p className="mt-1 text-red-600 font-semibold">Ne commence surtout pas maintenant si tu n'en consommes pas.</p>
                </>
              )
            },
            { 
              id: "gear_check", 
              label: "Check-up Matériel", 
              time: "J-1",
              desc: "Vérification complète : chaussures, straps, magnésie.",
              details: (
                <>
                  <p>Chaussures, straps, nutrition glucidique, électrolytes.</p>
                  <p className="mt-1">Rien de nouveau le jour de la compétition.</p>
                </>
              )
            }
          ]
        }
      ]
    },
    {
      title: "Phase 3 : Le Jour J",
      subtitle: "Avant l'épreuve",
      icon: <Flame className="w-5 h-5" />,
      proTip: "L'objectif de l'échauffement est l'excitation neuronale, pas la fatigue.",
      categories: [
        {
          name: "Chronologie Nutritionnelle",
          items: [
            { 
              id: "pre_meal", 
              label: "Repas Pré-compétition", 
              time: "H-4 à H-3",
              desc: "Glucides ++, pauvre en lipides/fibres.",
              details: (
                <>
                  <p>Riche en glucides, modéré en protéines (0,25-0,3g/kg max), très pauvre en lipides et fibres.</p>
                  <p className="mt-1">Exemple : Riz blanc, compote, blanc de poulet ou protéine en poudre.</p>
                  <p className="mt-1">Facile à digérer, énergie rapide.</p>
                </>
              )
            },
            { 
              id: "nitrate_final", 
              label: "Dernier shot de betterave", 
              time: "H-2.5",
              desc: "Dernier shot de betterave concentré.",
              details: (
                <>
                  <p>Dernier shot de betterave.</p>
                  <p className="mt-1">Le pic de nitrates plasmatiques survient 2 à 3h après ingestion.</p>
                </>
              )
            },
            { 
              id: "cafeine_final", 
              label: "Caféine Elite", 
              time: "H-1",
              desc: "Dosage : 3 mg / kg de poids de corps.",
              details: (
                <>
                  <p>2 à 3 mg/kg fractionné en 2 prises par exemple sur des parcours différents (c'est beaucoup, teste-le avant !).</p>
                  <p className="mt-1">Effet : Réduction de la perception de l'effort (RPE) et meilleure réactivité.</p>
                </>
              )
            }
          ]
        },
        {
          name: "Échauffement (Warm-up)",
          items: [
            { 
              id: "racs", 
              label: "RACs Full-Body", 
              time: "H-30 min",
              desc: "Mobilisation articulaire complète.",
              details: "Échauffement articulaire complet."
            },
            { 
              id: "pap_cap", 
              label: "PAP Capsulaire", 
              time: "H-15 min",
              desc: "Effort max sur contraction PAILs.",
              details: (
                <>
                  <p>Effort max sur contraction PAILs (Flexion d'épaule et Rotation externe d'épaule + fonction spécifique).</p>
                  <p className="mt-1 font-semibold text-red-600">Attention : Volume minimal pour ne pas cramer le système nerveux.</p>
                </>
              )
            },
            { 
              id: "plio", 
              label: "Pliométrie extensive", 
              time: "H-10 min",
              desc: "Volume bas sur sauts intensité moyenne.",
              details: "Volume sans aller à la fatigue sur des sauts d'intensité basse/moyenne."
            },
            { 
              id: "pap_muscular", 
              label: "PAP Musculaire, Sprints et sauts", 
              time: "H-5 min",
              desc: "Intensité max, volume très bas.",
              details: "Intensité max, volume bas."
            },
            { 
              id: "thermal", 
              label: "Veste thermique", 
              time: "Départ",
              desc: "Garder le corps au chaud jusqu'au bout.",
              details: "Garder le corps au chaud jusqu'au bout."
            }
          ]
        }
      ]
    },
    {
      title: "Phase 4 : En Course",
      subtitle: "Gestion & Entre-runs",
      icon: <Brain className="w-5 h-5" />,
      proTip: "Quand l’épreuve s’étire, la différence entre les bons et les champions se joue dans la gestion entre les runs.",
      categories: [
        {
          name: "Protocole Entre 2 Runs",
          items: [
            { 
              id: "active_recov", 
              label: "Récupération Active", 
              time: "H + 2 min",
              desc: "Marche active. Ne t'assois pas.",
              details: (
                <>
                  <p>Marche active. Ne t'assois pas.</p>
                  <p className="mt-1">Respire par le nez pour faire redescendre le rythme cardiaque.</p>
                </>
              )
            },
            { 
              id: "hydro_electro", 
              label: "Hydratation", 
              time: "H + 5 min",
              desc: "200-300ml d'eau avec électrolytes.",
              details: (
                <>
                  <p>Bois 200-300ml d'eau avec des électrolytes.</p>
                  <p className="mt-1">Si tu n'en as pas, une eau minérale type Vichy Célestins est parfaite.</p>
                  <p className="mt-1 text-red-600">Attention pour la Vichy si estomac sensible.</p>
                </>
              )
            },
            { 
              id: "refuel", 
              label: "Apport Énergie", 
              time: "H + 10 min",
              desc: "Demi-banane ou miel si nécessaire.",
              details: (
                <>
                  <p>Si tu te sens vide : Une demi-banane ou une petite gorgée de miel dilué avec de l'eau.</p>
                  <p className="mt-1">Si tu te sens bien : Ne mange rien de solide.</p>
                </>
              )
            },
            { 
              id: "mouth_rinse", 
              label: "Relance", 
              time: "H - 5 min",
              desc: "Rinçage de bouche sucré (recracher).",
              details: (
                <>
                  <p>Un dernier rinçage de bouche avec une boisson sucrée (dilué à l'eau), puis recrache si possible.</p>
                  <p className="mt-1">Remets-toi en mouvement (petits sauts, rotations articulaires).</p>
                </>
              )
            }
          ]
        },
        {
          name: "Mental In-Game",
          items: [
            { 
              id: "self_talk", 
              label: "Self-Talk Positif", 
              time: "Pendant",
              desc: "Dialogue interne instructif.",
              details: (
                <>
                  <p>Dialogue interne instructif.</p>
                  <p className="mt-1">Focus sur les consignes techniques et l'instant présent plutôt que sur le résultat final.</p>
                </>
              )
            }
          ]
        }
      ]
    }
  ];

  const toggleItem = (id) => {
    setCheckedItems(prev => ({ ...prev, [id]: !prev[id] }));
  };

  const toggleDetails = (e, id) => {
    e.stopPropagation();
    setOpenDetails(prev => ({ ...prev, [id]: !prev[id] }));
  };

  const toggleSection = (idx) => {
    setExpandedSections(prev => ({ ...prev, [idx]: !prev[idx] }));
  };

  const calculateProgress = (phaseIdx) => {
    const phase = sections[phaseIdx];
    let total = 0, checked = 0;
    phase.categories.forEach(cat => cat.items.forEach(item => {
      total++;
      if (checkedItems[item.id]) checked++;
    }));
    return (checked / total) * 100;
  };

  return (
    <div className="min-h-screen bg-slate-50 p-4 md:p-8 font-sans text-slate-900 pb-24">
      <div className="max-w-md mx-auto">
        {/* Header */}
        <header className="mb-6 text-center">
          <h1 className="text-3xl font-black tracking-tighter text-red-600 italic">COMPETITION READY.</h1>
          <h2 className="text-sm font-bold text-slate-400 uppercase tracking-[0.3em]">Checklist</h2>
        </header>

        {/* Tab Navigation */}
        <div className="flex justify-between mb-8 bg-white/60 backdrop-blur-xl p-1.5 rounded-2xl border border-white shadow-sm">
          {sections.map((section, i) => (
            <button
              key={i}
              onClick={() => setActiveTab(i)}
              className={`flex-1 py-3 rounded-xl flex flex-col items-center transition-all duration-300 ${
                activeTab === i ? 'bg-white shadow-md text-red-600 scale-[1.05]' : 'text-slate-300 hover:text-slate-500'
              }`}
            >
              <div className={`${activeTab === i ? 'scale-110' : 'scale-100'} transition-transform`}>
                {section.icon}
              </div>
              <span className="text-[8px] mt-1 font-black uppercase tracking-widest">Phase {i+1}</span>
            </button>
          ))}
        </div>

        {/* Current Phase Overview */}
        <div className="mb-6 px-2">
          <div className="flex justify-between items-end mb-2">
            <div>
              <h3 className="text-2xl font-black text-slate-800 tracking-tight leading-none">{sections[activeTab].title}</h3>
              <p className="text-red-500 font-bold text-xs uppercase mt-1 tracking-wider">{sections[activeTab].subtitle}</p>
            </div>
            <span className="text-xs font-black text-slate-300 tracking-tighter">{Math.round(calculateProgress(activeTab))}%</span>
          </div>
          <div className="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden">
            <div 
              className="h-full bg-red-600 transition-all duration-700 ease-out"
              style={{ width: `${calculateProgress(activeTab)}%` }}
            />
          </div>
        </div>

        {/* Categories & Items */}
        <div className="space-y-4">
          {sections[activeTab].categories.map((cat, catIdx) => {
            const sectionKey = `${activeTab}-${catIdx}`;
            const isExpanded = expandedSections[sectionKey];

            return (
              <div key={catIdx} className="bg-white/80 backdrop-blur-md border border-white rounded-[1.5rem] shadow-sm overflow-hidden">
                <button 
                  onClick={() => toggleSection(sectionKey)}
                  className="w-full p-4 flex justify-between items-center hover:bg-white/40 transition-colors"
                >
                  <span className="font-black text-[10px] uppercase tracking-[0.15em] text-slate-400">{cat.name}</span>
                  {isExpanded ? <ChevronUp size={14} className="text-red-400"/> : <ChevronDown size={14} className="text-slate-300"/>}
                </button>
                
                <div className={`transition-all duration-300 ease-in-out ${!isExpanded ? 'max-h-0' : 'max-h-[1500px]'} overflow-hidden`}>
                  <div className="p-3 pt-0 space-y-2">
                    {cat.items.map((item) => (
                      <div key={item.id} className="rounded-2xl border border-slate-50 overflow-hidden transition-all">
                        <div 
                          onClick={() => toggleItem(item.id)}
                          className={`flex items-start gap-3 p-3 cursor-pointer transition-all ${
                            checkedItems[item.id] ? 'bg-red-50/50' : 'bg-white hover:bg-slate-50'
                          }`}
                        >
                          <div className="mt-1 flex-shrink-0">
                            {checkedItems[item.id] ? (
                              <CheckCircle2 className="text-red-600 w-5 h-5" />
                            ) : (
                              <Circle className="text-slate-200 w-5 h-5 group-hover:text-red-200" />
                            )}
                          </div>
                          
                          <div className="flex-1">
                            <div className="flex justify-between items-start">
                              <div className="flex flex-col">
                                <span className="text-[9px] font-black text-red-500 uppercase tracking-tighter mb-0.5">{item.time}</span>
                                <p className={`font-bold text-sm leading-tight transition-colors ${checkedItems[item.id] ? 'text-red-700' : 'text-slate-800'}`}>
                                  {item.label}
                                </p>
                              </div>
                              <button 
                                onClick={(e) => toggleDetails(e, item.id)}
                                className={`p-1.5 rounded-lg transition-all ${openDetails[item.id] ? 'bg-red-600 text-white' : 'bg-slate-50 text-slate-300'}`}
                              >
                                <Info size={14} />
                              </button>
                            </div>
                          </div>
                        </div>

                        {/* Detailed Description Drawer */}
                        <div className={`transition-all duration-300 ease-in-out overflow-hidden bg-white/80 ${openDetails[item.id] ? 'max-h-[800px] p-4 border-t border-slate-50' : 'max-h-0 opacity-0'}`}>
                           <div className="text-[11px] text-slate-600 leading-relaxed font-medium">
                            {item.details}
                           </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        {/* Dynamic Pro Tip Footer */}
        <div className="mt-8 p-5 bg-white rounded-3xl border border-slate-100 shadow-xl relative overflow-hidden flex gap-4 animate-in fade-in duration-700">
          <div className="bg-red-600 p-2.5 rounded-2xl text-white shadow-lg shadow-red-100 self-start">
            <ShieldCheck size={20} />
          </div>
          <div>
            <h4 className="font-black text-[10px] uppercase tracking-widest text-red-600">Conseil Pro Phase {activeTab + 1}</h4>
            <p className="text-[11px] leading-relaxed mt-1 font-bold text-slate-700 italic">
              "{sections[activeTab].proTip}"
            </p>
          </div>
        </div>

        <p className="text-center text-slate-300 text-[9px] font-black uppercase tracking-[0.3em] mt-8">
          Next Athlete Performance System v1.0
        </p>
      </div>
    </div>
  );
}

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(React.createElement(App));
    </script>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=True)

st.caption("Next Athlete Performance System v1.0")
