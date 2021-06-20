from flask import Flash

app = Flash(__name__)


@app.route('/')
def hello():
    return 'hello world'
