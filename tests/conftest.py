"""Shared pytest fixtures for library0 tests."""
from pathlib import Path

import pytest


@pytest.fixture
def tmp_vault(tmp_path: Path) -> Path:
    """Provide a tmp dir to use as a vault root."""
    return tmp_path
