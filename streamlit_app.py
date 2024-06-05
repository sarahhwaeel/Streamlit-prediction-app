# -*- coding: utf-8 -*-
"""Streamlit app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_ovGcWd6eiR6pdhrvfYLAbAYFtqaRHk-
"""

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Install required packages
pip install streamlit localtunnel numpy pandas tensorflow keras matplotlib seaborn


pip install streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py

! wget -q -O - ipv4.icanhazip.com

! streamlit run app.py & npx localtunnel --port 8501
