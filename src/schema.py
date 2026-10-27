"""Схема валидации данных Bike Sharing."""
from __future__ import annotations
import pandas as pd
import pandera.pandas as pa
from pandera.pandas import Column, DataFrameSchema, Check

schema = DataFrameSchema({
    "instant": Column(int, Check.ge(1)),
    "dteday": Column(pa.DateTime),
    "season": Column(int, Check.isin([1, 2, 3, 4])),
    "yr": Column(int, Check.isin([0, 1])),
    "mnth": Column(int, Check.in_range(1, 12)),
    "hr": Column(int, Check.in_range(0, 23)),
    "holiday": Column(int, Check.isin([0, 1])),
    "weekday": Column(int, Check.in_range(0, 6)),
    "workingday": Column(int, Check.isin([0, 1])),
    "weathersit": Column(int, Check.in_range(1, 4)),
    "temp": Column(float, Check.in_range(0, 1)),
    "atemp": Column(float, Check.in_range(0, 1)),
    "hum": Column(float, Check.in_range(0, 1)),
    "windspeed": Column(float, Check.in_range(0, 1)),
    "casual": Column(int, Check.ge(0)),
    "registered": Column(int, Check.ge(0)),
    "cnt": Column(int, Check.ge(1)),
}, strict=True)

def validate_raw(frame: pd.DataFrame) -> pd.DataFrame:
    return schema.validate(frame.dropna())
