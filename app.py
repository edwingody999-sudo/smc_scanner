import os
import gradio as gr
import google.generativeai as genai
from PIL import Image

# Weka API Key kutoka Environment Variables
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def analyze_chart(image, pair_tf):
    if image is None:
        return "❌ Tafadhali weka picha ya chart kwanza"
    
    try:
        # MODEL INAYOFANYA KAZI KWA RENDER
        model = genai.GenerativeModel("gemini-2.0-flash")
        
        prompt = f"""
        Wewe ni mchambuzi wa kitaalamu wa SMC/ICT Trading. 
        Chambua chart hii ya {pair_tf}.
        
        Jibu kwa Kiswahili safi na kwa utaratibu huu:
        
        **1. BIAS**: Bullish au Bearish au Neutral
        **2. KEY LEVEL**: Toa Support na Resistance muhimu
        **3. ENTRY**: Wapi kuingia trade
        **4. SL**: Stop Loss wapi
        **5. TP1**: Take Profit ya kwanza
        **6. TP2**: Take Profit ya pili  
        **7. SABABU**: Eleza kwa nini umetoa hii bias kwa kutumia SMC - OB
