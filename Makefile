ACTIVATE_VENV=. .venv/bin/activate

build:
	docker build -t lowes-lookup .

dev-env: clean
	python3 -m venv .venv
	$(ACTIVATE_VENV); pip3 install -r requirements.txt

run-local:
	PYTHONPATH=src $(ACTIVATE_VENV); uvicorn main:app --reload

clean:
	rm -rf .venv

run: build clean-docker
	docker run -p 8080:8080 lowes-lookup
