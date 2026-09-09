import os
import gradio as gr
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def analyze_chart(image, pair_tf):
    if image is None:
        return "Tafadhali weka picha ya chart kwanza"
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    Wewe ni mchambuzi wa SMC/ICT wa kitaalumu. Chambua chart hii ya {pair_tf}.
    Toa jibu kwa mtindo huu:
    **BIAS**: BULLISH / BEARISH / NEUTRAL
    **ENTRY**: 
    **SL**: 
    **TP1**: 
    **TP2**: 
    **SABABU**: Eleza kwa ufupi kwa kutumia SMC kama OB, FVG, Liquidity
    """
    
    response = model.generate_content([prompt, image])
    return response.text

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
