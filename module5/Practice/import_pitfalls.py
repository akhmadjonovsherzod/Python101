# # first.py
# def foo():
#     print("foo() called")
#
# print("This prints always")
#
# if __name__ == "__main__":
#     print("Running first.py directly")
#     foo()
#
# # second.py
# import first
# print("second.py is running")
#
#
# If you run python first.py, output is:
#
# text
#
# Copy code
# This prints always
# Running first.py directly
# foo() called
# If you run python second.py, output is:
#
# text
#
# Copy code
# This prints always
# second.py is running


#isort package - Python package that sorts imports alphabetically and automatically separated into sections and by type
#pip install isort