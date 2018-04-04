# import collections
# import numpy as np
#
#
# def calc_temperature_stats(temperatures_data):
#     temperatures = []
#
#     ids = np.unique([temperature_data['id'] for temperature_data in temperatures_data])
#     for id in ids:
#         temps = [temperature['temperature'] for temperature in temperatures_data if temperature['id'] == id]
#         counters = collections.Counter(temps)
#         print(median(temps))
#         print(np.median(temps))
#         print(average(temps))
#         print(np.average(temps))
#         max_count = max(counters.values())
#         temperatures.append({
#             'id': id,
#             'median': round(np.median(temps), 2),
#             'average': round(np.average(temps), 2),
#             'mode': [k for k, v in counters.items() if v == max_count]
#         })
#     return temperatures

# Revised func (vanilla python without using numpy and collections)
def calc_temperature_stats(temperatures_data):
    temperatures = []

    ids = list(sorted(set([temperature_data['id'] for temperature_data in temperatures_data])))
    for id in ids:
        temps = [temperature['temperature'] for temperature in temperatures_data if temperature['id'] == id]
        counters = get_counters(temps)
        max_count = max(counters.values())
        temperatures.append({
            'id': id,
            'median': round(median(temps), 2),
            'average': round(average(temps), 2),
            'mode': [k for k, v in counters.items() if v == max_count]
        })
    return temperatures


def average(numbers):
    n = len(numbers)
    if n < 1:
        return None
    else:
        return sum(numbers) / n


def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted_numbers[n//2]
    else:
        return sum(sorted_numbers[n//2-1:n//2+1]) / 2


def get_counters(numbers):
    counts = dict()
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return counts
