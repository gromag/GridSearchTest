from random import random
import subprocess

num_exp = 6
random.seed(0)

max_ngram_values = [1, 2, 3]
max_itr_values = [1, 5, 10]

for _ in range(num_exp):
    params = {"rand_max_ngram": random.randint(1, 3), "rand_max_itr": random.randchoice([1, 5, 10])}
    subprocess.run(
        [
            "dvc",
            "exp",
            "run",
            "--queue",
            "--set-param",
            f"training.max_ngram={params['rand_max_ngram']}",
            "--set-param",
            f"training.max_itr={params['rand_max_itr']}",
        ]
    )
