lint: 
	python3 -m isort **/*.py && python3 -m black **/*.py
test:
	python3 -m unittest discover tests