# DocumentClassification


```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_lg

dvc exp run
# or 
python src/feat_main.py --config params.yaml

```

## Useful commands

Reproduce pipeline:
`dvc repro`

Run new experiment with parameters changed:
`dvc exp run --set-param training.max_ngram=2 --set-param training.max_iter=10`

Schedule run of new experiment with parameters changed:
`dvc exp run --queue --set-param training.max_ngram=2 --set-param training.max_iter=10`

Run all experiments in the queue:
`dvc exp run --run-all`

Run all experiments in the queue using up to 3 concurring jobs:
`dvc exp run --run-all --jobs 3`

View past and queued experiments:
`dvc exp show`

View experiments showing only the changed columns and sorting by F1 column:
`dvc exp show  --only-changed --sort-by F1 --sort-order desc`


Remove all experiments from workspace:
`dvc exp list --names-only | xargs dvc exp remove`






## Known issues

DVC remote will require the SAS token to be created for the entire storage account and not for the single container, the latter will fail.