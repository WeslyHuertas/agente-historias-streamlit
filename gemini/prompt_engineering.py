def build_prompt(params: dict) -> str:
    return (
        f"You are a talented storyteller. Write a {params['length']} {params['genre']} story "
        f"with a {params['tone']} tone.\n\n"
        f"Characters: {params['characters']}\n"
        f"Setting: {params['setting']}\n"
        f"Plot: {params['plot']}\n\n"
        f"The story should have a strong beginning, rising action, conflict, and resolution. "
        f"It should be emotionally engaging and vividly written."
    )
