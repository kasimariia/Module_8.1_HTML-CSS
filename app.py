from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def greeting():
    return render_template("my_page.html")

@app.route('/contact', methods=['GET'])
def kontakty():
    return render_template("contacts.html")

if __name__ == '__main__':
    app.run()