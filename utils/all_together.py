"""
This module runs three python modules in order to execute the final backup operation #
"""
# all_together.py

# all_together.py

import time
from pathlib import Path


import utils.create_backup
import utils.remove_old_backups
import utils.verify_backup

directory = Path("d:/reposground/work/edcollbkp/utils")

# Define list of functions to execute
functions = [
    utils.create_backup.create_backup,
    utils.remove_old_backups.remove_bkp,
    utils.verify_backup.check_file,
]

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
