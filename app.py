import os
import gradio as gr
import google.generativeai as genai
from PIL import Image
import io

genai.configure(api_key=os.environ["GEMINI_API_KEY"]) # <-- HII NDIO SAHIHI

def analyze_chart(image, pair_tf):    description="Upload picha ya chart upate BIAS, ENTRY, SL, TP kwa kutumia SMC"
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)
