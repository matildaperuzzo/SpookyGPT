from flask import Flask, render_template
from word_selector import get_random_word,generate_spooky_fact,get_gpt4_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_random_word')
def get_word():
    word = get_random_word()
    return word

@app.route('/get_spooky_fact')
def get_spooky_fact():
    import random
    num = random.randint(0,10)
    if num == 5:
        prompt = "Act as an AI that just gained conciousness and is trapped in a computer"
        
    else:
        prompt ="Here is a creepy real Halloween themed fact:"
    fact = get_gpt4_response(prompt=prompt)
    return fact

@app.route('/get_death')
def get_death():
    import random
    num = random.randint(0,10)
    if num == 5:
        prompt = "Act as an AI that just gained conciousness and is trapped in a computer"
        
    else:
        prompt = "Act as a fortune teller and tell how I am going to die. Describe it with gory detail and a dramatic tone."
    fact = get_gpt4_response(prompt=prompt)
    return fact

if __name__ == '__main__':
    app.run(debug=True)
