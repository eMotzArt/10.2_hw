import json


class Candidates:
    def __init__(self, file_name: str):
        self.candidates_file = file_name

    def load_candidates(self) -> list[dict]:
        with open(self.candidates_file, encoding='utf-8') as file:
            return json.load(file)

    def show_all(self) -> list[dict]:
        candidates = self.load_candidates()

        to_return_list = []
        for candidate in candidates:
            to_return_list.append(f"{candidate['name']}\n" \
                                  f"{candidate['id']}\n" \
                                  f"{candidate['skills']}\n\n")
        to_return_str = ''.join(to_return_list)
        return to_return_str

    def show_by_id(self, id) -> str | None:
        candidates = self.load_candidates()

        try:
            selected_candidate = candidates[id-1]
        except IndexError:
            return None

        to_return_list = []
        to_return_list.append(f'<img src={selected_candidate["picture"]}>\n\n')

        to_return_list.append(f"{selected_candidate['name']}\n" \
                         f"{selected_candidate['id']}\n" \
                         f"{selected_candidate['skills']}")
        to_return_str = ''.join(to_return_list)

        return to_return_str

    def show_by_skill(self, skill) -> str | None:
        candidates = self.load_candidates()
        to_return_list = []
        for candidate in candidates:

            if skill not in map(lambda skill: skill.lower(), candidate['skills'].split(', ')):
                continue

            to_return_list.append(f"{candidate['name']}\n" \
                                  f"{candidate['id']}\n" \
                                  f"{candidate['skills']}\n\n")
        to_return_str = ''.join(to_return_list)
        if to_return_str:
            return to_return_str
        return None

class Preformater:
    @classmethod
    def pre(cls, data: str) -> str:
        return f'<pre>{data}</pre>'