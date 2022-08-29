# ------------------------------------------------------------------------------------
#          Challenge  2
# Create a menu for people with food allergies.

# Currently, Stevie keeps all information about gluten or lactose free options in his head,
# and his memory isn’t getting better.
# To avoid him having a local hospital on speed-dial, create a list of gluten and lactose-free items!
# It should have three sections, gluten-free only , lactose-free only , and both gluten and lactose-free.

# Your function should take the whole data-set,
# and return an object, with the three options containing an array of objects with the name,
# and price of each item.
# ------------------------------------------------------------------------------------


import json

with open(r".\src\data\bakery.json") as f:
    data = json.load(f)
    f.close()

recipes = data['recipes']

TaskGroupByIntolerance = []

lactoseFree = []
lactoseAndGluteFree = []
glutenFree = []
# Iterating through the recipes list and checking if the recipe is lactose free and gluten free, if it
# is then it adds it to the lactoseAndGluteFree list. If it is lactose free but not gluten free then
# it adds it to the lactoseFree list. If it is gluten free but not lactose free then it adds it to the
# glutenFree list.
for i in range(len(recipes)):
    
    if (recipes[i]['lactoseFree'] and recipes[i]['glutenFree']) == True:
        lactoseAndGluteFree.append({
            'name': recipes[i]['name'],
            'price':recipes[i]['price']
        }
        )
    
    if (recipes[i]['lactoseFree'] and not recipes[i]['glutenFree']) == True:
        lactoseFree.append(
            {
                'name': recipes[i]['name'],
                'price':recipes[i]['price']
            }
        )
    
    if (recipes[i]['glutenFree'] and not recipes[i]['lactoseFree']) == True:
        glutenFree.append(
            {
                'name': recipes[i]['name'],
                'price':recipes[i]['price']
            }
        )
    

TaskGroupByIntolerance.append({
        'glutenFree' : glutenFree,
        'lactoseFree': lactoseFree,
        'lactoseAndGlutenFree':lactoseAndGluteFree
    })


with open(r".\src\answers\answerTwoPython.json", 'w', encoding='ISO-8859-1') as f:
    f.write(str(TaskGroupByIntolerance).strip('[]'))
    f.close()
