from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates/index.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    grade = float(request.form['txtgrade'])
    if grade >= 70:
        answer = "Aprobado"
    else:
        answer = "Aprendizaje inicial"
    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)