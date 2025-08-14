#Create Virtual Environment & Install requests, pandas
# Step 1: Create a virtual environment named venv
python -m venv venv

# Step 2: Activate the virtual environment

# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Step 3: Install required packages
pip install requests pandas

#Run pip list Inside and Outside the Virtual Environment
pip list
Expected output
Package    Version
---------- -------
pip        24.x.x
pandas     2.x.x
requests   2.x.x
setuptools ...

#Outside Virtual Environment
deactivate
#then run again
pip list

#Description
Environment	Packages Shown	Notes
Inside venv	requests, pandas	Only packages installed in venv
Outside venv	System/global packages	Doesn't include requests, pandas (if not globally installed)