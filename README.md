# Python Backend Template

A clean starting point for Python backend services, powered by [uv](https://github.com/astral-sh/uv) for lightning-fast dependency management.

## 🚀 Getting Started

### Prerequisites

- [uv](https://github.com/astral-sh/uv) installed on your system.
- Python 3.12 (managed automatically by uv via `.python-version`).

### Installation

Setup the virtual environment and install dependencies:

```bash
make install
```

### Project Structure

```
├── .python-version    # Target Python version
├── Makefile           # Task automation
├── pyproject.toml     # Project & tool configuration
├── main.py            # Entry point
├── tests/             # Unit and integration tests (planned)
└── uv.lock            # Pinned dependencies
```

## Running

Start the main entry point:

```bash
make run
```

## Running Tests
```shell
uv run pytest
```