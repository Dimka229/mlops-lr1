"""Этап prepare: проверка исходных данных и разбиение."""
from __future__ import annotations
from pathlib import Path
import pandas as pd
from src.schema import validate_raw
from src.utils import ensure_parent, get_logger, load_params

log = get_logger("prepare")
TRAIN_OUT = Path("data/processed/train.csv")
TEST_OUT = Path("data/processed/test.csv")

def check(frame: pd.DataFrame, target: str) -> pd.DataFrame:
    validated = validate_raw(frame)
    log.info("схема пройдена: %d строк, %d колонок", len(validated), validated.shape[1])
    if validated[target].isna().any():
        raise ValueError(f"в целевой переменной {target} есть пропуски")
    return validated

def split(frame: pd.DataFrame, test_size: float, by_time: bool, seed: int) -> tuple:
    if by_time:
        frame = frame.sort_values("dteday_hour").reset_index(drop=True)
        edge = int(len(frame) * (1 - test_size))
        return frame.iloc[:edge], frame.iloc[edge:]
    shuffled = frame.sample(frac=1.0, random_state=seed).reset_index(drop=True)
    edge = int(len(shuffled) * (1 - test_size))
    return shuffled.iloc[:edge], shuffled.iloc[edge:]

def main() -> None:
    params = load_params()
    data_params = params["data"]
    target = data_params["target"]
    raw = pd.read_csv(data_params["raw"], parse_dates=["dteday"])
    raw = check(raw, target)
    raw["dteday_hour"] = raw["dteday"] + pd.to_timedelta(raw["hr"], unit="h")
    raw = raw.drop_duplicates(subset="dteday_hour", keep="last")
    train, test = split(raw, test_size=float(data_params["test_size"]), by_time=bool(data_params["split_by_time"]), seed=int(params["train"]["seed"]))
    train.to_csv(ensure_parent(TRAIN_OUT), index=False)
    test.to_csv(ensure_parent(TEST_OUT), index=False)
    log.info("обучение: %d строк, тест: %d строк", len(train), len(test))

if __name__ == "__main__":
    main()
