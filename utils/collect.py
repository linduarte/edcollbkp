# collect.py

# collect.py

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
