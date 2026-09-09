import os
import gradio as gr
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def analyze_chart(image, pair_tf):
    if image is None:
        return "❌ Tafadhali weka picha ya chart kwanza"
    
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        
        # Tumetumia string ya kawaida ili isivunje
        prompt = (
            f"Chambua chart hii ya {pair_tf} kwa SMC/ICT. "
            "Jibu kwa Kiswahili na utaratibu huu:\n"
            "1. BIAS: Bullish/Bearish/Neutral\n"
            "2. KEY LEVEL: Support na Resistance\n"
            "3. ENTRY: Wapi kuingia\n"
            "4. SL: Stop Loss\n"
            "5. TP1: Take Profit 1\n"
            "6. TP2: Take Profit 2\n"
            "7. SABABU: Eleza kwa kutumia OB, FVG, Liquidity\n"
            "8. HATARI: Risk %"
        )
        
        response = model.generate_content([prompt, image])
        return response.text
        
    except Exception as e:
        return f"❌ Error: {e}"

iface = gr.Interface(
    fn=analyze_chart,
    inputs=[
        gr.Image(type="pil", label="1. Weka Screenshot ya Chart"), 
        gr.Textbox(label="2. Andika Pair + Timeframe", placeholder="Mf: EURUSD 1H")
    ],
    outputs=gr.Textbox(label="3. Uchambuzi wa AI", lines=20),
    title="SMC AI Scanner",
    description="Weka screenshot ya chart + Pair TF. AI itakupa BIAS, ENTRY, SL, TP kwa kutumia SMC"
)

iface.launch(server_name="0.0.0.0", server_port=7860)
