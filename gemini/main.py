from input_handler import parse_user_input, validate_input
from prompt_engineering import build_prompt
from story_generator import generate_story
from pdf_writer import save_story_to_pdf

def main():
    print("🎨 Welcome to the Creative Story Agent!\n")
    user_input = input("Describe your story (characters, genre, setting, plot, tone):\n> ")

    params = parse_user_input(user_input)

    if not validate_input(params):
        print("⚠️ Incomplete input. Please include characters, genre, setting, plot, and tone.")
        return

    prompt = build_prompt(params)
    print("\n📜 Generating your story...\n")
    story = generate_story(prompt)

    if "❌" in story:
        print(story)  # Show error
        return

    print("✅ Story successfully generated!")
    print("📄 Saving to PDF...")

    title = f"{params['genre'].capitalize()} Story: {params['characters'].split()[0]}"
    filename = f"{params['characters'].split()[0].lower()}_story.pdf"
    save_story_to_pdf(title, story, filename)

    print(f"📂 Saved as: {filename}")

if __name__ == "__main__":
    main()
