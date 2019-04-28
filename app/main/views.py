from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_quotes

# views
@main.route("/")
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # random_quote = get_quotes()
    
    title = "Home - Welcome to the best Blog page"
    
    return render_template("index.html", title = title)