# raster_data

Загрузка спутникового снимка Sentinel-2 и работа с ним в GeoServer.

Установите зависимости и запустите скрипт:

```bash
python3 -m pip install pystac-client planetary-computer
python3 get_data.py
```

Скрипт скачивает снимок в `data/sentinel.tif` относительно папки проекта,
независимо от текущей папки запуска. Папка `data/` создаётся автоматически.

Для запуска GeoServer:

```bash
docker compose up --build
```

GeoServer доступен по адресу http://localhost:8080/geoserver.
Папка `data/` подключена в контейнер как `/data`, поэтому путь к снимку
в GeoServer — `/data/sentinel.tif`.
