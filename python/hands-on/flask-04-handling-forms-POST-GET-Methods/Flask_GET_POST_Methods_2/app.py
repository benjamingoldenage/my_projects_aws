# Import Flask modules

from flask import Flask, render_template, request
# Create an object named app
app = Flask(__name__)

# create a function named "lcm" which calculates a least common multiple values of two numbers. 


# Create a function named `index` which uses template file named `index.html` 
# send three numbers as template variable to the app.py and assign route of no path ('/') 

@app.route('/')
def index():
    return render_template('index.html')


# calculate sum of them using "lcm" function, then sent the result to the 
# "result.hmtl" file and assign route of path ('/calc'). 
# When the user comes directly "/calc" path, "Since this is a GET request, LCM has not been calculated" string returns to them with "result.html" file


@app.route('/total', methods = ["GET", "POST"])
def total():
    if request.method == "POST":
        value1 = request.form.get ("value1")
        value2 = request.form.get ("value2")
        value3 = request.form.get ("value3")
        return render_template("number.html", total = int(value1)+int(value2)+int(value3))
    else:
        return render_template("number.html")

# Add a statement to run the Flask application which can be debugged.

if __name__ =='__main__':
    # app.run(debug = True)
    app.run(host='0.0.0.0', port=80)