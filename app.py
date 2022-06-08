from flask import Flask, abort
from classes import RepositoryCandidates, Preformater

app = Flask(__name__)

CANDIDATES_FILE: str = 'candidates.json'

@app.route('/')
def page_index():
    result = RepositoryCandidates(CANDIDATES_FILE).get_all()
    if result:
        return Preformater.pre(result)
    else:
        abort(404)


@app.route('/candidates/<int:cand_num>')
def page_per_num(cand_num):
    result = RepositoryCandidates(CANDIDATES_FILE).get_by_id(cand_num)
    if result:
        return Preformater.pre(result)
    else:
        abort(404)

@app.route('/skills/<skill>')
def page_per_skills(skill: str):
    result = RepositoryCandidates(CANDIDATES_FILE).get_by_skill(skill)
    if result:
        return Preformater.pre(result)
    else:
        abort(404)
if __name__=='__name__':
    app.run(host='127.0.0.2', port=80)
