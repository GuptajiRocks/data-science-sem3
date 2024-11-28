from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def main_page():
    return render_template("index.html")

@app.route('/marks', methods=['POST'])
def marks():
    selected_subjects = request.form.getlist('subjects')  # List of selected subjects
    subject_values = {}
    for subject in selected_subjects:
        value = request.form.get(f"{subject}_value")
        subject_values[subject] = value

    return jsonify({"selected_subjects_with_values": subject_values})

if __name__ == "__main__":
    app.run(debug=True)
