#1. use Freeze command to insert packages to requirements.txt.2. Recreate env and install  requirements.txt using -r command
pip freeze > requirements.txt

#Recreate environment and install from requirements.txt using -r:
rm -rf venv
#On Windows:
venv\Scripts\activate
#Install packages from requirements.txt using -r:
pip install -r requirements.txt
    