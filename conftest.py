import django
import pytest

pytest_plugins = ["django"]  # Garante que pytest-django seja carregado
django.setup()
