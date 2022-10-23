import utils
from flask import Flask

app = Flask(__name__)


@app.route('/')
def page_index():
    return utils.get_all()


@app.route('/candidates/<pk>')
def page_candidates(pk):
    return utils.get_by_pk(pk)


@app.route('/skills/<skill>')
def page_skills(skill):
    return utils.get_by_skill(skill)


if __name__ == "__main__":
    app.run()
