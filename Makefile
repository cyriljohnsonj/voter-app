clean:
	@rm -rf .env
	@rm -rf .pyc
	@echo "Cleaned application...🎉"

env: clean
	@virtualenv env --always-copy
	@echo "Environment is ready...🎉"

freeze:
	@pip freeze > requirements.txt

run:
	@echo "Starting application...🤪"
	@python main.py

install: env
	@. env/bin/activate
	@pip install -r requirements.txt
	@echo "Packages are installed...🎉"

image:
	@docker build -t voter-app:0.0.1 .
	@echo "Docker image built...😎"

