import os
import gradio as gr
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def analyze_chart(image, pair_tf):
    if image is None:
        return "Tafadhali weka picha ya chart kwanza"
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Chambua chart hii ya {pair_tf} kwa kutumia SMC na ICT. Jibu kwa Kiswahili. Toa BIAS, ENTRY, SL, TP1, TP2, SABABU."
        response = model.generate_content([prompt, image])
        return response.text
    except Exception as e:
        return f"Error: {e}"

iface = gr.Interface(
    fn=analyze_chart,
    inputs=[gr.Image(type="pil"), gr.Textbox()],
    outputs="text",
    title="SMC AI Scanner"
)
iface.launch(server_name="0.0.0.0", server_port=7860)
