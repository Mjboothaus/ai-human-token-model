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

lock:
    uv lock