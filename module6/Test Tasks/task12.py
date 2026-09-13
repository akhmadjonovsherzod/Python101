import os
import shutil
import uuid


class TempDir:
    """
    Context manager that creates a new temporary directory with a random,
    unique name, switches the current working directory into it, and on
    exit restores the previous working directory and removes the temporary
    directory (with all its contents).
    """

    def __init__(self, prefix="tmp_"):
        self.prefix = prefix
        self.dir_name = None
        self.previous_cwd = None

    def __enter__(self):
        # Generate a unique directory name
        self.dir_name = f"{self.prefix}{uuid.uuid4().hex}"

        # Create the directory using os.mkdir
        os.mkdir(self.dir_name)

        # Remember where we were, then move into the new directory
        self.previous_cwd = os.getcwd()
        os.chdir(self.dir_name)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Go back to the previous working directory first
        os.chdir(self.previous_cwd)

        # Remove the temporary directory and everything inside it
        full_path = os.path.join(self.previous_cwd, self.dir_name)
        shutil.rmtree(full_path)

        # Returning False (or None) lets any exception propagate normally
        return False