install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black mylib/*.py 
	black *.py

lint:
	ruff check *.py mylib/*.py

deploy:
	#deploy goes here
		
all: install test format lint deploy
