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

# Creating a list of unique ingredients and a list of all ingredients.
ingredientTypeUniq = []
ingredientss = []
for i in range(len(ingredentsForSoldCakes)):
    for j in range(len(ingredentsForSoldCakes[i]['ingredients'])):
        ingredientTypeUniq.append(ingredentsForSoldCakes[i]['ingredients'][j]['name'])
        ingredientss.append(ingredentsForSoldCakes[i]['ingredients'][j])

ingredientTypeUniq = list(set(ingredientTypeUniq))


# Creating a list of dictionaries with the unique ingredients and the amount of each ingredient needed
# for the sold cakes.
ingredientSum = []
for j in range(len(ingredientTypeUniq)):
    amount = 0.00
    unit = ""
    for i in range(len(ingredientss)):
        if ingredientss[i]['name'] == ingredientTypeUniq[j]:
            nums = ingredientss[i]['amount'].split(" ")[0]
            unit = ingredientss[i]['amount'].split(" ")[1]
            amount = amount + float(nums)
    ingredientSum.append({
        'name': ingredientTypeUniq[j],
        'amount': str(amount) + " " + unit})

# Calculating the price of the ingredients needed for the sold cakes.
lista =[]
for i in range(len(ingredientSum)):
    whPrice = 0.00
    newAmount = 0.00
    unit = ""
    for j in range(len(wholeSale)):
        if ingredientSum[i]['name'] == wholeSale[j]['name']:
            updAmount = float(ingredientSum[i]['amount'].split(" ")[0])
            whAmount = float(wholeSale[j]['amount'].split(" ")[0])
            whPrice = float(wholeSale[j]['price'])/whAmount
            unit = ingredientSum[i]['amount'].split(" ")[1]
    lista.append({
        'totalPrice': (whPrice*updAmount)
    })

# Calculating the total price of the ingredients needed for the sold cakes.
ingredientPrice = 0
for i in range(len(lista)):
    ingredientPrice += (lista[i]['totalPrice'])

TaskSumTotalProfit = int(TaskSumTotalSales - ingredientPrice)

with open(r"./src/answers/answerThreePython.json", 'w', encoding='utf-8') as f:
    json.dump(TaskSumTotalProfit, f, ensure_ascii=False, indent=4)