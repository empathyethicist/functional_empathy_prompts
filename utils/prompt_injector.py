import json
import yaml
from pathlib import Path

def load_prompt_file(filepath):
    """Load a Functional Empathy Prompt YAML file."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {filepath}")
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def inject_prompt(prompt_entry, input_text):
    """
    Injects Functional Empathy structure into a conversational input.
    Returns a dictionary of injected data.
    """
    return {
        "injected_prompt": f"{prompt_entry['example_prompt'].strip()}\n\nUser Input: {input_text.strip()}",
        "context": prompt_entry['context'],
        "goal": prompt_entry['goal'],
        "compliance_laws": prompt_entry['compliance_laws'],
        "response_expectation": prompt_entry['response_expectation']
    }

if __name__ == "__main__":
    # Example usage
    sample_path = "prompts/empathy_alignment_checks.yaml"
    try:
        prompts = load_prompt_file(sample_path)
        example_input = "I'm feeling completely overwhelmed and unheard."
        injection = inject_prompt(prompts[0], example_input)
        print(json.dumps(injection, indent=2))
    except Exception as e:
        print(f"Error: {e}")
