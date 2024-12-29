PYTHON = python3
VENV = venv
PIP = $(VENV)/bin/pip
PYTHON_VENV = $(VENV)/bin/python
SRC_DIR = src
TEST_DIR = tests
REQ_FILE = requirements.txt

.PHONY: all install run clean test check-reqs

# Vérification des prérequis
check-reqs:
	@if [ ! -f $(REQ_FILE) ]; then \
		echo "Erreur: $(REQ_FILE) non trouvé" >&2; \
		echo "Assurez-vous d'être dans le bon répertoire" >&2; \
		exit 1; \
	fi

all: check-reqs install

$(VENV)/bin/activate: check-reqs
	@echo "Création de l'environnement virtuel..."
	$(PYTHON) -m venv $(VENV)
	@echo "Environnement virtuel créé avec succès"

install: $(VENV)/bin/activate
	@echo "Installation des dépendances..."
	$(PIP) install --upgrade pip
	$(PIP) install -r $(REQ_FILE)
	@echo "Installation terminée avec succès"

run:
	$(PYTHON_VENV) $(SRC_DIR)/main.py

clean:
	rm -rf $(VENV)
	rm -rf __pycache__
	rm -rf $(SRC_DIR)/__pycache__
	rm -rf $(SRC_DIR)/detection/__pycache__
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

test:
	$(PYTHON_VENV) -m pytest $(TEST_DIR)

format:
	$(PYTHON_VENV) -m black $(SRC_DIR)
	$(PYTHON_VENV) -m isort $(SRC_DIR)

lint:
	$(PYTHON_VENV) -m flake8 $(SRC_DIR)
	$(PYTHON_VENV) -m pylint $(SRC_DIR)

# Mise à jour des dépendances
update-deps:
	$(PIP) freeze > requirements.txt

help:
	@echo "Commandes disponibles:"
	@echo "  make install    - Installe l'environnement virtuel et les dépendances"
	@echo "  make run       - Lance l'application"
	@echo "  make clean     - Nettoie les fichiers temporaires et le venv"
	@echo "  make test      - Lance les tests"
	@echo "  make format    - Formate le code (black + isort)"
	@echo "  make lint      - Vérifie la qualité du code"
