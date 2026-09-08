import gradio as gr
import google.generativeai as genai
import os

API_KEY = os.getenv("GEMINI_API_KEY") 
genai.configure(api_key=API_KEY)

def analyze_chart(image):
    if image is None:
        return "Tafadhali upload picha ya chart kwanza"
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = """Wewe ni mtaalamu wa SMC na ICT Trading. Chambua hii chart.
Toa jibu kwa Kiswahili:
**SIGNAL**: BUY / SELL / WAIT
**REASON**: Point 3. Taja Order Block, FVG, Liquidity
**ENTRY**: Bei
**SL**: Stop Loss  
**TP**: Take Profit 1, 2"""
    
    response = model.generate_content([prompt, image])
    return response.text

iface = gr.Interface(
    fn=analyze_chart,
    inputs=gr.Image(type="pil", label="Weka Picha ya Chart"),
    outputs=gr.Textbox(label="AI Analysis", lines=15),
    title="SMC Scanner AI"
)
iface.launch(server_name="0.0.0.0", server_port=7860)
