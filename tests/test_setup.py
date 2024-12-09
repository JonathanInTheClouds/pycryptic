from setuptools import setup
import subprocess

def test_setup():
    """Ensure that setup.py can run without errors."""
    result = subprocess.run(
        ["python", "setup.py", "--version"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
