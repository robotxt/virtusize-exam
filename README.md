# Virtusize Exam 

## Requirements:

**Python:** ^3.10

**Fastapi:** ^0.110.1

**Poetry**: Dependency Management Tool ([https://python-poetry.org/docs/](https://python-poetry.org/docs/))


## Development setup:

**Run localhost:**

`make run` or `uvicorn main:app --reload`


## Documentation:
**API Documentation:**

swagger/openapi ([http://localhost:8000/docs](http://localhost:8000/docs))

**Wordcount API:**
This will trigger a GET request to the url and get the content of the HTML
It will use regex to search a keyword in the HTML and it will return number of keyword match