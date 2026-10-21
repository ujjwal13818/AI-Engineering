import json                          # whole module: json.dumps(...)
from pathlib import Path             # one name: Path(...)
from collections import Counter, defaultdict
from dataclasses import dataclass as dc   # rarely needed
import numpy as np


import os
from dotenv import load_dotenv

load_dotenv()                                   # reads .env into environment variables

api_key = os.getenv("LLM_API_KEY")
model = os.getenv("MODEL_NAME", "default-model")   # default if missing

if not api_key:
    raise ValueError("LLM_API_KEY is not set. Add it to your .env file.")