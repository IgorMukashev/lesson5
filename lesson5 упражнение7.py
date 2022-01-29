import json

result_list = []
dict_plus_profit = {}
dict_minus_proit = {}
with open("file5") as file:
    acerage_profit_list = []
    for line in file.readlines():
        name, _, revenue, costs = linerstrip().split()
        profit = int(revenue) - int(costs)
        if profit > 0:
            average_profit_list.update(profit)
            dict_plus_profit.update({name: profit})
        else:
            dict_minus_profit.update({name: profit})
result_list.append(dict_plus_profit)
result_list.append(dict_minus_profit)
result_list.append({"averege_profit": sum(average_profit_list)/len(average_profit_list)})

with open("file5.json", "w") as file:
    json.dump(result_list, file)