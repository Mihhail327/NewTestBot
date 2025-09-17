import json
from pathlib import Path
from logger import logger

ADS_FILE = Path("ads.json")

def load_ads():
    if ADS_FILE.exists():
        try:
            with open(ADS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Ошибка чтения ads.json: {e}")
            return []
    return []

def save_ad(ad):
    ads = load_ads()
    ads.append(ad)
    try:
        with open(ADS_FILE, "w", encoding="utf-8") as f:
            json.dump(ads, f, ensure_ascii=False, indent=2)
        logger.info(f"Объявление сохранено: {ad}")
    except Exception as e:
        logger.error(f"Ошибка записи в ads.json: {e}")