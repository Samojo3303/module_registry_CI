import os

## =================== UPDATE THESE VALUES =================== ##
# Env variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "default_token")
LOG_LEVEL = 2
LOG_FILE = os.getenv("LOG_FILE", "/home/runner/work/module_registry/log.txt")

# Repository location
REPO_PATH = os.getenv("REPO_PATH", "/home/runner/work/module_registry")



## =================== DO NOT MODIFY BELOW THIS LINE =================== ##
# constants
ONE_URL = os.path.join(os.path.dirname(os.path.realpath(__file__)), "one-url.txt")

# JSON Fields
FIELDS = [
    "URL",
]

SCORE_FIELDS = [
    "NetScore",
    "RampUp",
    "Correctness",
    "BusFactor",
    "ResponsiveMaintainer",
    "License",
    "Depends",
    "Pull"
]

LATENCY_FIELDS = [ f"{s}_Latency" for s in SCORE_FIELDS ]
ALL_FIELDS = FIELDS + SCORE_FIELDS + LATENCY_FIELDS

# printing Colors
ESC="\033"
RED=ESC+"[91m"
GREEN=ESC+"[92m"
YELLOW=ESC+"[93m"
BLUE=ESC+"[94m"
RESET=ESC+"[0m"
BOLD=ESC+"[1m"
