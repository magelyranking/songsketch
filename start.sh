#!/bin/bash

# Charger pyenv dans le script
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Aller dans ton projet
cd ~/songsketch || exit 1

# Activer ton environnement virtuel
pyenv activate songsketch-env || exit 1

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application Streamlit
streamlit run app.py
#!/bin/bash
cd ~/songsketch
eval "$(pyenv init -)"   # charge pyenv dans le script
eval "$(pyenv virtualenv-init -)"
pyenv shell songsketch-env
pip install -r requirements.txt
streamlit run app.py
#!/bin/bash
cd ~/songsketch
pyenv activate songsketch-env
pip install -r requirements.txt
streamlit run app.py

