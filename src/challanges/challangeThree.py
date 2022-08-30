# ------------------------------------------------------------------------------------
#          Challenge  3
# What was last week's profit?

# Now that the Tax Guys are off his back, and people with food allergies are safe,
# Stevie wants to know how much money he actually made last week. Based on the quantity of the items sold,
# with the ingredients taken into account,
# calculate the difference between the sum of sale prices and the wholesale price of the ingredients used.

# Your function should take the whole data-set, and return a number,
# the difference between the amount of money selling sweets generated,
# and the cost of producing them, calculated based on the wholesale price of the ingredients used.

# ------------------------------------------------------------------------------------

import json
from challangeOne import getTaskSumTotalSales

with open(r"./src/data/bakery.json") as f:
    data = json.load(f)
    f.close()


recipes = data['recipes']
lastWeekSales = data['salesOfLastWeek']
wholeSale = data['wholesalePrices']


# Creating a list of dictionaries with the ingredients and the amount sold for each cake.
ingredentsForSoldCakes = []
TaskSumTotalSales = 0
for i in range(len(lastWeekSales)):
    for j in range(len(recipes)):
        if lastWeekSales[i]['name'] == recipes[j]['name']:
            ingredentsForSoldCakes.append({
                "ingredients": recipes[j]['ingredients'],
                "sold" : lastWeekSales[i]['amount']
            })
            TaskSumTotalSales += int(recipes[j]['price'].split(" ")[0])* int(lastWeekSales[i]['amount'])

# Converting the amount of ingredients to the amount of ingredients needed for the sold cakes.
for sub in ingredentsForSoldCakes:
    for i in range(len(sub['ingredients'])):
        sold =int(sub['sold'])
        ingredient = str(sub['ingredients'][i]['amount']).split(" ")
        amount = float(ingredient[0])*int(sold)
        if ingredient[1] == 'g':
            sub['ingredients'][i]['amount'] = str(amount/1000) + " kg"

        elif ingredient[1] == 'ml':
            sub['ingredients'][i]['amount'] = str(amount/1000) + " l"
        else:
            sub['ingredients'][i]['amount'] = str(amount) + " pc"

# Calculating the price of the ingredients needed for the sold cakes.

lista =[]
for sub in ingredentsForSoldCakes:
    for i in range(len(sub['ingredients'])):
       
        for j in range(len(wholeSale)):
            if sub['ingredients'][i]['name'] == wholeSale[j]['name']:
                
                updAmount = float(sub['ingredients'][i]['amount'].split(" ")[0])

                whAmount = float(wholeSale[j]['amount'].split(" ")[0])
                whPrice = int(wholeSale[j]['price'])
                onewayroad = updAmount/whAmount

        lista.append({
            'totalPrice': (onewayroad * whPrice)
        })

# Calculating the total price of the ingredients needed for the sold cakes.
ingredientPrice_3 = 0
for i in range(len(lista)):
    ingredientPrice_3 += (lista[i]['totalPrice'])

TaskSumTotalProfit = int(getTaskSumTotalSales() - ingredientPrice_3)


with open(r"./src/answers/answerThreePython.json", 'w', encoding='utf-8') as f:
    json.dump(TaskSumTotalProfit, f, ensure_ascii=False, indent=4)