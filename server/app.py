from flask import Flask
app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

@app.route('/')
def index():
    return 'Welcome to Flatiron Cars'

@app.route('/<string:car_name>')
def car(car_name):
    if car_name in existing_models:
        return f'Flatiron {car_name} is in our fleet!'
    else:
        return f'No models called {car_name} exists in our catalog'

if __name__ == '__main__':
    app.run(port=5555, debug=True)


