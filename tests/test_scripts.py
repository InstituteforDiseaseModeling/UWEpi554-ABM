"""Smoke test: each example script runs to completion without raising an error."""

import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

# simulation.py is a fill-in-the-blanks template, so it isn't expected to run as-is
SCRIPTS = sorted(p.name for p in ROOT.glob('*.py') if p.name != 'simulation.py')


@pytest.mark.parametrize('script', SCRIPTS)
def test_script_runs(script):
    env = os.environ | {'MPLBACKEND': 'Agg'}  # Render plots off-screen so plt.show() doesn't block
    result = subprocess.run([sys.executable, script], cwd=ROOT, env=env,
                            capture_output=True, text=True, timeout=300)
    assert result.returncode == 0, result.stderr
