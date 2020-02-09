from flask import Flask, render_template
import requests

app = Flask(__name__)

def getRandomCocktail():

    r = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php')

    cocktail = r.json()

    #print(cocktail['drinks'][0]['strDrink'])

    cocktail_name = cocktail['drinks'][0]['strDrink']

    cocktail_thumb = cocktail['drinks'][0]['strDrinkThumb']

    ingredients = []

    measurements = []

    i = 1

    while i <= 15:

        cocktail_ingredient = cocktail['drinks'][0]['strIngredient' + str(i)]

        cocktail_measure = cocktail['drinks'][0]['strMeasure' + str(i)]

        if cocktail_ingredient != None:
            ingredients.append(cocktail_ingredient)


        if cocktail_measure != None:
            measurements.append(cocktail_measure)

        i += 1



    cocktail = {'name':cocktail_name, 'thumb':cocktail_thumb, 'ingredients':ingredients, 'measurements': measurements}

    return cocktail

@app.route('/')
def index(): 

    getRandomCocktail()

    data = getRandomCocktail()

    return render_template('index.html', data=data)


