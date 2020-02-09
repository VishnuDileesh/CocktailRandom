from flask import Flask
import requests

app = Flask(__name__)

def getRandomCocktail():

    r = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php')

    cocktail = r.json()

    #print(cocktail['drinks'][0]['strDrink'])

    cocktail_name = cocktail['drinks'][0]['strDrink']

    cocktail_thumb = cocktail['drinks'][0]['strDrinkThumb']

    print(cocktail_thumb)

@app.route('/')
def index(): 

    getRandomCocktail()

    return "Hello World"


