from contextlib import ContextDecorator
from datetime import datetime


class LogFile(ContextDecorator):
    """
    Context manager / decorator that logs the start time, execution time,
    and any error that occurred while the wrapped block/function was running.
    """

    def __init__(self, filename):
        self.filename = filename
        self.start_time = None

    def __enter__(self):
        self.start_time = datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = datetime.now()
        run_time = end_time - self.start_time

        error_message = None if exc_val is None else str(exc_val)

        log_line = (
            f"Start: {self.start_time} | "
            f"Run: {run_time} | "
            f"An error occurred: {error_message}\n"
        )

        with open(self.filename, "a") as log_file:
            log_file.write(log_line)

        # Returning False (or None) re-raises any exception that occurred
        return False