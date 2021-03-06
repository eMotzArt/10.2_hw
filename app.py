from flask import Flask, abort
from classes import RepositoryCandidates, Preformater, AppTemplateRenderer as Renderer

app = Flask(__name__)

CANDIDATES_FILE: str = 'candidates.json'

@app.route('/')
def page_index():
    if candidates := RepositoryCandidates(CANDIDATES_FILE).get_all():
        return Renderer.render_index(candidates)
    else:
        abort(404)


@app.route('/candidates/<int:candidate_number>')
def page_per_num(candidate_number: int):

    if candidate := RepositoryCandidates(CANDIDATES_FILE).get_by_id(candidate_number):
        return Renderer.render_by_id(candidate)
    else:
        abort(404)

@app.route('/skills/<skill>')
def page_per_skills(skill: str):
    if candidates := RepositoryCandidates(CANDIDATES_FILE).get_by_skill(skill):
        return Renderer.render_by_skill(candidates)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(host='127.0.0.2', port=80)

