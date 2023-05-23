from os import getlogin
from pathlib import Path


class OperatingSystemsPlatforms:
    WINDOWS = "Windows"
    LINUX = "Linux"
    MAC = "Darwin"


class Paths:
    class Storage:
        WINDOWS = Path(".gerev\\storage")
        MAC = Path(".gerev\\storage")
        LINUX = Path(f'/home/{getlogin()}/.gerev/storage/')
        DOCKER = Path(f'/home/{getlogin()}/.gerev/storage/')


class EnvironmentVariables:
    DOCKER_DEPLOYMENT = "DOCKER_DEPLOYMENT"
