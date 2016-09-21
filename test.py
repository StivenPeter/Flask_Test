from flask import Flask

stiven = Flask(__name__)

@app.route("/")      
def  WithAnI():
    return "I am Stiven With An I"

@app.route("/about")
def aboutMe():
    return "I am THE Stiven Peter."

@app.route("/philosophy")
def phil():
    return "Go here if you want to be corrupted"

if __name__ == '__main__':
    stiven.run()