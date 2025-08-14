#!/usr/bin/env python3
import os
import sys

EXPECTED_DIRS = [
    "services/market_data/app",
    "services/strategy_engine/app",
    "services/order_executor/app",
    "services/risk/app",
    "services/backtester/app",
    "services/agents/app",
    "services/ui",
]

EXPECTED_FILES = [
    "docker-compose.yml",
    ".env.example",
]

missing = []
for path in EXPECTED_DIRS:
    if not os.path.isdir(os.path.join(os.getcwd(), path)):
        missing.append(path)

for path in EXPECTED_FILES:
    if not os.path.exists(os.path.join(os.getcwd(), path)):
        missing.append(path)

if missing:
    print("Missing paths:")
    for m in missing:
        print(" -", m)
    sys.exit(1)

print("Repository structure looks OK.")