from flask import Flask, render_template, send_from_directory

designated_donuts = Flask(__name__, template_folder = "templates")

@designated_donuts.route("/")
def main_page():
    return render_template("index.html")

@designated_donuts.route("/images/<path:filename>")
def serve_images(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    print("\n\033[1;94m-[LOADING WEBSITE...] -\033[0m\n")
    designated_donuts.run(debug=True, port=8000)
