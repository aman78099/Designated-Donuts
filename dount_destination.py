from flask import Flask, render_template

donut_destination = Flask(__name__, template_folder = "templates")

@donut_destination.route("/")
def main_page():
    return render_template("index.html")


if __name__ == "__main__":
    print("\n\033[1;94m-[LOADING WEBSITE...] -\033[0m\n")
    donut_destination.run(debug=True, port=5000)


