from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1=22, number2=22)

@app.route('/mult')
def sum():
    num1 , num2 = 47, 444
    return render_template('body.html', value1=num1, value2=num2, multiplication=num1*num2)


if __name__=="__main__":
    app.run(host='0.0.0.0', port=80)
    # app.run(debug=True)