# ------------------------------------------------------------------------------------
#          Challenge  1
# What was last week's sales in terms of money?

# With the Tax Authority already breathing down Stevie's neck,
# he quickly needs to report his last week of sales.
# Based on the data you received,
# calculate how much money he generated, if he only needs to
#  report his total sales.

# Your function should take the whole data-set, and return a number,
# calculated based on his last week's sales, and the price he sells
#  the sweets for.

# ------------------------------------------------------------------------------------

from ast import Num
import json

with open(r".\src\data\bakery.json") as f:
    data = json.load(f)
    f.close()

recipes = data['recipes']
lastWeekSales = data['salesOfLastWeek']


# Iterating through the lastWeekSales and recipes lists and adding the price of the item to the total
# sales.
TaskSumTotalSales = 0
for i in range(len(lastWeekSales)):
    for j in range(len(recipes)):
        if lastWeekSales[i]['name'] == recipes[j]['name']:
            TaskSumTotalSales += int(recipes[j]['price'].split(" ")[0])* int(lastWeekSales[i]['amount'])

with open(r".\src\answers\answerOnePython.json", 'w', encoding='utf-8') as f:
    json.dump(TaskSumTotalSales, f, ensure_ascii=False, indent=4)