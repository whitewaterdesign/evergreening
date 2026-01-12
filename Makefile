# Variables
PYTHON = uv run python
UV = uv

.PHONY: help install run lock sync clean lint ruff mypy black

# Default target: show help
help:
	@echo "Usage:"
	@echo "  make install   Install dependencies"
	@echo "  make run       Run the application (main.py)"
	@echo "  make lint      Run all linters (ruff, mypy, black)"
	@echo "  make ruff      Run ruff check"
	@echo "  make mypy      Run static type analysis"
	@echo "  make black     Run black formatter check"
	@echo "  make sync      Sync dependencies with lockfile"
	@echo "  make lock      Update the lockfile"
	@echo "  make clean     Remove temporary files"

# Install dependencies and setup venv
install:
	$(UV) sync

# Run the main application
run:
	$(PYTHON) main.py

# Linting and Formatting
lint: ruff mypy black

ruff:
	$(UV) run ruff check .

mypy:
	$(UV) run mypy .

black:
	$(UV) run black --check .

# Update the lockfile
lock:
	$(UV) lock

# Sync the environment with the lockfile
sync:
	$(UV) sync

# Clean up python cache and build artifacts
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf .ruff_cache