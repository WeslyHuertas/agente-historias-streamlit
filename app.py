import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import textstat

MODEL_NAME = "tiiuae/falcon-7b-instruct"

@st.cache_resource(show_spinner=False)
def cargar_modelo():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype="auto",
        device_map="auto"
    )
    return pipeline("text-generation", model=model, tokenizer=tokenizer)

generator = cargar_modelo()

st.title("🤖 Chat de Historias Creativas")

# Session state para mantener la conversación
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hola 👋 Soy un agente creativo. ¡Cuéntame qué historia quieres que invente! Dame personajes, género, escenario, conflicto, tono, longitud o estilo si quieres."}
    ]

# Mostrar mensajes anteriores
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrada del usuario
user_input = st.chat_input("Escribe tu solicitud de historia aquí...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Estoy creando una historia para ti..."):

            # Construye el prompt
            prompt = (
                f"A partir de la siguiente descripción, escribe una historia creativa:\n"
                f"{user_input}\n"
                f"Comienza la historia a continuación:\n\n"
                f"Historia:"
            )

            # Generar historia
            salida = generator(prompt, max_new_tokens=800, do_sample=True, temperature=0.8)
            historia = salida[0]["generated_text"]

            # Mostrar historia
            st.markdown(historia)

            # Análisis de legibilidad
            score = textstat.flesch_reading_ease(historia)
            nivel = textstat.text_standard(historia, float_output=True)
            st.markdown("### 📊 Análisis de legibilidad")
            st.w
