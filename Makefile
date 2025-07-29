.PHONY: install migrate run clean test shell

# Python interpreter to use
PYTHON := python3

# Install dependencies
install:
	$(PYTHON) -m pip install -r requirements.txt

# Run database migrations
migrate:
	$(PYTHON) manage.py migrate

# Run development server
run:
	$(PYTHON) manage.py runserver

# Create superuser
createsuperuser:
	$(PYTHON) manage.py createsuperuser

# Run Django shell
shell:
	$(PYTHON) manage.py shell

# Run tests
test:
	$(PYTHON) manage.py test

# Clean Python cache files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete

# Default target
all: install migrate run 