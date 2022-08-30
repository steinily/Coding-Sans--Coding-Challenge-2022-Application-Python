# ------------------------------------------------------------------------------------
#          Challenge  4
#      The freedom of choice

# The best-selling items are already available,
# but Stevie wants to know what sweets he could make without purchasing
# additional ingredients, only working from his existing inventory.

# At this point, Stevie confesses with tears in his eyes that he somehow
#  managed to go through primary school without actually
# learning metric unit conversions. He only knows milliliters and grams,
#  so the recipes in his cookbook are in these units.
# However, his inventory software, and the wholesaler both report in
#  kilograms and liters.

# This hasn't been much of a problem as long as he was conducting heart
#  surgeries, apart from getting weird looks from his butcher
# when asking for 1523 grams of chicken breast. But he can't run a bakery
#  like this, so he needs your help.

# Give Stevie the amount of sweets he could produce,if he used his entire
#  inventory for one recipe.
# Do this for each recipe he can make based on his current inventory and
#  list it in alphabetic order based on the recipe's name.
# Your function should take the whole data-set, and return a list matching
#  the structure of the example below.

# ------------------------------------------------------------------------------------


import json
import re


with open(r"./src/data/bakery.json") as f:
    data = json.load(f)
    f.close()

recipes = data['recipes']
inventory = data['inventory']

# Creating a list of dictionaries, where each dictionary
#  has a name and ingredients key.
recipiesandingredients = []
for i in range(len(recipes)):
    recipiesandingredients.append(
        {'name': recipes[i]['name'], 'ingredients': recipes[i]['ingredients']})


# Converting the units of the ingredients to kg, l, and pc.
for sub in recipiesandingredients:
    for i in range(len(sub['ingredients'])):
        ingredient = str(sub['ingredients'][i]['amount']).split(" ")
        amount = float(ingredient[0])

        if ingredient[1] == 'g':
            sub['ingredients'][i]['amount'] = str(amount/1000) + " kg"
        elif ingredient[1] == 'ml':
            sub['ingredients'][i]['amount'] = str(amount/1000) + " l"
        else:
            sub['ingredients'][i]['amount'] = str(amount) + " pc"


# Calculating the maximum amount of each ingredient that can be used.
for i in range(len(recipiesandingredients)):
    for j in range(len(recipiesandingredients[i]['ingredients'])):
        for k in range(len(inventory)):
            if recipiesandingredients[i]['ingredients'][j]['name'] == inventory[k]['name']:
                invAmount = float(inventory[k]['amount'].split(" ")[0])
                ingAmount = float(
                    recipiesandingredients[i]['ingredients'][j]['amount'].split(" ")[0])
                recipiesandingredients[i]['ingredients'][j]['max'] = invAmount/ingAmount


def myFunc(e):
    """
    It sorts the list of dictionaries by the totalPrice key,
     then removes any dictionaries with a
    negative totalPrice.

    :param e: the element in the list
    :return: A list of dictionaries.
    """

    return e['max']


for i in range(len(recipiesandingredients)):
    recipiesandingredients[i]['ingredients'].sort(reverse=True, key=myFunc)

# Creating a list of dictionaries, where each dictionary
#  has a name and amount key.
TaskCalcTotalBakeableAmount = []
for sub in recipiesandingredients:
    TaskCalcTotalBakeableAmount.append({
        'name': sub['name'],
        'amount': int(sub['ingredients'][-1]['max'])
    })


def f_remove_accents(old):
    """
    Removes common accent characters, lower form.
    Uses: regex.
    """
    new = old.encode("cp1252").decode("utf-8").lower()
    new = re.sub(r'[àáâãäå]', 'a', new)
    new = re.sub(r'[èéêë]', 'e', new)
    new = re.sub(r'[ìíîï]', 'i', new)
    new = re.sub(r'[òóôõö]', 'o', new)
    new = re.sub(r'[ùúûü]', 'u', new)
    return new


def sortbyname(e):
    """
    It removes accents from a string

    :param e: the element of the list
    :return: the value of the variable new.
    """
    new = f_remove_accents(e['name'])
    return new


TaskCalcTotalBakeableAmount.sort(key=sortbyname)

with open(r"./src/answers/answerFourPython.json", 'w') as f:
    json.dump(TaskCalcTotalBakeableAmount, f, ensure_ascii=False, indent=4)
    f.close()
