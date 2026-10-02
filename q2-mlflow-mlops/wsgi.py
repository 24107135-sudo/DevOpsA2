"""
WSGI entrypoint for Gunicorn.

Gunicorn imports this module instead of running serve_model.py as __main__,
so the model has to be loaded explicitly before the first request arrives.
"""

from serve_model import app, load_model

load_model()