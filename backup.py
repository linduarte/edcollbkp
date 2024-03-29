# Code improved by chatGPT
import os
import zipfile
from datetime import datetime
from pathlib import Path

# Configuration
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
OBJECT_TO_BACKUP = r"C:/Users/clldu/AppData/Local/Microsoft/Edge/User Data/Default/Collections/collectionsSQLite"
BACKUP_DIRECTORY = r"C:/Users/clldu/OneDrive/Python/vault/"
MAX_BACKUP_AMOUNT = 2


def create_backup():
    object_to_backup_path = Path(OBJECT_TO_BACKUP)
    backup_directory_path = Path(BACKUP_DIRECTORY)

    try:
        assert object_to_backup_path.exists()
    except AssertionError:
        print("Object to backup does not exist.")
        return

    backup_directory_path.mkdir(parents=True, exist_ok=True)

    existing_backups = [
        x
        for x in backup_directory_path.iterdir()
        if x.is_file() and x.suffix == ".zip" and x.name.startswith("backup-")
    ]

    oldest_to_newest_backup_by_name = list(
        sorted(existing_backups, key=lambda f: f.name)
    )
    while len(oldest_to_newest_backup_by_name) >= MAX_BACKUP_AMOUNT:
        backup_to_delete = oldest_to_newest_backup_by_name.pop(0)
        backup_to_delete.unlink()

    backup_file_name = f'backup-{datetime.now().strftime("%Y%m%d%H%M%S")}-{object_to_backup_path.name}.zip'

    with zipfile.ZipFile(
        str(backup_directory_path / backup_file_name), mode="w"
    ) as zip_file:
        if object_to_backup_path.is_file():
            zip_file.write(
                object_to_backup_path.absolute(),
                arcname=object_to_backup_path.name,
                compress_type=zipfile.ZIP_DEFLATED,
            )
        elif object_to_backup_path.is_dir():
            for file in object_to_backup_path.glob("**/*"):
                if file.is_file():
                    zip_file.write(
                        file.absolute(),
                        arcname=str(file.relative_to(object_to_backup_path)),
                        compress_type=zipfile.ZIP_DEFLATED,
                    )

    print("Backup is done!")


if __name__ == "__main__":
    create_backup()
