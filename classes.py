import json
from typing import Optional


class RepositoryCandidates:
    '''Класс считывает и берет с базы данные (все, по id, по skill'у)'''
    def __init__(self, file_name: str):
        self.candidates_file = file_name

    def load_candidates(self) -> list[dict]:
        with open(self.candidates_file, encoding='utf-8') as file:
            return json.load(file)

    def get_all(self) -> list[dict]:
        # candidates = self.load_candidates()
        #
        # to_return_list = []
        # for candidate in candidates:
        #     to_return_list.append(f"{candidate['name']}\n" \
        #                           f"{candidate['id']}\n" \
        #                           f"{candidate['skills']}\n\n")
        # to_return_str = ''.join(to_return_list)
        # return to_return_str
        return self.load_candidates()

    def get_by_id(self, id: int) -> Optional[dict]:
        candidates = self.load_candidates()

        try:
            selected_candidate = candidates[id-1]
        except IndexError:
            return None

        return selected_candidate
        #
        # to_return_list = []
        # to_return_list.append(f'<img src={selected_candidate["picture"]}>\n\n')
        #
        # to_return_list.append(f"{selected_candidate['name']}\n" \
        #                  f"{selected_candidate['id']}\n" \
        #                  f"{selected_candidate['skills']}")
        # to_return_str = ''.join(to_return_list)
        #
        # return to_return_str

    def get_by_skill(self, skill) -> Optional[list[dict]]:
        candidates = self.load_candidates()
        skillful_candidates = []
        for candidate in candidates:
            if skill in map(lambda skill: skill.lower(), candidate['skills'].split(', ')):
                skillful_candidates.append(candidate)

        if skillful_candidates:
            return skillful_candidates
        return None

class AppTemplateRenderer:
    def render_index(candidates_list: list[dict]) -> str:
        to_return_list = []
        for candidate in candidates_list:
            to_return_list.append(f"{candidate['name']}\n" \
                                  f"{candidate['id']}\n" \
                                  f"{candidate['skills']}\n\n")
        to_return_str = Preformater.pre(''.join(to_return_list))
        return to_return_str

    def render_by_id(candidate: [dict]) -> str:
        to_return_list = []
        to_return_list.append(f'<img src={candidate["picture"]}>\n\n')

        to_return_list.append(f"{candidate['name']}\n" \
                         f"{candidate['id']}\n" \
                         f"{candidate['skills']}")
        to_return_str = Preformater.pre(''.join(to_return_list))

        return to_return_str

    def render_by_skill(candidates_list: list[dict]) -> str:
        to_return_list = []
        for candidate in candidates_list:
            to_return_list.append(f"{candidate['name']}\n" \
                                  f"{candidate['id']}\n" \
                                  f"{candidate['skills']}\n\n")
        to_return_str = Preformater.pre(''.join(to_return_list))
        return to_return_str

class Preformater:
    @classmethod
    def pre(cls, data: str) -> str:
        return f'<pre>{data}</pre>'