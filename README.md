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

## Старт (Colab)

1. Загружаем проект в GitHub и подключаем DagsHub.
2. Открываем `notebooks/lr1_data_and_pipeline.ipynb` в Google Colab.
3. Запускаем все ячейки.

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

Метрики `reports/metrics.json`.
