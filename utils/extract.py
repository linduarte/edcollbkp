import glob
import zipfile

files = glob.glob(r"C:/Users/clldu/OneDrive/Python/vault/*.zip")


def extract_zip():
    for file in files:
        print("Unzipping:", file)

        with zipfile.ZipFile(file, "r") as zip_ref:
            zip_ref.extractall(
                r"C:/Users/clldu/OneDrive/Python/vault_collect"
            )  # too long comment line  # noqa: E501


# if __name__ == "__main__":
extract_zip()
