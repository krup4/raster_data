from pystac_client import Client
from pathlib import Path
import planetary_computer
import urllib.request

item_id = "S2C_MSIL2A_20261020T070921_R106_T40SCE_20261020T103804"

catalog = Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1",
    modifier=planetary_computer.sign_inplace
)

item = next(catalog.search(
    collections=["sentinel-2-l2a"],
    ids=[item_id]
).items())

url = item.assets["visual"].href

data_dir = Path(__file__).resolve().parent / "data"
data_dir.mkdir(parents=True, exist_ok=True)
output_path = data_dir / "sentinel.tif"
urllib.request.urlretrieve(url, output_path)
print(f"Файл сохранён: {output_path}")
