
# base imports
import logging
from pathlib import Path

# local
from lib.config_loader import load_config


logging.basicConfig()
logging.root.setLevel(logging.DEBUG)
logger = logging.getLogger()


if __name__ == "__main__":

    config = load_config()
    config_training = config["training"]
    dataset_path = Path(*config["global"]["feature_dataset_path"])
    model_path = Path(*config["global"]["model_path"])
    max_ngram = config_training["max_ngram"]
    use_idf = config_training["use_idf"]
    random_state = config_training["random_state"]
    early_stopping = config_training["early_stopping"]
    tol = config_training["tol"]
    max_itr = config_training["max_itr"]

    Path(model_path.parent).mkdir(parents=True, exist_ok=True)
    with open(model_path, "w") as model:
        model.write(f"{max_ngram}-{use_idf}-{random_state}-{early_stopping}-{tol}")
