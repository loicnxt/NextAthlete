import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Checklist Competition", layout="centered", initial_sidebar_state="collapsed")

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

        const ICONS = {
    heartbeat: `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
     fill="none" stroke="currentColor" stroke-width="2"
     stroke-linecap="round" stroke-linejoin="round"
     class="w-6 h-6">
  <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
</svg>`,

    bolt: `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
     fill="none" stroke="currentColor" stroke-width="2"
     stroke-linecap="round" stroke-linejoin="round"
     class="w-6 h-6">
  <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
</svg>`,

    flame: `
<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="M15.362 5.214A8.252 8.252 0 0 1 12 21 8.25 8.25 0 0 1 6.038 7.047 8.287 8.287 0 0 0 9 9.601a8.983 8.983 0 0 1 3.361-6.867 8.21 8.21 0 0 0 3 2.48Z" />
  <path stroke-linecap="round" stroke-linejoin="round" d="M12 18a3.75 3.75 0 0 0 .495-7.468 5.99 5.99 0 0 0-1.925 3.547 5.975 5.975 0 0 1-2.133-1.001A3.75 3.75 0 0 0 12 18Z" />
</svg>`,

    brain: `
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-brain"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M15.5 13a3.5 3.5 0 0 0 -3.5 3.5v1a3.5 3.5 0 0 0 7 0v-1.8" /><path d="M8.5 13a3.5 3.5 0 0 1 3.5 3.5v1a3.5 3.5 0 0 1 -7 0v-1.8" /><path d="M17.5 16a3.5 3.5 0 0 0 0 -7h-.5" /><path d="M19 9.3v-2.8a3.5 3.5 0 0 0 -7 0" /><path d="M6.5 16a3.5 3.5 0 0 1 0 -7h.5" /><path d="M5 9.3v-2.8a3.5 3.5 0 0 1 7 0v10" />
</svg>`
};


        // Structure des données (exactement comme ton React original)
        const sections = [
            {
                title: "Phase 1 : J-14 à J-7",
                subtitle: "L'Affûtage & La Fondation",
                icon: "heartbeat",
                proTip: "Le but ici est la fraîcheur. On ne cherche plus à progresser physiquement, mais à arriver reposé et ultra-performant.",
                categories: [
                    {
                        name: "Entraînement & Physio",
                        items: [{ id: "taper", label: "Phase de Taper", time: "J-14 ou J-7", details: "Réduction du volume global en maintenant l'intensité." }]
                    },
                    {
                        name: "Nutrition & Hygiène",
                        items: [{ id: "sleep", label: "Sommeil 'Banking'", time: "J-14 à J-0", details: "Cherche à stocker du sommeil.<br>Vise +45 à +90 min/nuit.<br>La régularité > Quantité." }]
                    }
                ]
            },
            {
                title: "Phase 2 : J-6 à J-1",
                subtitle: "La Semaine Critique",
                icon: "bolt",
                proTip: "Tout le monde est prêt physiquement. Ceux qui gagnent sont ceux qui optimisent les détails que les autres négligent.",
                categories: [
                    {
                        name: "Nutrition & Hydratation",
                        items: [
                            { id: "beet", label: "Charge de Jus de Betterave", time: "J-6 à J-1", details: `70-140 ml/jour pour augmenter l'oxyde nitrique.<br>Améliore l'économie de l'effort et l'utilisation de l'ATP Pcr.<br> <span class="text-red-600 font-semibold">Attention : Éviter bains de bouche antiseptiques.</span>` },
                            { id: "sodium", label: "Hyperhydratation sodée", time: "J-3 à J-1", details: "Bois de l'eau riche en sodium ou ajoute des électrolytes à ton hydratation si tu ne le fais pas quotidiennement." },
                            { id: "residues", label: "Régime sans résidus", time: "J-2", details: `
<div class="space-y-4">
    <p>
        Élimine les fibres (légumes crus, grains entiers) pour vider le tractus intestinal. Cela évite les troubles digestifs et peut te faire gagner 500g à 1kg sur la balance ("poids mort" intestinal).
    </p>
    <div class="rounded-lg border border-slate-200 overflow-hidden">
        <table class="w-full text-[10px] text-left border-collapse">
            <thead>
                <tr class="bg-red-50 text-red-800 border-b border-red-100">
                    <th class="p-2 font-bold w-1/3">Catégorie (Stop)</th>
                    <th class="p-2 font-bold">Exemples</th>
                    <th class="p-2 font-bold">Pourquoi stopper</th>
                </tr>
            </thead>
            <tbody class="bg-white">
                <tr class="border-b border-slate-100">
                    <td class="p-2 font-bold text-slate-700">Fibres insolubles</td>
                    <td class="p-2 text-slate-600">Légumes crus (brocoli, chou), graines, pain complet</td>
                    <td class="p-2 text-slate-500">↑ volume, ↑ fermentation → ballonnements</td>
                </tr>
                <tr class="border-b border-slate-100">
                    <td class="p-2 font-bold text-slate-700">Légumineuses</td>
                    <td class="p-2 text-slate-600">Lentilles, pois chiches, haricots</td>
                    <td class="p-2 text-slate-500">↑ gaz + digestion lente</td>
                </tr>
                <tr class="border-b border-slate-100">
                    <td class="p-2 font-bold text-slate-700">Céréales complètes</td>
                    <td class="p-2 text-slate-600">Riz complet, quinoa, avoine complet</td>
                    <td class="p-2 text-slate-500">↑ fibre insoluble → contenu intestinal élevé</td>
                </tr>
                <tr class="border-b border-slate-100">
                    <td class="p-2 font-bold text-slate-700">Fruits riches en fibres</td>
                    <td class="p-2 text-slate-600">Framboises, poires, pommes avec peau</td>
                    <td class="p-2 text-slate-500">↑ fibre insoluble, fermentation</td>
                </tr>
                <tr class="border-b border-slate-100">
                    <td class="p-2 font-bold text-slate-700">Noix / fruits secs</td>
                    <td class="p-2 text-slate-600">Amandes, noix, pruneaux</td>
                    <td class="p-2 text-slate-500">Gras ralentit vidange, difficile à digérer</td>
                </tr>
                <tr class="border-b border-slate-100">
                    <td class="p-2 font-bold text-slate-700">Boissons gazeuses</td>
                    <td class="p-2 text-slate-600">Soda, eau gazeuse</td>
                    <td class="p-2 text-slate-500">Ballonnements, CO₂</td>
                </tr>
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
                <tr class="border-b border-slate-100">
                    <td class="p-2 font-bold text-slate-700">Glucides digestibles</td>
                    <td class="p-2 text-slate-600">Riz blanc, pâtes blanches, pomme de terre, banane mûre</td>
                    <td class="p-2 text-slate-500">Maintient glycogène → énergie intacte</td>
                </tr>
                <tr class="border-b border-slate-100">
                    <td class="p-2 font-bold text-slate-700">Protéines faciles</td>
                    <td class="p-2 text-slate-600">Blanc de poulet, dinde, œufs, whey</td>
                    <td class="p-2 text-slate-500">Pas de fibre → digestion rapide</td>
                </tr>
                <tr class="border-b border-slate-100">
                    <td class="p-2 font-bold text-slate-700">Lipides</td>
                    <td class="p-2 text-slate-600">Très modérés (huile d'olive crue)</td>
                    <td class="p-2 text-slate-500">Légers pour le repas, pas de friture</td>
                </tr>
                <tr class="border-b border-slate-100">
                    <td class="p-2 font-bold text-slate-700">Liquides & sodium</td>
                    <td class="p-2 text-slate-600">Eau plate, Vichy plate, bouillon</td>
                    <td class="p-2 text-slate-500">Maintien hydratation et sodium</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
` },
                            { id: "carbs", label: "Augmentation Glucidique Contrôlée", time: "J-1", details: "Cible : 4-5g de glucides / kg de PDC, à répartir sur la journée.<br>Dernier gros apport ≥6 h avant coucher." }
                        ]
                    },
                    {
                        name: "Suppléments & Logistique",
                        items: [
                            { id: "caf_reset", label: "Arrêt de la Caféine", time: "J-7 à J-2", details: "Se sevrer une semaine avant pour resensibiliser les récepteurs.<br>Ajustement recommandé si grand consommateur de café pour éviter les troubles : Réduire à ≤50 mg/j, pas arrêt total." },
                            { id: "creatine", label: "Maintien Créatine et Beta-Alanine", time: "Quotidien", details: `Si tu en prends déjà, maintenir la dose de croisière.<br><span class="text-red-600 font-semibold">Ne commence surtout pas maintenant si tu n'en consommes pas.</span>` },
                            { id: "gear", label: "Check-up Matériel", time: "J-1", details: "Chaussures, straps, nutrition glucidique, électrolytes.<br>Rien de nouveau le jour de la compétition." }
                        ]
                    }
                ]
            },
            {
                title: "Phase 3 : Le Jour J",
                subtitle: "Avant l'épreuve",
                icon: "flame",
                proTip: "L'objectif de l'échauffement est l'excitation neuronale, pas la fatigue.",
                categories: [
                    {
                        name: "Chronologie Nutritionnelle",
                        items: [
                            { id: "pre_meal", label: "Repas Pré-compétition", time: "H-4 à H-3", details: "Riche en glucides, modéré en protéines (0,25-0,3g/kg max), très pauvre en lipides et fibres.<br>Exemple : Riz blanc, compote, blanc de poulet ou protéine en poudre.<br>Facile à digérer, énergie rapide." },
                            { id: "nitrate_final", label: "Dernier shot de betterave", time: "H-2.5 à H-2", details: "Dernier shot de betterave.<br>Le pic de nitrates plasmatiques survient 2 à 3h après ingestion." },
                            { id: "caf_final", label: "Caféine Elite", time: "H-1", details: "2 à 3 mg/kg fractionné en 2 prises par exemple sur des parcours différents (c'est beaucoup, teste-le avant !).<br>Effet : Réduction de la perception de l'effort (RPE) et meilleure réactivité." }
                        ]
                    },
                    {
                        name: "Warm-up",
                        items: [
                            { id: "pap", label: "PAP Musculaire", time: "H-15m", details: "Contractions max très brèves.\\nIntensité max, volume bas." },
                            { id: "vest", label: "Veste thermique", time: "Dép.", details: "Garder le corps au chaud jusqu'au signal." }
                        ]
                    }
                ]
            },
            {
                title: "Phase 4 : En Course",
                subtitle: "Gestion & Entre-runs",
                icon: "brain",
                proTip: "La différence entre les bons et les champions se joue dans la gestion entre les runs.",
                categories: [
                    {
                        name: "Protocole",
                        items: [
                            { id: "recov", label: "Récup Active", time: "H+2m", details: "Marche active.\\nNe t'assois pas.\\nRespire par le nez." },
                            { id: "rinse", label: "Relance (Rinçage)", time: "H-5m", details: "Rinçage de bouche sucré (recracher) pour stimuler le cerveau." }
                        ]
                    }
                ]
            }
        ];

        function App() {
            const [activeTab, setActiveTab] = useState(0);
            const [checkedItems, setCheckedItems] = useState({});
            const [openDetails, setOpenDetails] = useState({});

            const currentPhase = sections[activeTab];
            const allItems = currentPhase.categories.flatMap(c => c.items);
            const progress = (allItems.filter(i => checkedItems[i.id]).length / allItems.length) * 100;

            const toggleCheck = (id) => {
                setCheckedItems(prev => ({ ...prev, [id]: !prev[id] }));
            };

            const toggleInfo = (e, id) => {
                e.stopPropagation();
                setOpenDetails(prev => ({ ...prev, [id]: !prev[id] }));
            };

            return React.createElement('div', { className: 'max-w-md mx-auto p-4 pb-20' },
                // Header
                React.createElement('header', { className: 'mb-6 text-center' },
                    React.createElement('h1', { className: 'text-3xl font-black text-red-600 italic tracking-tighter' }, 'COMPETITION READY.'),
                    React.createElement('h2', { className: 'text-sm font-bold text-slate-400 uppercase tracking-[0.3em]' }, 'Checklist'),
                    React.createElement('p', { className: 'mt-3 text-[9px] font-black text-slate-300 uppercase tracking-[0.4em] opacity-80' }, 'NEXT ATHLETE PERFORMANCE SYSTEM')
                 ),

                // Navigation
                React.createElement('div', { className: 'flex justify-between mb-8 bg-white/60 backdrop-blur-xl p-1.5 rounded-2xl border border-white shadow-sm' },
                    sections.map((s, i) => React.createElement('button', {
                        key: i,
                        onClick: () => setActiveTab(i),
                        className: `flex-1 py-3 rounded-xl flex flex-col items-center transition-all ${activeTab === i ? 'bg-white shadow-md text-red-600 scale-[1.05]' : 'text-gray-300'}`
                    }, 
                        React.createElement('span', {
                            className: 'mb-1',
                            dangerouslySetInnerHTML: { __html: ICONS[s.icon] }
                        }),
                        React.createElement('span', { className: 'text-[8px] mt-1 font-black uppercase' }, `Phase ${i+1}`)
                    ))
                ),

                // Progress
                React.createElement('div', { className: 'mb-6 px-2' },
                    React.createElement('div', { className: 'flex justify-between items-end mb-2' },
                        React.createElement('div', null,
                            React.createElement('h2', { className: 'text-2xl font-black text-slate-800' }, currentPhase.title),
                            React.createElement('p', { className: 'text-red-500 font-bold text-[12px] uppercase' }, currentPhase.subtitle)
                        ),
                        React.createElement('span', { className: 'text-xs font-black text-slate-300' }, `${Math.round(progress)}%`)
                    ),
                    React.createElement('div', { className: 'w-full bg-slate-200 h-1.5 rounded-full overflow-hidden' },
                        React.createElement('div', { 
                            className: 'h-full bg-red-600 transition-all duration-700', 
                            style: { width: `${progress}%` } 
                        })
                    )
                ),

                // Content
                currentPhase.categories.map((cat, idx) => React.createElement('div', { key: idx, className: 'mb-6' },
                    React.createElement('h3', { className: 'font-black text-[10px] uppercase tracking-widest text-slate-400 mb-3 px-2' }, cat.name),
                    cat.items.map(item => React.createElement('div', { key: item.id, className: 'mb-2' },
                        React.createElement('div', { 
                            onClick: () => toggleCheck(item.id),
                            className: `flex items-center gap-3 p-4 bg-white rounded-2xl border border-white shadow-sm cursor-pointer transition-all ${checkedItems[item.id] ? 'bg-red-50/50 border-red-100' : ''}`
                        },
                            React.createElement('div', { className: `w-5 h-5 rounded-full border-2 flex items-center justify-center flex-shrink-0 ${checkedItems[item.id] ? 'bg-red-600 border-red-600' : 'border-slate-200'}` },
                                checkedItems[item.id] && React.createElement('span', { className: 'text-white text-[10px]' }, '✔')
                            ),
                            React.createElement('div', { className: 'flex-1' },
                                React.createElement('p', { className: 'text-[9px] font-black text-red-500 uppercase' }, item.time),
                                React.createElement('p', { className: `text-sm font-bold ${checkedItems[item.id] ? 'text-red-700' : 'text-slate-800'}` }, item.label)
                            ),
                           React.createElement('button', {
    onClick: (e) => toggleInfo(e, item.id),
    className: `
        p-1.5
        text-[11px]
        leading-none
        rounded-lg
        transition-all
        ${openDetails[item.id] 
            ? 'bg-red-600 text-white' 
            : 'bg-slate-50 text-slate-300'}
    `
}, 'ⓘ')
                        ),
                        openDetails[item.id] && React.createElement('div', { className: 'mt-1 p-4 bg-white/50 rounded-2xl text-[11px] text-slate-600 leading-relaxed border border-white' },
                            React.createElement('span', { style: { display: 'block', width: '100%' }, dangerouslySetInnerHTML: { __html: item.details } })
                        )
                    ))
                )),

                // Footer Tip
                React.createElement('div', { className: 'mt-8 p-5 bg-white rounded-3xl border border-slate-100 shadow-xl flex gap-4' },
                    React.createElement('div', { className: 'bg-red-600 p-2 rounded-2xl text-white shadow-lg shadow-red-100 self-start' },
                    React.createElement('svg', {
    xmlns: "http://www.w3.org/2000/svg",
    fill: "none",
    viewBox: "0 0 24 24",
    strokeWidth: 1.5,         
    stroke: "currentColor",
    className: "w-5 h-5"       
},
    React.createElement('path', {
        strokeLinecap: "round",
        strokeLinejoin: "round",
        d: "M9 12.75 11.25 15 15 9.75m-3-7.036A11.959 11.959 0 0 1 3.598 6 11.99 11.99 0 0 0 3 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285Z"
    })
)
),
                    React.createElement('div', null,
                        React.createElement('h4', { className: 'font-black text-[10px] uppercase text-red-600',  style: { letterSpacing: '0.2em' } }, `Conseil Pro Phase ${activeTab+1}`),
                        React.createElement('p', { className: 'text-[11px] font-bold text-slate-700 italic mt-1' }, `"${currentPhase.proTip}"`)
                    ))
            );
        }

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(React.createElement(App));
    </script>
</body>
</html>
"""

components.html(html_code + '''
<style>
    html, body {
        margin: 0;
        padding: 0;
        height: auto;
        overflow: visible;
        background-color: #ffffff;
    }
''', height=2000, scrolling=False)
