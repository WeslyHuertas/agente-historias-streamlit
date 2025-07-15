import google.generativeai as genai

# Configura tu clave de API de Gemini
genai.configure(api_key="AIzaSyDfnre-8VIpcJpzV-z_fi7EESdIvMh9x0U")

# Usa el modelo correcto que sí tienes habilitado
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

def generate_story(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error generating story: {str(e)}"
