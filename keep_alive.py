from flask import Flask
from threading import Thread
import random


app = Flask('')

@app.route('/')
def home():
	return f"""<h1>Grinder Selfbot Is Ready</h1><h2><u>Extras</u></h2>Dragon SMP Bot: <a href="https://dsc.lol/dragonsmp-bot">Invite</a><br>Dragon SMP Bot Website: <a href="https://dragonsmp.glique.repl.co">Go to Website</a><br><hr>Any issues then Contact me on Instagram<br><a href="https://www.instagram.com/ifreakuyt/">iFreaku on Instagram</a><br><code>-made by iFreaku</code>"""

def run():
  app.run(
		host='0.0.0.0',
		port=random.randint(2000,9000)
	)

def keep_alive():
	'''
	Creates and starts new thread that runs the function run.
	'''
	t = Thread(target=run)
	t.start()
