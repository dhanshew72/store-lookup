ACTIVATE_VENV=. .venv/bin/activate
dev-env: clean
	python3 -m venv .venv
	$(ACTIVATE_VENV); pip3 install -r requirements.txt

run-local:
	PYTHONPATH=src $(ACTIVATE_VENV); uvicorn main:app --reload

clean:
	rm -rf .venv
