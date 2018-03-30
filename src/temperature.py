import collections
import numpy as np


def calc_temperature_stats(temperatures_data):
    temperatures = []

    ids = np.unique([temperature_data['id'] for temperature_data in temperatures_data])
    for id in ids:
        temps = [temperature['temperature'] for temperature in temperatures_data if temperature['id'] == id]
        counters = collections.Counter(temps)
        max_count = max(counters.values())
        temperatures.append({
            'id': id,
            'median': round(np.median(temps), 2),
            'average': round(np.average(temps), 2),
            'mode': [k for k, v in counters.items() if v == max_count]
        })
    return temperatures
