# # -*- coding: utf-8 -*-
# """
#     flask.__main__
#     ~~~~~~~~~~~~~~

#     Alias for flask.run for the command line.

#     :copyright: 2010 Pallets
#     :license: BSD-3-Clause
# """

# if __name__ == "__main__":
#     from .cli import main

#     main(as_module=True)
from flask import (Flask, render_template)

app = Flask("__main__")

@app.route("/")
def my_index():
    return render_template("index.html", flask_token="Hello   world")

app.run(debug=True)