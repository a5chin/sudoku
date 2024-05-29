"""Module containing error handlers for HTTP errors."""

from app.api.errors.http_error import http_error_handler
from app.api.errors.validation_error import http422_error_handler

__all__ = ["http_error_handler", "http422_error_handler"]
