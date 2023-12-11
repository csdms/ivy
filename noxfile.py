import pathlib
import shutil

import nox

ROOT = pathlib.Path(__file__).parent


@nox.session
def test(session: nox.Session) -> None:
    """Run the tests."""
    session.install("matplotlib", "pandas")
    session.install("pytest", "pytest-xdist")

    with session.chdir("lessons/python/ivy-diffusion"):
        session.install("-e", ".")

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


@nox.session(name="test-notebooks", venv_backend="mamba", python="3.11")
def test_notebooks(session: nox.Session) -> None:
    """Run the notebooks."""
    args = [
        "pytest",
        "lessons",
        "--ignore-glob=*py",
        "--nbmake",
        "--nbmake-kernel=python3",
        "--nbmake-timeout=3000",
        "-n",
        "auto",
        "-vvv",
    ] + session.posargs

    session.conda_install("nbmake", "pytest", "pytest-xdist")
    session.conda_install("--file", "lessons/requirements.in")
    session.install("git+https://github.com/csdms/bmi-example-python.git")

    session.run(*args)


@nox.session(name="insert-toc")
def insert_toc(session: nox.Session) -> None:
    session.install("git+https://github.com/mcflugen/heartfelt-hooks.git")

    notebooks = (
        "lessons/landlab/landlab/bedrock_landslides_on_dems.ipynb",
        "lessons/landlab/landlab/create_a_component-solution.ipynb",
        "lessons/landlab/landlab/intro-to-grids-solution.ipynb",
        "lessons/landlab/landlab/intro_part_for_component_clinic.ipynb",
        "lessons/landlab/landlab/landlab-fault-scarp-for-espin-solution.ipynb",
        "lessons/landlab/landlab/overland_flow.ipynb",
        "lessons/landlab/landlab/practice-your-skills-solution.ipynb",
        "lessons/landlab/landlab/tidal_flow_calculator.ipynb",
    )

    for notebook in notebooks:
        session.run("insert-toc", "--in-place", "--allow-missing-toc", "-vvv", notebook)


@nox.session(name="hide-solutions")
def hide_solutions(session: nox.Session) -> None:
    session.install("git+https://github.com/mcflugen/heartfelt-hooks.git")

    insert_toc(session)

    solution_notebooks = (
        (
            "lessons/landlab/landlab/practice-your-skills-solution.ipynb",
            "lessons/landlab/landlab/practice-your-skills.ipynb",
        ),
        (
            "lessons/landlab/landlab/intro-to-grids-solution.ipynb",
            "lessons/landlab/landlab/intro-to-grids.ipynb",
        ),
        (
            "lessons/landlab/landlab/landlab-fault-scarp-for-espin-solution.ipynb",
            "lessons/landlab/landlab/landlab-fault-scarp-for-espin.ipynb",
        ),
        (
            "lessons/landlab/landlab/create_a_component-solution.ipynb",
            "lessons/landlab/landlab/create_a_component.ipynb",
        ),
    )

    for solution, lesson in solution_notebooks:
        shutil.copy(solution, solution + ".bak")
        out = session.run(
            "hide-solution-cells",
            "--silent",
            "--tags-to-hide=solution",
            solution,
            external=True,
            silent=True,
        )

        session.log(f"overwriting {lesson}")
        with open(lesson, "w") as fp:
            fp.write(out)


@nox.session
def lint(session: nox.Session) -> None:
    """Look for lint."""
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files")


@nox.session(python=False)
def clean(session):
    """Remove all .venv's, build files and caches in the directory."""
    root_folders = [".pytest_cache", ".venv", ".nox"] if not session.posargs else []

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
