import os
import gradio as gr
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def analyze_chart(image, pair_tf):
    if image is None:
        return "Tafadhali weka picha ya chart kwanza"
    
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
        prompt = f"""
        Wewe ni mchambuzi wa SMC/ICT. Chambua chart hii ya {pair_tf}.
        Jibu kwa Kiswahili kwa format hii:
        **BIAS**: BULLISH/BEARISH/NEUTRAL
        **ENTRY**: 
        **SL**: 
        **TP1**: 
        **TP2**: 
        **SABU**: Tumia OB, FVG, Liquidity
        """
        response = model.generate_content([prompt, image])
        return response.text
    except Exception as e:
        return f"Error: {e}"

iface = gr.Interface(
    fn=analyze_chart,
    inputs=[
        gr.Image(type="pil", label="Weka Screenshot ya Chart"), 
        gr.Textbox(label="Pair + Timeframe mf: EURUSD 1H")
    ],
    outputs=gr.Textbox(label="Uchambuzi wa AI"),
    title="SMC AI Scanner"
)
iface.launch(server_name="0.0.0.0", server_port=7860)
