import streamlit as st
import datetime
import random

# 🔮 Liste de métiers du futur
def prevoir_metiers_du_futur():
    metiers = [
        "Architecte d'environnements virtuels",
        "Coach en déconnexion numérique",
        "Ingénieur en IA éthique",
        "Spécialiste des énergies renouvelables",
        "Facilitateur de travail hybride",
        "Designer d’expériences immersives",
        "Agriculteur urbain intelligent",
        "Consultant en transition écologique",
        "Analyste de données de santé",
        "Mentor en apprentissage automatique"
    ]
    return random.sample(metiers, 3)

# 🎯 Profil simulé
profil_utilisateur = {
    "localisation": "Abidjan",
    "niveau": "débutant",
    "types_travail": ["à distance", "temps partiel", "flexible"],
    "domaines": ["rédaction", "vente", "livraison"],
    "historique_feedback": {}
}

# 💼 Simulations d'opportunités
opportunites = [
    {"id": 1, "titre": "Rédacteur Web débutant", "description": "Travail à distance, flexible, idéal pour débutants", "domaine": "rédaction", "lien": "https://exemple.com/job1"},
    {"id": 2, "titre": "Livreur en ville", "description": "Travail sur site, besoin de permis", "domaine": "livraison", "lien": "https://exemple.com/job2"},
    {"id": 3, "titre": "Assistant commercial", "description": "Poste à distance, temps partiel, contact client", "domaine": "vente", "lien": "https://exemple.com/job3"},
    {"id": 4, "titre": "Développeur IA senior", "description": "CDI, expérience requise, temps plein", "domaine": "tech", "lien": "https://exemple.com/job4"}
]

# 🧠 Évaluation des opportunités
def analyser_faisabilite(offre, profil):
    score = 0
    description = offre["description"].lower()
    for critere in profil["types_travail"]:
        if critere in description:
            score += 1
    if offre["domaine"] in profil["domaines"]:
        score += 1
    if profil["niveau"] == "débutant" and "débutant" in description:
        score += 1
    if score >= 2:
        return "✅ Faisable pour vous"
    elif score == 1:
        return "⚠️ À étudier"
    else:
        return "❌ Peu adapté"

# 🖥️ Interface Streamlit
st.set_page_config(page_title="ORIOS AI", page_icon="🤖")
st.title("🤖 ORIOS - Opportunités de Travail Personnalisées")
st.markdown("### Aujourd'hui : " + datetime.date.today().strftime("%d %B %Y"))

# Métiers du futur
st.subheader("🌍 Métiers du futur à explorer")
for m in prevoir_metiers_du_futur():
    st.markdown(f"- {m}")

# Opportunité du jour
offre = random.choice(opportunites)
faisabilite = analyser_faisabilite(offre, profil_utilisateur)

st.subheader("💼 Opportunité du jour")
st.markdown(f"**{offre['titre']}**")
st.write(offre['description'])
st.markdown(f"[🔗 Lien vers l'offre]({offre['lien']})")
st.info(f"Évaluation : {faisabilite}")

# Choix utilisateur
choix = st.radio("Souhaitez-vous accepter cette offre ?", ("Oui", "Non"))
if st.button("Valider ma décision"):
    profil_utilisateur["historique_feedback"][offre["id"]] = "acceptée" if choix == "Oui" else "refusée"
    st.success(f"Décision enregistrée : {profil_utilisateur['historique_feedback'][offre['id']]}")

# Historique
st.subheader("📋 Historique de vos choix")
if not profil_utilisateur["historique_feedback"]:
    st.write("Aucune décision enregistrée pour le moment.")
else:
    for offre in opportunites:
        if offre["id"] in profil_utilisateur["historique_feedback"]:
            decision = profil_utilisateur["historique_feedback"][offre["id"]]
            st.write(f"- {offre['titre']} : {decision}")
