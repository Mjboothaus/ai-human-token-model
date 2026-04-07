default:
    just --list

sync:
    uv sync

notebook-edit:
    uv run marimo edit notebooks/main.py

notebook-run:
    uv run marimo run notebooks/main.py

notebook-check:
    uv run marimo check notebooks/main.py

lint:
    uv run ruff check .

lint-fix:
    uv run ruff check . --fix

typecheck:
    uv run ty check .
test:
    uv run pytest

check:
    just lint
    just typecheck
    just test

lock:
    uv lock