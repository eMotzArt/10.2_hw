from flask import Flask
from utils import show_all, show_by_id, show_by_skill

app = Flask(__name__)

@app.route('/')
def page_index():
    return show_all()

@app.route('/candidates/<int:cand_num>')
def page_per_num(cand_num):
   return show_by_id(cand_num)

@app.route('/skills/<skill>')
def page_per_skills(skill: str):
    return show_by_skill(skill)


if __name__ == "__main__":
    app.run(host='127.0.0.2', port=80)
