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

with open(r".\src\data\bakery.json") as f:
    data = json.load(f)
    f.close()

recipes = data['recipes']
lastWeekSales = data['salesOfLastWeek']
wholeSale = data['wholesalePrices']

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


for sub in ingredentsForSoldCakes:
    for i in range(len(sub['ingredients'])):
        sold =int(sub['sold'])
        ingredient = str(sub['ingredients'][i]['amount']).split(" ")
        amount = float(ingredient[0])*float(sold)
        if ingredient[1] == 'g':
            sub['ingredients'][i]['amount'] = str(amount/1000) + " kg"

        elif ingredient[1] == 'ml':
            sub['ingredients'][i]['amount'] = str(amount/1000) + " l"
        else:
            sub['ingredients'][i]['amount'] = str(amount) + " pc"

ingredientTypeUniq = []
ingredientss = []
for i in range(len(ingredentsForSoldCakes)):
    for j in range(len(ingredentsForSoldCakes[i]['ingredients'])):
        ingredientTypeUniq.append(ingredentsForSoldCakes[i]['ingredients'][j]['name'])
        ingredientss.append(ingredentsForSoldCakes[i]['ingredients'][j])

ingredientTypeUniq = list(set(ingredientTypeUniq))


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
            newAmount = updAmount/whAmount
            unit = ingredientSum[i]['amount'].split(" ")[1]
    lista.append({
        'totalPrice': int(whPrice*newAmount)
    })

ingredientPrice = 0
for i in range(len(lista)):
    ingredientPrice += int(lista[i]['totalPrice'])
print(TaskSumTotalSales)
print(ingredientPrice)

