# collect.py

# collect.py

from pathlib import Path


import utils.create_backup
import utils.remove_old_backups
import utils.verify_backup

directory = Path("d:/reposground/work/edcollbkp/utils")

# Call the necessary functions from utils module
utils.create_backup.create_backup()
utils.remove_old_backups.remove_bkp()
utils.verify_backup.check_file()
