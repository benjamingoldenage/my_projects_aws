# Import Flask modules
from flask import Flask, render_template, redirect, url_for
# Create an object named app 
app = Flask (__name__)


# Create a function named list10 which creates a list counting from 1 to 10 within `list10.html` 
# and assign to the route of ('/list10')
@app.route('/list10')
def list10():
    return render_template('list10.html')


    
# run this app in debug mode on your local. Do not forget to change debug mode to publish mode before you push to the Github repo

if __name__ =='__main__':
    # app.run(debug = True)
    app.run(host='0.0.0.0', port=80)