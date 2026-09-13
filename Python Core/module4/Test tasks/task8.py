import time
import inspect


def log(fn):

    def wrapper(*args, **kwargs):

        # 1. Start timer
        start = time.time()

        # 2. Call the original function
        result = fn(*args, **kwargs)

        # 3. Stop timer
        end = time.time()

        # 4. Calculate execution time
        execution_time = end - start

        # 5. Get function parameters
        parameters = inspect.signature(fn).parameters

        # 6. Create a list for positional arguments
        args_info = []

        for name, value in zip(parameters, args):
            args_info.append(f"{name}={value}")

        # 7. Create a list for keyword arguments
        kwargs_info = []

        for name, value in kwargs.items():
            kwargs_info.append(f"{name}={value}")

        # 8. Convert lists into strings
        args_string = ", ".join(args_info)
        kwargs_string = ", ".join(kwargs_info)

        # 9. Create the log message
        log_message = (
            f"{fn.__name__}; "
            f"args: {args_string}; "
            f"kwargs: {kwargs_string}; "
            f"execution time: {execution_time} sec.\n"
        )

        # 10. Open the file and append the log
        with open("log.txt", "a") as file:
            file.write(log_message)

        # 11. Return the original function's result
        return result

    return wrapper
