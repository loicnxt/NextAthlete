import React, { useState } from 'react';
import { 
  CheckCircle2, 
  Circle, 
  Flame, 
  Zap, 
  Brain, 
  ChevronDown, 
  ChevronUp, 
  Info, 
  Activity,
  Clock,
  Timer,
  ShieldCheck,
  ZapOff
} from 'lucide-react';

const App = () => {
  const [activeTab, setActiveTab] = useState(0);
  const [checkedItems, setCheckedItems] = useState({});
  const [expandedSections, setExpandedSections] = useState({ "0-0": true, "1-0": true, "2-0": true, "3-0": true });
  const [openDetails, setOpenDetails] = useState({});

  const sections = [
    {
      title: "Phase 1 : J-14 à J-7",
      subtitle: "L'Affûtage & La Fondation",
      icon: <Activity className="w-5 h-5" />,
      proTip: "Le but ici est la fraîcheur. Ne cherche plus à progresser physiquement, mais à arriver reposé et ultra-précis.",
      categories: [
        {
          name: "Entraînement & Physio",
          items: [
            { 
              id: "taper", 
              label: "Phase de Taper", 
              time: "J-14",
              desc: "Réduction drastique du volume d'entraînement.",
              details: "Réduction du volume global. On maintient l'intensité mais on diminue la durée des séances pour laisser le corps surcompenser."
            },
            { 
              id: "massage", 
              label: "Soins des tissus mous", 
              time: "J-10 Max",
              desc: "Dernier massage profond (Deep Tissue).",
              details: "À faire impérativement avant J-10. Après cette limite, le risque de courbatures ou de perte de tonus musculaire (effet 'jambes molles') est trop important."
            }
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
              details: "Augmenter le temps de sommeil (9h-10h) deux semaines avant. Améliore les temps de réaction et la précision sur les obstacles techniques."
            }
          ]
        }
      ]
    },
    {
      title: "Phase 2 : J-6 à J-1",
      subtitle: "La Semaine Critique",
      icon: <Zap className="w-5 h-5" />,
      proTip: "Le sevrage de caféine est difficile les 3 premiers jours, mais le boost le jour J sera ton plus grand avantage nerveux.",
      categories: [
        {
          name: "Nutrition & Hydratation",
          items: [
            { 
              id: "carb_load", 
              label: "Augmentation Glucidique", 
              time: "J-1",
              desc: "Cible : 4-5g de glucides / kg de PDC.",
              details: "L'objectif est de maximiser les stocks de glycogène musculaire et hépatique pour avoir un réservoir d'énergie plein."
            },
            { 
              id: "residues", 
              label: "Régime sans résidus", 
              time: "J-2",
              desc: "Élimine les fibres (légumes crus, grains entiers).",
              details: "Vider le tractus intestinal pour éviter les troubles digestifs. Gain potentiel de 500g à 1kg sur la balance (poids mort intestinal)."
            },
            { 
              id: "sodium", 
              label: "Hyperhydratation sodée", 
              time: "J-3 à J-1",
              desc: "Eau riche en sodium ou électrolytes.",
              details: "Le sodium aide à retenir le fluide dans le plasma sanguin (expansion du volume plasmatique), crucial pour la thermorégulation et le débit cardiaque."
            },
            { 
              id: "nitrates_load", 
              label: "Charge Jus de Betterave", 
              time: "J-6 à J-1",
              desc: "Saturer le corps en nitrates (1-2 shots/jour).",
              details: "70-140 ml (300-600mg nitrates). Vasodilatateur puissant, améliore l'économie de l'effort et l'utilisation de l'ATP Pcr."
            }
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
              details: "Se sevrer une semaine avant pour resensibiliser les récepteurs à l'adénosine. Le boost du jour J sera explosif."
            },
            { 
              id: "creatine", 
              label: "Maintien Créatine", 
              time: "Quotidien",
              desc: "Maintenir la dose de croisière (3-5g).",
              details: "Si tu en prends déjà, continue. Ne commence surtout pas maintenant pour éviter une rétention d'eau imprévue."
            },
            { 
              id: "gear_check", 
              label: "Check-up Matériel", 
              time: "J-2",
              desc: "Vérification complète : chaussures, straps, magnésie.",
              details: "Rien de nouveau le jour de la compétition. Teste tes straps et ta nutrition une dernière fois."
            }
          ]
        }
      ]
    },
    {
      title: "Phase 3 : Le Jour J",
      subtitle: "Avant l'épreuve",
      icon: <Flame className="w-5 h-5" />,
      proTip: "Respecte scrupuleusement le timing du dernier shot de betterave. L'effet de pic est une fenêtre physiologique précise.",
      categories: [
        {
          name: "Chronologie Nutritionnelle",
          items: [
            { 
              id: "pre_meal", 
              label: "Repas Pré-compétition", 
              time: "H-4 à H-3",
              desc: "Glucides ++, pauvre en lipides/fibres.",
              details: "Exemple : Riz blanc, compote, blanc de poulet ou protéine en poudre. Facile à digérer, énergie rapide."
            },
            { 
              id: "nitrate_final", 
              label: "Nitrate Shot Final", 
              time: "H-2.5",
              desc: "Dernier shot de betterave concentré.",
              details: "Le pic de nitrates plasmatiques survient 2 à 3h après l'ingestion. C'est le moment clé pour l'oxyde nitrique."
            },
            { 
              id: "cafeine_final", 
              label: "Caféine Elite", 
              time: "H-1",
              desc: "Dosage : 3 mg / kg de poids de corps.",
              details: "Effet : Réduction de la perception de l'effort (RPE) et mobilisation des acides gras. À prendre avant le run le plus important."
            },
            { 
              id: "tampon", 
              label: "Tampon Acide", 
              time: "H-1",
              desc: "Bicarbonate ou Beta-Alanine.",
              details: "Si l'épreuve est très lactique (1-8 min). Attention : peut causer des troubles gastriques majeurs. À tester impérativement avant."
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
              details: "Réveiller chaque articulation sans créer de fatigue nerveuse."
            },
            { 
              id: "pap_cap", 
              label: "PAP Capsulaire", 
              time: "H-15 min",
              desc: "Effort max sur contraction PAILs.",
              details: "Flexion d'épaule et Rotation externe d'épaule spécifique pour préparer le grip et les suspensions."
            },
            { 
              id: "plio", 
              label: "Pliométrie extensive", 
              time: "H-10 min",
              desc: "Volume bas sur sauts intensité moyenne.",
              details: "Réveiller les tendons sans entamer les réserves d'énergie."
            },
            { 
              id: "pap_muscular", 
              label: "PAP Musculaire & Sprints", 
              time: "H-5 min",
              desc: "Intensité max, volume très bas.",
              details: "Quelques sauts max ou sprints courts pour la potentiation nerveuse finale."
            },
            { 
              id: "thermal", 
              label: "Veste thermique", 
              time: "Départ",
              desc: "Garder le corps au chaud jusqu'au bout.",
              details: "Ne laisse pas tes muscles se refroidir pendant l'attente sur la ligne de départ."
            }
          ]
        }
      ]
    },
    {
      title: "Phase 4 : En Course",
      subtitle: "Gestion & Entre-runs",
      icon: <Brain className="w-5 h-5" />,
      proTip: "Le 'Mouth Rinsing' (rinçage de bouche) trompe ton cerveau en lui faisant croire que de l'énergie arrive, sans peser sur ton estomac.",
      categories: [
        {
          name: "Protocole Entre 2 Runs",
          items: [
            { 
              id: "active_recov", 
              label: "Récupération Active", 
              time: "H + 2 min",
              desc: "Marche active. Ne t'assois pas.",
              details: "Respiration nasale profonde pour faire redescendre le rythme cardiaque et évacuer les déchets métaboliques."
            },
            { 
              id: "hydro_electro", 
              label: "Hydratation Sodée", 
              time: "H + 5 min",
              desc: "200-300ml d'eau avec électrolytes.",
              details: "Une eau type Vichy Célestins est parfaite pour tamponner l'acidité produite par le premier run."
            },
            { 
              id: "refuel", 
              label: "Apport Énergie", 
              time: "H + 10 min",
              desc: "Demi-banane ou miel si nécessaire.",
              details: "Si tu te sens bien, ne mange rien de solide. Le sang doit rester dans tes muscles, pas dans ton estomac."
            },
            { 
              id: "mouth_rinse", 
              label: "Relance & Rinçage", 
              time: "H - 5 min",
              desc: "Rinçage de bouche sucré (recracher).",
              details: "Dernière relance : petits sauts et rotations articulaires pour préparer le second run."
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
              details: "Focus sur les consignes techniques et l'instant présent plutôt que sur le résultat final."
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
                        <div className={`transition-all duration-300 ease-in-out overflow-hidden bg-white/80 ${openDetails[item.id] ? 'max-h-40 p-4 border-t border-slate-50' : 'max-h-0 opacity-0'}`}>
                           <p className="text-[11px] text-slate-600 leading-relaxed font-medium">
                            {item.details}
                           </p>
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
};

export default App;
