# store-lookup
Simple web service for looking up a single item for multiple zip codes which isn't easily apparent on how to do via the lowes website.

**Pre Reqs:**
- Docker
- Python 3.9
- Pip 3


**Running Locally:**
- Run `make dev-env`
- Run `make run-local`
- Visit http://127.0.0.1:8000/docs to see all endpoints
- Only operational endpoint http://127.0.0.1:8000/search?product_id={product_id}&zipcode={zipcode}


**Running Locally in Docker:**
- Run `make run`
- Visit http://127.0.0.1:8080/docs to see all endpoints



A service that does this similarly for several other outlets https://brickseek.com/
