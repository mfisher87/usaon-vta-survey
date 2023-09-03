import nox

nox.options.default_venv_backend = "mamba"


@nox.session
def typecheck(session):
    session.install("--file environment.yml")
    session.install("mypy")

    session.run("mypy")

