import os


def create_log_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        return True
    return False
