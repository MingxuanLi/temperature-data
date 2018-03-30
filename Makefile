.PHONY: init test

init:
	pip install -r requirements.txt

test:
	py.test --cov=src tests/test.py -v

run:
	python main.py ${file}
