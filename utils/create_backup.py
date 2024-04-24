# verify_backup.py

# create_backup.py

import zipfile
from datetime import datetime
from pathlib import Path


def create_backup():
    file_to_backup = r"C:/Users/clldu/AppData/Local/Microsoft/Edge/User Data/Profile 1/Collections/collectionsSQLite"
    backup_directory = r"C:/Users/clldu/OneDrive/Python/vault"

    object_to_backup_path = Path(file_to_backup)
    backup_directory_path = Path(backup_directory)

    # Validate the object we are about to backup exists before we continue
    assert object_to_backup_path.exists(), "Object to backup does not exist."

    # Validate the backup directory exists and create if required
    backup_directory_path.mkdir(parents=True, exist_ok=True)

    # Create zip file
    backup_file_name = f'backup-{datetime.now().strftime("%Y%m%d%H%M%S")}-{object_to_backup_path.name}.zip'
    with zipfile.ZipFile(
        backup_directory_path / backup_file_name, mode="w"
    ) as zip_file:
        zip_file.write(
            object_to_backup_path.absolute(),
            arcname=object_to_backup_path.name,
            compress_type=zipfile.ZIP_DEFLATED,
        )

    print("Backup is done!")
