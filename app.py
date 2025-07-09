from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        expression = request.form['expression']
        try:
            # Evaluate the mathematical expression safely
            result = eval(expression)
        except Exception:
            result = 'Error'
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
