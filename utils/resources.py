from pathlib import Path


def path(picture):
    return str(Path(__file__).parent.parent.joinpath(f'resources/{picture}'))