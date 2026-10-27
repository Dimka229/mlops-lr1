# MLOps: Лабораторная работа 1 (Вариант 1 — Bike Sharing)

**Цель:** собрать проект, результат которого воспроизводится на другой машине одной последовательностью команд.

## Задача

Регрессия: предсказание количества аренд велосипедов в час (Bike Sharing, UCI).
**Поток для ЛР4:** обучение на 2011 годе, поток — 2012 год.

## Структура проекта

```
.
├── src/                 # Исходный код пайплайна
│   ├── schema.py        # Валидация данных (Pandera)
│   ├── ingest.py        # Имитация выгрузки (срез по году)
│   ├── prepare.py       # Очистка и разбиение
│   ├── featurize.py     # Генерация признаков
│   ├── train.py         # Обучение модели
│   ├── evaluate.py      # Метрики и проверка порога
│   └── tracking.py      # Логирование в MLflow (DagsHub)
├── notebooks/
│   └── lr1_data_and_pipeline.ipynb
├── data/                # Данные (исходники и промежуточные)
├── models/              # Веса моделей
├── reports/             # Метрики и графики
├── params.yaml          # Все параметры
├── dvc.yaml             # Описание пайплайна
├── pyproject.toml       # Зависимости
└── .pre-commit-config.yaml
```

## Быстрый старт (в Colab)

1. Загрузите проект в свой GitHub и подключите DagsHub.
2. Откройте `notebooks/lr1_data_and_pipeline.ipynb` в Google Colab.
3. Запустите все ячейки сверху вниз.

## Воспроизведение

```
# Развернуть окружение
pip install -q uv
uv export --frozen --no-hashes -o requirements.txt
pip install -q -r requirements.txt

# Забрать данные и воспроизвести
dvc pull
dvc repro
```

Метрики смотрите в `reports/metrics.json`.