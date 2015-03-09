#!/usr/bin/env python
import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs
from flask.ext.frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXENSION= '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)



if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
	freezer.freeze()
    else:
        app.run(host='127.0.0.1', port=5001, debug=True)
