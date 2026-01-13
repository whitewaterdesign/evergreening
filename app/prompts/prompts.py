import os

def import_prompt(path: str) -> str:
    try:
        with open(os.path.join(os.path.dirname(__file__), path), 'r') as f:
            prompt = f.read()
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

    return prompt

EVERGREEN_EXTRACTOR = import_prompt("evergreen-extractor.md")