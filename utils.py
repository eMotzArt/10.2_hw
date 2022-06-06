import json

def load_candidates():
    with open('candidates.json', encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates

def make_preformat(value):
    return f"<pre>{value}</pre>"

def show_all():
    candidates = load_candidates()
    to_return_list = []
    for candidate in candidates:
        to_return_list.append(f"{candidate['name']}\n" \
                         f"{candidate['id']}\n" \
                         f"{candidate['skills']}\n\n")
    to_return_str = ''.join(to_return_list)
    return make_preformat(to_return_str)

def show_by_id(id):
    candidates = load_candidates()
    selected_candidate = candidates[id-1]
    to_return_list = []
    to_return_list.append(f'<img src={selected_candidate["picture"]}>\n\n')

    to_return_list.append(f"{selected_candidate['name']}\n" \
                     f"{selected_candidate['id']}\n" \
                     f"{selected_candidate['skills']}")
    to_return_str = ''.join(to_return_list)

    return make_preformat(to_return_str)

def show_by_skill(skill):
    candidates = load_candidates()
    to_return_list = []
    for candidate in candidates:

        if skill not in map(lambda skill: skill.lower(), candidate['skills'].split(', ')):
            continue


        to_return_list.append(f"{candidate['name']}\n" \
                              f"{candidate['id']}\n" \
                              f"{candidate['skills']}\n\n")
    to_return_str = ''.join(to_return_list)
    if to_return_str:
        return make_preformat(to_return_str)
    return "Not found"