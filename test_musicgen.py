import torchaudio
from audiocraft.models import MusicGen

def main():
    # Charger le modèle de base (small = rapide, bon pour tester)
    model = MusicGen.get_pretrained("facebook/musicgen-small")
    model.set_generation_params(duration=5)  # durée en secondes

    # Texte de test
    descriptions = ["A happy pop melody with piano and guitar"]

    print("🎶 Génération en cours...")
    wav = model.generate(descriptions)

    # Sauvegarde du résultat en .wav
    torchaudio.save("test_output.wav", wav[0].cpu(), 32000)
    print("✅ Fichier généré : test_output.wav")

if __name__ == "__main__":
    main()
from audiocraft.models import MusicGen
import torchaudio

# Charger le modèle léger (rapide, idéal pour tester)
model = MusicGen.get_pretrained("facebook/musicgen-small")

# Paramètres : durée du clip en secondes
model.set_generation_params(duration=8)

# Texte descriptif
descriptions = ["A happy pop melody with piano and claps"]

# Générer
print("⏳ Génération en cours...")
wav = model.generate(descriptions)

# Sauvegarde en WAV
torchaudio.save("test_output.wav", wav[0].cpu(), 32000)

print("✅ Fichier généré : test_output.wav")
from audiocraft.models import MusicGen
import torchaudio

# Charger un modèle léger (petit = plus rapide en CPU)
model = MusicGen.get_pretrained("facebook/musicgen-small")

# Durée de la génération (en secondes)
model.set_generation_params(duration=8)

# Description textuelle
descriptions = ["A happy pop melody with piano and claps"]

# Génération
wav = model.generate(descriptions)

# Sauvegarde en .wav
torchaudio.save("test_output.wav", wav[0].cpu(), 32000)

print("✅ Fichier généré : test_output.wav")
import torchaudio
from audiocraft.models import MusicGen

def main():
    # Charger le modèle de base
    model = MusicGen.get_pretrained("facebook/musicgen-small")
    model.set_generation_params(duration=5)  # 5 secondes d'audio

    # Texte de test
    descriptions = ["A happy pop melody with piano and guitar"]

    print("🎶 Génération en cours...")
    wav = model.generate(descriptions)

    # Sauvegarde du résultat en .wav
    torchaudio.save("test_output.wav", wav[0].cpu(), 32000)
    print("✅ Fichier généré : test_output.wav")

if __name__ == "__main__":
    main()

