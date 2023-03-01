import os
import pathlib
import shutil

import nox

ROOT = pathlib.Path(__file__).parent


nox.options.sessions = ["lint", "test", "test-bmi", "test-notebooks"]


@nox.session
def test(session: nox.Session) -> None:
    """Run the tests."""
    session.install("pytest", "pytest-xdist")

    args = [
        "-n",
        "auto",
        "-vvv",
    ] + session.posargs


    with session.chdir("lessons/best-practices"):
        for fname in ["examples.py", "test_examples.py"]:
            session.log(f"test -f {fname}")
            if not pathlib.Path(fname).is_file():
                session.error(f"{fname}: file does not exist")

    session.run("pytest", *args)


@nox.session(name="test-notebooks", venv_backend="mamba", python="3.9")
def test_notebooks(session: nox.Session) -> None:
    """Run the notebooks."""
    args = [
        "pytest",
        "lessons",
        "--nbmake",
        "--nbmake-kernel=python3",
        "--nbmake-timeout=3000",
        "-n",
        "auto",
        "-vvv",
    ] + session.posargs

    session.conda_install("nbmake", "pytest", "pytest-xdist")
    session.conda_install("--file", "lessons/requirements.in")

    session.run(*args)


@nox.session
def lint(session: nox.Session) -> None:
    """Look for lint."""
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files")


@nox.session(python=False)
def clean(session):
    """Remove all .venv's, build files and caches in the directory."""
    root_folders = (
        [ ".pytest_cache", ".venv", ".nox" ]
        if not session.posargs
        else []
    )

    with session.chdir(ROOT):
        for folder in root_folders:
            session.log(f"rm -r {folder}")
            shutil.rmtree(folder, ignore_errors=True)

    for folder in _args_to_folders(session.posargs):
        with session.chdir(folder):
            for pattern in ["*.py[co]", "__pycache__"]:
                session.log(f"rm {pattern}")
                _clean_rglob(pattern)

    clean_checkpoints(session)


@nox.session(python=False, name="clean-checkpoints")
def clean_checkpoints(session):
    """Remove jupyter notebook checkpoint files."""
    for folder in _args_to_folders(session.posargs):
        with session.chdir(folder):
            _clean_rglob("*-checkpoint.ipynb")
            _clean_rglob(".ipynb_checkpoints")


def _args_to_folders(args):
    return [ROOT] if not args else [pathlib.Path(f) for f in args]


def _clean_rglob(pattern):
    nox_dir = pathlib.Path(".nox")

    for p in pathlib.Path(".").rglob(pattern):
        if nox_dir in p.parents:
            continue
        if p.is_dir():
            p.rmdir()
        else:
            p.unlink()
