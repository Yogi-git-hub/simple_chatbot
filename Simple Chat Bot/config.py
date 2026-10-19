# This code is responsible for read all required config things for process
from dotenv import load_dotenv
from pathlib import Path
import os

BASE_PATH=Path(__file__).resolve().parent

load_dotenv(Path.joinpath(BASE_PATH,'.env'))

BASE_MODEL=os.getenv("BASE_MODEL","hermes3:3b")

BASE_URL=os.getenv("BASE_URL",None)

API_KEY=os.getenv("API_KEY",None)





