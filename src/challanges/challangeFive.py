# ------------------------------------------------------------------------------------
#          Challenge  5
#      The wedding of the Godfather's daughter

# Stevie made some bad choices in the past,
# and getting involved with shady people was definitely one of them.
# A few days ago, two guys came into the shop,
# and reminded him that Guido the Merciful is having
#  a wedding for his only daughter.
# For the wedding, they requested the following items to be made,
#  in a manner Stevie just could not refuse:

# Francia krémes : 300
# Rákóczi túrós : 200
# Képviselőfánk : 300
# Isler : 100
# Tiramisu: 150

# Calculate how much money this sets poor Stevie back,
# who regrets asking for money all those years ago from the
#  mafia for his already bankrupt Ostrich Farm.
# Stevie wants to keep his cakery running, so he doesn’t want
#  to touch his inventory.

# For the amount, calculate the ingredients price on wholesale.
# Your function should take the whole data-set (the order)
#  and return a number (the amount of his losses in money).
# For some help, you can use the array below for the order:

# [
#    [
#        {
#          "name": "Francia krémes",
#          "amount": 300
#        },
#        {
#          "name": "Rákóczi túrós",
#          "amount": 200
#        },
#        {
#          "name": "Képviselőfánk",
#          "amount": 300
#        },
#        {
#          "name": "Isler",
#          "amount": 100
#        },
#        {
#          "name": "Tiramisu",
#          "amount": 150
#        }
#      ]
# ------------------------------------------------------------------------------------


import json
import math

with open(r".\src\data\bakery.json") as f:
    data = json.load(f)
    f.close()

with open(r".\src\data\cakesForWedding.json") as f:
    wedding = json.load(f)
    f.close()

recipes = data['recipes']
wholeSale = data['wholesalePrices']

# Creating a list of dictionaries, where each dictionary has a name and ingredients.
recipiesandingredients = []
for i in range(len(recipes)):
    recipiesandingredients.append(
        {'name': recipes[i]['name'], 'ingredients': recipes[i]['ingredients']})

# Creating a list of dictionaries, where each dictionary has a name, ingredients and sold.
recipePlusWeddingCakes = []
for i in range(len(wedding)):
    for sub in recipiesandingredients:
        if sub['name'] == wedding[i]['name']:
            recipePlusWeddingCakes.append(
                {
                  'name': sub['name'],
                  'ingredients': sub['ingredients'],
                  'sold': wedding[i]['amount']
                  })



# Calculating the amount of ingredients needed for the wedding.
for sub in recipePlusWeddingCakes:
    for i in range(len(sub['ingredients'])):
        sold = int(sub['sold'])
        ingredient = str(sub['ingredients'][i]['amount']).split(" ")
        amount = float(ingredient[0])*int(sold)

        if (ingredient[1] == 'g'):
            sub['ingredients'][i]['amount'] = str(amount/1000) + " kg"
        elif (ingredient[1] == 'ml'):
            sub['ingredients'][i]['amount'] = str(amount/1000) + " l"
        else:
            sub['ingredients'][i]['amount'] = str(amount) + " pc"


# Calculating the price of the ingredients needed for the wedding.
lista =[]
for sub in recipePlusWeddingCakes:
    for i in range(len(sub['ingredients'])):
        for j in range(len(wholeSale)):
            if sub['ingredients'][i]['name'] == wholeSale[j]['name']:
                
                updAmount = float(sub['ingredients'][i]['amount'].split(" ")[0])
                whAmount = float(wholeSale[j]['amount'].split(" ")[0])
                whPrice = int(wholeSale[j]['price'])
                onewayroad = math.ceil(updAmount/whAmount)

        lista.append({
            'totalPrice': (onewayroad * whPrice)
        })

# Summing up the total price of the ingredients needed for the wedding.
ingredientPrice = 0
for i in range(len(lista)):
    ingredientPrice += (lista[i]['totalPrice'])


with open(r".\src\answers\answerFivePython.json", 'w', encoding='utf-8') as f:
    json.dump(ingredientPrice, f, ensure_ascii=False, indent=4)
