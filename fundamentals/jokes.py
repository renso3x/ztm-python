# setup virtualenv env/

# fire the env => source venv/bin/activate

# pip install module


import pyjokes

joke =  pyjokes.get_joke('en', 'neutral')

print(joke)