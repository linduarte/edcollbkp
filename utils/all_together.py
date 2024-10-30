"""
This module runs three python modules in order to execute the final backup operation #
"""
# all_together.py

# all_together.py

import time
from pathlib import Path
from . import create_backup
from . import remove_old_backups
from . import verify_backup

directory = Path("d:/reposground/work/edcollbkp/utils")

# Define list of functions to execute
functions = [
    create_backup.create_backup,
    remove_old_backups.remove_bkp,
    verify_backup.check_file,
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
