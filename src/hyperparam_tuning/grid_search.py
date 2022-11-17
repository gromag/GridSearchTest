import itertools
import subprocess


max_ngram_values = [11, 12]
max_itr_values = [4, 8]

for max_ngram, max_itr in itertools.product(max_ngram_values, max_itr_values):
    subprocess.run(
        [
            "dvc",
            "exp",
            "run",
            "--queue",
            "--set-param",
            f"training.max_ngram={max_ngram}",
            "--set-param",
            f"training.max_itr={max_itr}",
        ]
    )
