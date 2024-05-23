import streamlit as st

# Initialiser les états de session pour les sliders
if "volume" not in st.session_state:
    st.session_state.volume = 0
if "plage_horaire" not in st.session_state:
    st.session_state.plage_horaire = 1

# Fonctions pour ajuster les valeurs des sliders
def increase_volume():
    st.session_state.volume += 10000

def decrease_volume():
    if st.session_state.volume > 0:
        st.session_state.volume -= 10000

def increase_plage_horaire():
    st.session_state.plage_horaire += 1

def decrease_plage_horaire():
    if st.session_state.plage_horaire > 1:
        st.session_state.plage_horaire -= 1

# Titre de l'application
st.title("Calculateur de TPS")

# Description de l'application
st.write("""
Cette application permet de calculer le nombre de Transactions Par Seconde (TPS) 
en fonction du nombre de SMS souhaité et de la plage horaire sélectionnée.
""")

# Séparateur
st.markdown("---")

# Entrée du nombre de SMS souhaité avec des boutons aux extrémités
st.write("Veuillez selectionner le volume souhaité :")
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.button("-", on_click=decrease_volume, key="diminution_volume")
with col2:
    st.slider("", min_value=0, max_value=30000000, step=10000, key="volume")
with col3:
    st.button("+", on_click=increase_volume, key="augmentation_volume")

# Entrée de la plage horaire en heures avec des boutons aux extrémités
st.write("Veuillez sélectionner la plage horaire (en heures) :")
col4, col5, col6 = st.columns([1, 6, 1])
with col4:
    st.button("-", on_click=decrease_plage_horaire, key="diminution_plage_horaire")
with col5:
    st.slider("", min_value=1, max_value=24, step=1, key="plage_horaire")
with col6:
    st.button("+", on_click=increase_plage_horaire, key="augmentation_plage_horaire")

# Séparateur
st.markdown("---")

# Bouton Submit
submit = st.button("Submit")

# Calcul et affichage du résultat après avoir cliqué sur Submit
if submit:
    if st.session_state.plage_horaire > 0:  # Pour éviter la division par zéro
        tps = int(st.session_state.volume) / (int(st.session_state.plage_horaire) * 3600)
        # Utilisation de conteneurs stylisés pour afficher les résultats
        st.success(f"Le nombre de TPS requis pour envoyer {st.session_state.volume} requêtes en {st.session_state.plage_horaire} heures est : {int(tps)}")
    else:
        st.error("La plage horaire doit être supérieure à 0.")

# Footer
st.markdown("---")



st.write("Awa Mb, may 2024")
