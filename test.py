from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

MODEL_NAME = "tiiuae/falcon-rw-1b"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    torch_dtype=torch.float16
)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def pedir_entrada(nombre, ejemplo=""):
    valor = ""
    while not valor.strip():
        valor = input(f"{nombre} ({ejemplo}): ").strip()
    return valor

def construir_prompt(datos):
    prompt = (
        f"Escribe una historia original en español con las siguientes características:\n\n"
        f"📚 Género: {datos['género']}\n"
        f"🎭 Tono: {datos['tono']}\n"
        f"📍 Escenario: {datos['escenario']}\n"
        f"👥 Personajes: {datos['personajes']}\n"
        f"🧩 Elementos de trama: {datos['trama']}\n"
        f"📝 Longitud: {datos['longitud']}\n\n"
        f"Comienza la historia a continuación:\n\nHistoria:"
    )
    return prompt

def main():
    print("🧙 Generador de historias creativas\nPor favor, responde los siguientes campos:")

    campos = {
        "personajes": "Ej: Ana (exploradora valiente), Tomás (androide, tímido, leal)",
        "escenario": "Ej: Año 3045, planeta Marte terraformado, atmósfera opresiva",
        "género": "fantasía, misterio, romance, terror, ciencia ficción, comedia, aventura",
        "trama": "Ej: Conflicto interno, obstáculos físicos, resolución trágica",
        "tono": "humorístico, oscuro, caprichoso, dramático, satírico",
        "longitud": "Corta (300-400), mediana (400-600), larga (600-800)"
    }

    datos = {}
    for campo, ejemplo in campos.items():
        datos[campo] = pedir_entrada(f"{campo.capitalize()}", ejemplo)

    prompt = construir_prompt(datos)

    print("\n🛠️ Generando historia...\n")
    salida = generator(prompt, max_new_tokens=800, do_sample=True, top_p=0.9, temperature=0.8)
    historia = salida[0]["generated_text"]
    print("📖 Historia generada:\n")
    print(historia)

if __name__ == "__main__":
    main()

