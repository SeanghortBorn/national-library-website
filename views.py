from flask import Blueprint, render_template, request, jsonify, redirect, url_for


views = Blueprint(__name__, "views")

# Static display
@views.route("/")
def home():
    return render_template("home.html")


@views.route("/profile")
def profile():
    return render_template("profile.html")

@views.route("/checker")
def checker():
    return render_template("checker.html")

# Return data as json
@views.route("/json")
def get_json():
    return jsonify({'name': 'tim', 'coolness': '109'})

# Display data as json
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

# Return to any page
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))