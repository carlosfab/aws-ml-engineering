import os
from pathlib import Path

PARENT_DIR = Path(__file__).parent.resolve().parent
CODE_DIR = PARENT_DIR / "src"
TEST_DIR = PARENT_DIR / "tests"
DATA_DIR = PARENT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
TRANSFORMED_DATA_DIR = DATA_DIR / "transformed"

if not Path(TRANSFORMED_DATA_DIR).exists():
    os.mkdir(TRANSFORMED_DATA_DIR)
