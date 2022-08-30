# ------------------------------------------------------------------------------------
#          Challenge  6
#        Next two week's sales
#
# Consistency and plannability are key!
#
# Based on this mantra, Stevie wants to know the ingredients he should order
#  to last him two weeks combined with his inventory.
# He already knows last week's sales, and he assumes the next two weeks will
#  be the same.
# To be on the safe side, he'd like to have a 10% surplus of everything on top
#  of the amount which would last two weeks.
#
# Calculate the amount of ingredients based on past sales
# for the next two weeks,
# and add 10% on top of it.
# Your function should take the whole data-set, and return a shopping list for
#  Stevie to take to his wholesaler,
# based on the example below. Remember, the wholesaler needs the amounts in
#  kilograms and liters.
#
# ------------------------------------------------------------------------------------

import json
import math


with open(r".\src\data\bakery.json") as f:
    data = json.load(f)
    f.close()

recipes = data['recipes']
inventory = data['inventory']
wholeSale = data['wholesalePrices']
lastWeekSales = data['salesOfLastWeek']

# Creating a list of dictionaries with the name and ingredients of each recipe.
recipiesandingredients = []
for i in range(len(recipes)):
    recipiesandingredients.append(
        {'name': recipes[i]['name'], 'ingredients': recipes[i]['ingredients']})

# Creating a list of lists with
# the name and amount of each cake sold last week.
lastWeeksalesName = []
for i in range(len(lastWeekSales)):
    lastWeeksalesName.append(
        [lastWeekSales[i]['name'], lastWeekSales[i]['amount']])

# This is creating a list of dictionaries with the name,
#  ingredients and amount sold of each cake.
soldCakes = []
for i in range(len(lastWeeksalesName)):
    for sub in recipiesandingredients:
        if sub['name'] == lastWeeksalesName[i][0]:
            soldCakes.append(
                {
                  'name': sub['name'],
                  'ingredients': sub['ingredients'],
                  'sold': lastWeeksalesName[i][1]
                  })


# This is converting the amount of ingredients to the amount
#  needed for the amount of cakes sold.
for sub in soldCakes:
    sold = sub['sold']
    for i in range(len(sub['ingredients'])):
        ingredient = str(sub['ingredients'][i]['amount']).split(" ")
        amount = float(ingredient[0])*(float(sold)+float(sold))

        if ingredient[1] == 'g':
            sub['ingredients'][i]['amount'] = str(amount/1000) + " kg"
        elif ingredient[1] == 'ml':
            sub['ingredients'][i]['amount'] = str(amount/1000) + " l"
        else:
            sub['ingredients'][i]['amount'] = str(amount) + " pc"


# Creating a list of lists with the ingredients of each cake.
soldCakesSum = []
for sub in soldCakes:
    soldCakesSum.append(sub['ingredients'])
# Flattening the list of lists.
soldCakesSumFlat = [element for sublist in soldCakesSum for element in sublist]

# This is creating a list of all the ingredients
#  used in the cakes sold last week.
ingredientTypeUniq = []
for i in range(len(soldCakesSumFlat)):
    ingredientTypeUniq.append(soldCakesSumFlat[i]['name'])

# Removing duplicates from the list.
ingredientTypeUniq = list(set(ingredientTypeUniq))
ingredientSum = []

# This is creating a list of dictionaries with the name and
#  amount of each ingredient used in the
# cakes sold last week.
for j in range(len(ingredientTypeUniq)):
    amount = 0.00
    unit = ""
    for i in range(len(soldCakesSumFlat)):
        if soldCakesSumFlat[i]['name'] == ingredientTypeUniq[j]:
            nums = soldCakesSumFlat[i]['amount'].split(" ")[0]
            unit = soldCakesSumFlat[i]['amount'].split(" ")[1]
            amount = amount + float(nums)
    ingredientSum.append({
        'name': ingredientTypeUniq[j],
        'amount': str(amount*1.1) + " " + unit})
# This is creating a list of dictionaries with the name and
# amount of each ingredient used in the
# cakes sold last week.
updatedShoppingList = []
for i in range(len(ingredientSum)):
    newAmount = 0.00
    unit = ""
    for j in range(len(inventory)):
        if ingredientSum[i]['name'] == inventory[j]['name']:
            ingAmount = ingredientSum[i]['amount'].split(" ")[0]
            invAmount = inventory[j]['amount'].split(" ")[0]
            newAmount = float(ingAmount)-float(invAmount)
            unit = ingredientSum[i]['amount'].split(" ")[1]
    updatedShoppingList.append({
        'name': ingredientSum[i]['name'],
        'amount': str(newAmount)+" "+unit
    })

shoppingListForClerk = []

# This is creating a list of dictionaries with the name,
#  amount and total price of each ingredient.
for i in range(len(updatedShoppingList)):
    whPrice = 0.00
    newAmount = 0.00
    unit = ""
    for j in range(len(wholeSale)):
        if updatedShoppingList[i]['name'] == wholeSale[j]['name']:
            updAmount = float(updatedShoppingList[i]['amount'].split(" ")[0])
            whAmount = float(wholeSale[j]['amount'].split(" ")[0])
            whPrice = float(wholeSale[j]['price'])/whAmount
            newAmount = math.ceil(math.ceil(updAmount/whAmount)*whAmount)
            unit = updatedShoppingList[i]['amount'].split(" ")[1]
    shoppingListForClerk.append({
        'name': updatedShoppingList[i]['name'],
        'amount': str(newAmount) + " " + unit,
        'totalPrice': int(whPrice*newAmount)
    })


def myFunc(e):
    """
    It sorts the list of dictionaries by the totalPrice key,
     then removes any dictionaries with a
    negative totalPrice.

    :param e: the element in the list
    :return: A list of dictionaries.
    """
    return e['totalPrice']


shoppingListForClerk.sort(reverse=True, key=myFunc)

for i in range(len(shoppingListForClerk)):
    if shoppingListForClerk[i]['totalPrice'] < 0:
        shoppingListForClerk.remove(shoppingListForClerk[i])


with open(r".\src\answers\answerSixPython.json", 'w', encoding='utf-8') as f:
    json.dump(shoppingListForClerk, f, ensure_ascii=False, indent=4)
    f.close()
