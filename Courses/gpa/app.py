from flask import Flask, render_template, request

app = Flask(__name__)

# Sample subject data (replace with your actual data)
subjects = [
    {'name': 'Math', 'credit': 3},
    {'name': 'Science', 'credit': 4},
    {'name': 'English', 'credit': 3},
    # ... more subjects
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_subjects = request.form.getlist('subjects')
        grades = request.form.getlist('grades')

        # Calculate GPA (adjust the formula as needed)
        total_credits = 0
        total_grade_points = 0
        for subject, grade in zip(selected_subjects, grades):
            credit = next(s['credit'] for s in subjects if s['name'] == subject)
            total_credits += credit
            total_grade_points += credit * float(grade)

        gpa = total_grade_points / total_credits

        return render_template('result.html', gpa=gpa)

    return render_template('index.html', subjects=subjects)

if __name__ == '__main__':
    app.run(debug=True)