# AUAT - Uat generation
Description.......

## Requirements
To install the application you need python 3.8+ and OpenAI API_KEY.
To generated the openAI key:
- Click your first name’s initial from the top-right corner of the OpenAI dashboard. Click the “View API Keys” link.
- In the submenu click the “+Create new Secret Key” button.
- You will see your new API Key. Copy and place it in a safe place.

## Quick Start

```
# install 
pip install poetry

# create a local directory
mkdir UAT
cd UAT

# clone the repo
git clone https://github.com/GabrieleVassallo/AutomaticUAT

# install the application
poetry shell
poetry install

# export OPENAI_KEY=<past your OpenAI key here>

# Run the application
cd UAT
poetry run streamlit run ./uat/uatApp.py

```