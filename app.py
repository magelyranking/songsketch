import streamlit as st
import torch
from transformers import AutoProcessor, MusicgenForConditionalGeneration

# Charger MusicGen depuis HuggingFace
@st.cache_resource
def load_model():
    processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
    model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
    return processor, model

processor, model = load_model()

st.title("🎶 AI SongSketch (Démo Cloud)")
text = st.text_input("Décris ta musique :", "A happy pop melody with piano and claps")

if st.button("Générer"):
    with st.spinner("⏳ Génération de la musique en cours..."):
        inputs = processor(text=[text], padding=True, return_tensors="pt")
        audio_values = model.generate(**inputs, max_new_tokens=256)

        # Conversion en numpy pour sauvegarder
        audio_array = audio_values[0, 0].cpu().numpy().astype("float32")

        import soundfile as sf
        sf.write("output.wav", audio_array, 32000)

        st.audio("output.wav")
        st.success("✅ Musique générée avec succès !")
