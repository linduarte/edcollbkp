import glob
import os

folderPath = r"C:/Users/clldu/OneDrive/Python/vault"


def remove_bkp():
    filesList = glob.glob(folderPath + r"\*")
    for file in filesList:
        print("Removing File {}".format(file))
        os.remove(file)
    print("All Files are Remove if Existed")


# delay = int(input("Enter the delay time :"))

# start_time = threading.Timer(delay, remove_bkp)

# start_time.start()


# line 10 - Unsupported escape sequence in string literal
# "filesList = glob.glob(folderPath + "\*")"
# We can make it correct by Pylance in two ways - a: filesList = glob.glob(folderPath + "\\*") # too long comment line  # noqa: E501
# b: filesList = glob.glob(folderPath + r"\*")
