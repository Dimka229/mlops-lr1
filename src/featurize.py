"""Этап featurize."""
from __future__ import annotations
from pathlib import Path
import numpy as np
import pandas as pd
from src.utils import ensure_parent, get_logger, load_params

log = get_logger("featurize")
IN = {"train": Path("data/processed/train.csv"), "test": Path("data/processed/test.csv")}
OUT = {"train": Path("data/features/train.csv"), "test": Path("data/features/test.csv")}

def build(frame: pd.DataFrame, target: str, drop: list[str], cyclic_hour: bool) -> pd.DataFrame:
    to_drop = [c for c in drop if c in frame.columns]
    features = frame.drop(columns=to_drop, errors="ignore")
    features = features.drop(columns=["dteday_hour"], errors="ignore")
    if cyclic_hour:
        hour = features.pop("hr")
        features["hr_sin"] = np.sin(2 * np.pi * hour / 24)
        features["hr_cos"] = np.cos(2 * np.pi * hour / 24)
    ordered = [c for c in features.columns if c != target]
    if target in features.columns:
        ordered.append(target)
    return features[ordered]

def main() -> None:
    params = load_params()
    target = params["data"]["target"]
    drop = list(params["data"]["drop"])
    cyclic_hour = bool(params["featurize"]["cyclic_hour"])
    for part, path in IN.items():
        frame = pd.read_csv(path)
        built = build(frame, target=target, drop=drop, cyclic_hour=cyclic_hour)
        built.to_csv(ensure_parent(OUT[part]), index=False)
        log.info("%s: %d строк, признаков %d", part, len(built), built.shape[1] - 1)

if __name__ == "__main__":
    main()
