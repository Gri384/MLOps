#!/usr/bin/env bash
set -euo pipefail

# Requires: uvicorn installed in current Python environment

run_service() {
  local app_dir="$1"
  local port="$2"
  echo "Starting ${app_dir} on :${port}"
  uvicorn main:create_app --factory --app-dir "${app_dir}" --host 0.0.0.0 --port "${port}" &
}

run_service services/market_data/app 8001
run_service services/strategy_engine/app 8002
run_service services/order_executor/app 8003
run_service services/risk/app 8004
run_service services/backtester/app 8005
run_service services/agents/app 8006

pids=$(jobs -p)
echo "Services started. PIDs: ${pids}"
trap 'echo Stopping...; kill ${pids} || true' INT TERM
wait