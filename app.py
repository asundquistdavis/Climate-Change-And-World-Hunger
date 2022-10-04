from flask import Flask, render_template, request

from data import get_amounts as ga
from data import get_temps as gt

app = Flask(__name__)

# index route which serves dashboard for websites
@app.route('/')
def index():
    return render_template('index.html')

# data route which serves data from database
@app.route('/api/v1.0/temps')
def temps():

    # call get_temps method
    temps = gt()

    # return data
    return temps

@app.route('/api/v1.0/foods')
def foods():

    # call get_foods method
    foods = gf()

    # return data
    return foods

if __name__ == '__main__':
    app.run(debug=True)

