import streamlit as st
import torchaudio
from audiocraft.models import MusicGen

# Charger le modèle une seule fois (évite les rechargements lents)
@st.cache_resource
def load_model():
    model = MusicGen.get_pretrained("facebook/musicgen-small")
    model.set_generation_params(duration=8)  # durée par défaut (secondes)
    return model

model = load_model()

# Interface Streamlit
st.title("🎶 AI SongSketch - Générateur de musique")

# Texte descriptif
description = st.text_area("Décris ta musique :", "A happy pop melody with piano and claps")

# Choix du style
style = st.selectbox(
    "Choisis un style musical :",
    ["Pop", "Jazz", "Rap", "Folk", "Classique", "Rock", "Électronique"]
)

# Durée
duration = st.slider("Durée (secondes)", 5, 30, 8)

if st.button("🚀 Générer la musique"):
    with st.spinner("🎶 Génération en cours..."):
        # Mettre à jour les paramètres
        model.set_generation_params(duration=duration)

        # Construire la description
        full_desc = f"{style} style: {description}"

        # Génération
        wav = model.generate([full_desc])

        # Sauvegarde du fichier
        output_path = "output_song.wav"
        torchaudio.save(output_path, wav[0].cpu(), 32000)

        st.success("✅ Musique générée !")
        st.audio(output_path)
        with open(output_path, "rb") as f:
            st.download_button("⬇️ Télécharger", f, file_name="songsketch.wav")
