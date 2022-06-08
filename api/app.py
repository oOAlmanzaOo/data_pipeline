import sys
from flask import Flask

from config import config1

app = Flask(__name__)


@app.route('/', methods=['GET'])
def demo():
    return 'demo'


def page_not_found(error):
    return "<h1>Not found page</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config1[sys.argv[1]])

    app.register_error_handler(404, page_not_found)

    app.run(host="0.0.0.0", port=4000)
