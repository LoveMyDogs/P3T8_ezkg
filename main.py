# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
# import "packages" from "this" project
from __init__ import app  # Definitions initialization
# from api.customers_bp import customers_app_api
from api.quiz_bp import quiz_app_api
from bp_projects.projects import app_projects
from customer_questions import initCustomerQuestions # Blueprint directory import projects definition
from model.questions import *
# app.register_blueprint(customers_app_api) # register customer api routes
app.register_blueprint(quiz_app_api)
app.register_blueprint(app_projects) # register api routes

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")

@app.route('/groupwork/')  # connects default URL to index() function
def groupwork():
    return render_template("groupwork.html")

@app.route('/notebook_groupwork/')  # connects /notebook_groupwork/ URL to stub() function
def notebook_groupwork():
    return render_template("notebook_groupwork.html")

@app.route('/explanations/')  # connects /explanations/ URL to stub() function
def explanations():
    return render_template("explanations.html")

@app.route('/chain_rule/')  # connects /chain_rule/ URL to stub() function
def chain_rule():
    return render_template("chain_rule.html")

@app.route('/power_rule/')  # connects /power_rule/ URL to stub() function
def power_rule():
    return render_template("power_rule.html")

@app.route('/significant_figures/')  # connects /significant_figures/ URL to stub() function
def significant_figures():
    return render_template("significant_figures.html")

@app.before_first_request
def activate_job():
    initCustomerQuestions()
    initDBQuestions()


# this runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
