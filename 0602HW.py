from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def intro():
	return "2019117662 컴퓨터학부 글로벌소프트웨어학과 박수환"

@app.route("/me/")
def intro_me():
	photo = ["경북대로고.jpeg", "whales.jpeg", "hamburger.jpeg"]
	pickme = random.choice(photo)
	return render_template('index.html', intro_img=pickme)

if __name__ == "__main__":
	app.run(debug=True)
