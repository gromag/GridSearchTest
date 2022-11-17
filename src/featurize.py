from pathlib import Path
from lib.config_loader import load_config
import logging

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)
logger = logging.getLogger()


if __name__ == "__main__":
    global_config = load_config()["global"]
    features_path = Path(*global_config["feature_dataset_path"])
    raw_path = Path(*global_config["raw_path"])
    sent_type = load_config()["featurization"]["sent_type"]

    Path(features_path.parent).mkdir(parents=True, exist_ok=True)
    with open(features_path, "w") as f:
        f.write(f"{sent_type}")
