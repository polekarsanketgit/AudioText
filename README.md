How to install?

Step1: pip install streamlit
Step2: streamlit hello

*** In case it's not working, follow the next step 

Step1: cd myproject
Step2: python -m venv .venv

(This will create a folder named ".venv" will appear in your project. This directory is where your virtual environment and its dependencies are installed.)

Activate your environment
# Windows command prompt
Step3: .venv\Scripts\activate.bat

Step4: pip install streamlit
Step5: streamlit hello

Or

*** if it not works use the long-form command:

Step5: python -m streamlit hello

Example: Code:

File Name: demo.py

import streamlit as st
st.write("Hello world")
*** Any time you want to use your new environment, you first need to go to your project folder (where the .venv directory lives) and run the command to activate it:

# Windows command prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

Step6: streamlit run demo.py

Or

Step6: python -m streamlit run demo.py
