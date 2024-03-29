"""
This module runs three python modules in order to execute the final backup operation #
"""

import time

import utils

# Define list of functions to execute
functions = [utils.extract_zip, utils.remove_bkp, utils.check_file]  # type: ignore


delay = 1

# Execute each function in the list
for i, func in enumerate(functions):
    print(f"Executing Function {i+1}")
    time.sleep(delay)
    try:
        func()
    except Exception as e:
        print(f"Error occurred while executing Function {i+1}: {e}")
        # Handle the exception as appropriate for your use case

if __name__ == "__main__":
    print("All functions executed successfully")
