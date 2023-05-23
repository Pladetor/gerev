from pathlib import Path
from platform import system
from os import environ

from consts import OperatingSystemsPlatforms, Paths, EnvironmentVariables

STORAGE_PATHS = {OperatingSystemsPlatforms.WINDOWS: Paths.Storage.WINDOWS,
                 OperatingSystemsPlatforms.MAC: Paths.Storage.MAC,
                 OperatingSystemsPlatforms.LINUX: Paths.Storage.LINUX}

IS_IN_DOCKER = environ.get(EnvironmentVariables.DOCKER_DEPLOYMENT, False)

STORAGE_PATH = Paths.Storage.DOCKER if IS_IN_DOCKER else STORAGE_PATHS.get(system())
STORAGE_PATH.mkdir(parents=True, exist_ok=True)

UI_PATH = Path('/ui/') if IS_IN_DOCKER else Path('../ui/build/')
SQLITE_DB_PATH = STORAGE_PATH / 'db.sqlite3'
SQLITE_TASKS_PATH = STORAGE_PATH / 'tasks.sqlite3'
SQLITE_INDEXING_PATH = STORAGE_PATH / 'indexing.sqlite3'
FAISS_INDEX_PATH = str(STORAGE_PATH / 'faiss_index.bin')
BM25_INDEX_PATH = str(STORAGE_PATH / 'bm25_index.bin')
UUID_PATH = str(STORAGE_PATH / '.uuid')
