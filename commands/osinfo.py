import os
import platform


def get_os_platform():
    return platform.system()


def get_os_release():
    return platform.release()
