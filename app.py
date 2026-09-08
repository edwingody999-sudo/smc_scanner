import gradio as gr
import google.generativeai as genai
from PIL import Image
import io

# Weka API KEY yako hapa
genai.configure(api_key="GEMINI_API_KEY")

def analyze_chart(image, pair_tf):
    if image is None:
        return "Tafadhali weka picha ya chart kwanza"
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    Wewe ni mchambuzi wa SMC wa kitaalamu. Chambua chart hii ya {pair_tf}.
    Toa jibu kwa mtindo huu:
    **BIAS**: BULLISH / BEARISH / NEUTRAL
    **ENTRY**: 
    **SL**: 
    **TP1**: 
    **TP2**: 
    **SABABU**: Eleza kwa ufupi kwa kutumia SMC - Liquidity, BOS, FVG, Order Block
    """
    
    response = model.generate_content([prompt, image])
    return response.text

iface = gr.Interface(
    fn=analyze_chart,
    inputs=[
        gr.Image(type="pil", label="Weka Picha ya Chart"),
        gr.Textbox(label="Andika Pair + Timeframe", placeholder="Mfano: EURUSD 1H")
    ],
    outputs=gr.Textbox(label="AI Analysis", lines=10),
    title="SMC Chart Scanner",
    description="Upload picha ya chart upate BIAS, ENTRY, SL, TP kwa kutumia SMC"
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)
