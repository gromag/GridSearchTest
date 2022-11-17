# base imports
import logging
from pathlib import Path
import string

from lib.config_loader import load_config

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


# local

logging.basicConfig()
logging.root.setLevel(logging.INFO)
logger = logging.getLogger()


def save_metrics(results, metrics_path: Path):
    output = f'Acc: {results["acc"]:.3f}\nRec: {results["rec"]:.3f}\nPrc: {results["prc"]:.3f}\nF1: {results["f1"]:.3f}\n'  # noqa: E501

    with open(str(metrics_path), "w") as outfile:
        outfile.write(output)

    print(output)


def plot_confusion_matrix(y_test, y_pred, labels, conf_matrix_path: Path):

    conf_matrix = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(15, 12))
    ax = sns.heatmap(conf_matrix, cmap="YlOrBr", annot=True)
    ax.set_xticklabels(labels, rotation=45)
    ax.set_yticklabels(labels, rotation=0)
    plt.savefig(str(conf_matrix_path))


if __name__ == "__main__":

    config = load_config()
    conf_matrix_path = Path(*config["evaluation"]["conf_matrix_path"])
    metrics_path = Path(*config["evaluation"]["metrics_path"])
    dataset_path = Path(*config["global"]["feature_dataset_path"])
    model_path = Path(*config["global"]["model_path"])

    results = {"acc": 0.5, "rec": 0.5, "prc": 0.5, "f1": 0.5}
    save_metrics(results, metrics_path)

    y_test = [0, 1, 2, 3]
    y_pred = [0, 1, 3, 2]
    labels = [letter for letter in string.ascii_uppercase[:4]]

    plot_confusion_matrix(y_test, y_pred, labels, conf_matrix_path)
