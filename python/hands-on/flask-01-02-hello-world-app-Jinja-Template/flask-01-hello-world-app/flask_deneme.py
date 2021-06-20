from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello ():
    return "Hello world"

# Url.ye assign etmek gerekiyor.  dekorator 

@app.route("/second")
def second ():
    return "bir gün herkes fb.li olacak"

@app.route("/third")
def third ():
    return "her yer ankara"

@app.route("/forth/<string:id>")
def forth (id):
    return f"id number of this page is{id}"

if  __name__ == "__main__" :
    app.run(debug=True)

# flask modülü ana kodları. debug true modda çalıstır.