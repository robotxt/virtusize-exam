
.PHONY: run 
run:
	uvicorn main:app --reload


.PHONY: test
test:
	pytest --cov=. tests/