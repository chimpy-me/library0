"""Smoke test: verify the package is importable and reports its version."""
import library0


def test_package_imports_and_reports_version():
    assert library0.__version__ == "0.0.1"
