import os


class Cd:
    """
    Context manager that changes the current working directory to the
    given path, and restores the previous working directory on exit.
    """

    def __init__(self, path):
        if not os.path.isdir(path):
            raise ValueError(f"'{path}' is not a directory or does not exist.")
        self.path = path
        self.previous_dir = None

    def __enter__(self):
        self.previous_dir = os.getcwd()
        os.chdir(self.path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.previous_dir)
        return False