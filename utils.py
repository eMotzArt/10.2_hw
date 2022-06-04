import json

def load_candidates():
    with open('candidates.json', encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates

