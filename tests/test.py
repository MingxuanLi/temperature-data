import json
import unittest
import numpy as np
from src import temperature

class TestTemperature(unittest.TestCase):
    def setUp(self):
        with open('./data/empty.json', 'r') as json_data:
            self.emptyData = json.load(json_data)
        with open('./data/simple.json', 'r') as json_data:
            self.simpleData = json.load(json_data)
        with open('./data/sample.json', 'r') as json_data:
            self.sampleData = json.load(json_data)
        with open('./data/complex.json', 'r') as json_data:
            self.complexData = json.load(json_data)

    def test_empty(self):
        temperatures = temperature.calc_temperature_stats(self.emptyData)
        self.assertEqual(self.emptyData, [])
        self.assertEqual(temperatures, [])

    def test_simple(self):
        temperatures = temperature.calc_temperature_stats(self.simpleData)
        self.assertEqual(temperatures[0], {'id': 'a', 'median': 3.53, 'average': 3.53, 'mode': [3.53]})

    def test_sample(self):
        self.assertEqual(len(self.sampleData), 15)
        temperatures = temperature.calc_temperature_stats(self.sampleData)
        self.assertEqual(len(temperatures), 3)

        a = [temp for temp in temperatures if temp['id'] == 'a'][0]
        b = [temp for temp in temperatures if temp['id'] == 'b'][0]
        c = [temp for temp in temperatures if temp['id'] == 'c'][0]

        self.assertEqual(a['median'], 3.64)
        self.assertEqual(a['average'], 3.78)
        self.assertEqual(a['mode'], [3.53])

        self.assertEqual(b['median'], 4.14)
        self.assertEqual(b['average'], 4.08)
        self.assertEqual(b['mode'], [4.15])

        self.assertEqual(c['median'], 3.95)
        self.assertEqual(c['average'], 3.72)
        self.assertEqual(c['mode'].sort(), [3.36, 3.96].sort())

    def test_complex(self):
        temperatures = temperature.calc_temperature_stats(self.complexData)
        a = [temp for temp in temperatures if temp['id'] == 'a'][0]
        b = [temp for temp in temperatures if temp['id'] == 'b'][0]
        g = [temp for temp in temperatures if temp['id'] == 'g'][0]

        self.assertEqual(a['median'], 13.91)
        self.assertEqual(a['average'], 13.45)
        self.assertEqual(a['mode'].sort(), [4.75, 6.97, 12.2, 13.04, 13.91, 16.0, 17.3, 17.75, 19.15].sort())

        self.assertEqual(b['median'], 17.83)
        self.assertEqual(b['average'], 17.74)
        self.assertEqual(b['mode'].sort(), [5.11, 8.96, 9.42, 14.42, 15.3, 16.78, 17.75, 17.83, 17.85, 20.36, 21.31, 24.71, 24.96, 25.56, 25.82].sort())

        self.assertEqual(g['median'], 22)
        self.assertEqual(g['average'], 19.59)
        self.assertEqual(g['mode'].sort(), [4.76, 15.68, 16.03, 22.0, 23.96, 25.22, 29.45].sort())
