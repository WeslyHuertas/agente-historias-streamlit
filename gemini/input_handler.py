def parse_user_input(text: str) -> dict:
    parts = text.split(",")
    if len(parts) < 5:
        return {}
    return {
        "characters": parts[0].strip(),
        "genre": parts[1].strip().lower(),
        "setting": parts[2].strip(),
        "plot": parts[3].strip(),
        "tone": parts[4].strip(),
        "length": "medium"
    }

def validate_input(params: dict) -> bool:
    required = ["characters", "genre", "setting", "plot"]
    for key in required:
        if not params.get(key):
            return False
    return True
