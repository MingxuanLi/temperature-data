# temperature-data

## Assumptions
The 'id' and 'temperature' field in the temperature data will be mandatory field and will NOT be null, the 'temperature' field will ONLY be a floating number and their sums within the max float number

## Python dependencies
This tests run on 3.6 or above

## Init Project
```make init```

## Run the app by providing the input file
```
make run file=data/empty.json
make run file=data/simple.json
make run file=data/sample.json
make run file=data/complex.json
```

You can use json-generator to generate test data https://www.json-generator.com

## Run Unit test
```make tests```

You can see the test coverage similar like below:
```
py.test --cov=src tests/test.py -v
======================================================================================================= test session starts =======================================================================================================
platform darwin -- Python 3.6.4, pytest-3.3.2, py-1.5.2, pluggy-0.6.0 -- /anaconda3/bin/python
cachedir: .cache
rootdir: /Users/mingxuanli/repo/github/temperature-data, inifile:
plugins: cov-2.5.1
collected 4 items

tests/test.py::TestTemperature::test_complex PASSED                                                                                                                                                                         [ 25%]
tests/test.py::TestTemperature::test_empty PASSED                                                                                                                                                                           [ 50%]
tests/test.py::TestTemperature::test_sample PASSED                                                                                                                                                                          [ 75%]
tests/test.py::TestTemperature::test_simple PASSED                                                                                                                                                                          [100%]

---------- coverage: platform darwin, python 3.6.4-final-0 -----------
Name                 Stmts   Miss  Cover
----------------------------------------
src/__init__.py          0      0   100%
src/temperature.py      11      0   100%
----------------------------------------
TOTAL                   11      0   100%


==================================================================================================== 4 passed in 0.23 seconds =====================================================================================================
```

