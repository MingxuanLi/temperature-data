import sys
import json
from src import temperature

with open(sys.argv[1], 'r') as json_data:
    temperaturesData = json.load(json_data)

res = temperature.calc_temperature_stats(temperaturesData)
print(res)