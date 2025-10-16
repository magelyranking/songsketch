import streamlit as st
from openai import OpenAI

# Teste si torch/musicgen dispo
HAS_MUSIC = True
try:
    import torch
    import scipy
    from transformers import AutoProcessor, MusicgenForConditionalGeneration
except ImportError:
    HAS_MUSIC = False
cd ~/songsketch
nano app.py
git status
git add app.py
git commit -m "Update app.py: auto-switch between lyrics-only (Cloud) and lyrics+music (local)"
git push origin main
cd ~/songsketch

# 1. Ouvre app.py et colle le code que je t’ai donné
nano app.py
# → colle le code
# → Ctrl+O (sauvegarder), Entrée
# → Ctrl+X (quitter)

# 2. Vérifie que git détecte bien le changement
git status

# 3. Ajoute et valide le fichier modifié
git add app.py
git commit -m "Update app.py: auto-switch between lyrics-only (Cloud) and lyrics+music (local)"

<<<<<<< HEAD
if submit:
    # Étape 1 : Génération paroles
    st.subheader("📝 Paroles générées")
    prompt = f"Écris une chanson intitulée '{titre}' sur le thème : {theme}. Format couplet/refrain."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    paroles = response.choices[0].message.content
    st.text_area("Paroles :", paroles, height=300)

    # Étape 2 : Génération musique (si possible)
    if HAS_MUSIC:
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

            sampling_rate = model.config.audio_encoder.sampling_rate
            scipy.io.wavfile.write(
                "output_song.wav",
                rate=sampling_rate,
                data=audio_values[0, 0].cpu().numpy()
            )

            st.audio("output_song.wav", format="audio/wav")
    else:
        st.info("⚠️ Mode Cloud : génération de musique désactivée (torch non disponible).")
=======
# 4. Pousse sur GitHub
git push origin main
>>>>>>> b25c72e (Update app.py: auto-switch between lyrics-only (Cloud) and lyrics+music (local))
