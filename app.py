import streamlit as st
from openai import OpenAI
from transformers import AutoProcessor, MusicgenForConditionalGeneration
import torch
import scipy

# OpenAI client
client = OpenAI()

# Streamlit config
st.set_page_config(page_title="SongSketch", page_icon="🎵")
st.title("🎵 SongSketch - Paroles & Musique")

# Formulaire
with st.form("song_form"):
    titre = st.text_input("Titre de la chanson", "Ma chanson")
    theme = st.text_area("Idée / style (ex: rap, rock, nostalgie...)")
    submit = st.form_submit_button("Générer")

if submit:
    # Étape 1 : Génération paroles avec OpenAI
    st.subheader("📝 Paroles générées")
    prompt = f"Écris une chanson intitulée '{titre}' sur le thème : {theme}. Format couplet/refrain."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    paroles = response.choices[0].message.content
    st.text_area("Paroles :", paroles, height=300)

    # Étape 2 : Génération musique avec MusicGen
    st.subheader("🎶 Instrumental généré")
    with st.spinner("Création de la musique..."):
        model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
        processor = AutoProcessor.from_pretrained("facebook/musicgen-small")

        inputs = processor(
            text=[f"instrumental {theme}"],
            padding=True,
            return_tensors="pt"
        )

        audio_values = model.generate(**inputs, max_new_tokens=256)

        # Sauvegarde en wav
        sampling_rate = model.config.audio_encoder.sampling_rate
        scipy.io.wavfile.write("output_song.wav", rate=sampling_rate,
                               data=audio_values[0, 0].cpu().numpy())

        st.audio("output_song.wav", format="audio/wav")
