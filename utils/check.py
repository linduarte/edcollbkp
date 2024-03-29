import os
import time


def check_file():
    path = r"C:/Users/clldu/OneDrive/Python/vault_collect/collectionsSQLite"  # too long comment line  # noqa: E501

    ti_c = os.path.getctime(path)
    ti_m = os.path.getmtime(path)

    c_ti = time.ctime(ti_c)
    m_ti = time.ctime(ti_m)

    # delay = int(input("Enter the delay time :"))

    # start_time = threading.Timer(delay, check_file)

    # start_time.start()

    print(
        f"The file located at the path {path} \\was created at {c_ti} and was "
        f"last modified at {m_ti}"
    )
