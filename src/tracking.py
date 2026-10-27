"""Обертка над MLflow."""
from __future__ import annotations
import os
from typing import Any
import mlflow
import mlflow.sklearn
import pandas as pd

def _enabled() -> bool:
    return bool(os.environ.get("MLFLOW_TRACKING_URI"))

def start_run(experiment: str, params: dict[str, Any]) -> None:
    if not _enabled(): return
    mlflow.set_experiment(experiment)
    mlflow.start_run()
    mlflow.log_params({k: v for k, v in params.items() if not isinstance(v, (list, dict))})

def log_metrics(metrics: dict[str, float]) -> None:
    if not _enabled(): return
    mlflow.log_metrics(metrics)

def log_model(model: Any, feature_names: list[str], sample: pd.DataFrame) -> None:
    if not _enabled(): return
    mlflow.sklearn.log_model(model, "model", input_example=sample)
