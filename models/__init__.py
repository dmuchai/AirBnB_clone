#!/usr/bin/python3
"""Initializes the storage engine for the application."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
