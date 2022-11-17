# Grid Search experiment report - Sun Nov 13 06:56:43 UTC 2022
## Intro text
## Experiments Metrics
| Experiment            | Created   | Executor   | Acc   | Rec   | Prc   | F1    | global.feature_dataset_path                                                   | global.model_path                                | featurization.path   | featurization.raw_path             | featurization.features_path   | featurization.sent_type   | training.max_ngram   | training.use_idf   | training.random_state   | training.early_stopping   | training.tol   | training.max_itr   | evaluation.conf_matrix_path               | evaluation.metrics_path          | data/cuad/features   | data/cuad/models   | data/cuad/raw   | src/evaluate.py   | src/evaluation   | src/featurization   | src/featurize.py   | src/train.py   | src/training   |
|-----------------------|-----------|------------|-------|-------|-------|-------|-------------------------------------------------------------------------------|--------------------------------------------------|----------------------|------------------------------------|-------------------------------|---------------------------|----------------------|--------------------|-------------------------|---------------------------|----------------|--------------------|-------------------------------------------|----------------------------------|----------------------|--------------------|-----------------|-------------------|------------------|---------------------|--------------------|----------------|----------------|
| workspace             | -         | -          | 0.634 | 0.634 | 0.643 | 0.613 | ['data', 'cuad', 'features', 'spacy_document_classification_train_test.json'] | ['data', 'cuad', 'models', 'doc_classifier_sgd'] | ['data', 'cuad']     | ['data', 'cuad', 'raw', 'CUAD_v1'] | ['data', 'cuad', 'features']  | spacy                     | 3                    | True               | 32                      | True                      | 0.001          | 1200               | ['model_metrics', 'confusion_matrix.png'] | ['model_metrics', 'metrics.txt'] | fadf50a              | e3c11ea            | 38056b1         | ef66322           | 8921ff7          | 50d17d1             | 9aeaef5            | b064c3e        | d0314bc        |
| gridsearch-experiment | 06:51 AM  | -          | 0.634 | 0.634 | 0.643 | 0.613 | ['data', 'cuad', 'features', 'spacy_document_classification_train_test.json'] | ['data', 'cuad', 'models', 'doc_classifier_sgd'] | ['data', 'cuad']     | ['data', 'cuad', 'raw', 'CUAD_v1'] | ['data', 'cuad', 'features']  | spacy                     | 3                    | True               | 32                      | True                      | 0.001          | 1200               | ['model_metrics', 'confusion_matrix.png'] | ['model_metrics', 'metrics.txt'] | fadf50a              | e3c11ea            | 38056b1         | ef66322           | 8921ff7          | 50d17d1             | 9aeaef5            | b064c3e        | d0314bc        |
| ├── c738691           | !         | !          | !     | !     | !     | !     | !                                                                             | !                                                | !                    | !                                  | !                             | !                         | !                    | !                  | !                       | !                         | !              | !                  | !                                         | !                                | -                    | -                  | -               | -                 | -                | -                   | -                  | -              | -              |
| ├── e392f5d           | !         | !          | !     | !     | !     | !     | !                                                                             | !                                                | !                    | !                                  | !                             | !                         | !                    | !                  | !                       | !                         | !              | !                  | !                                         | !                                | -                    | -                  | -               | -                 | -                | -                   | -                  | -              | -              |
| ├── 27abdaa           | !         | !          | !     | !     | !     | !     | !                                                                             | !                                                | !                    | !                                  | !                             | !                         | !                    | !                  | !                       | !                         | !              | !                  | !                                         | !                                | -                    | -                  | -               | -                 | -                | -                   | -                  | -              | -              |
| └── 3e73d4b           | !         | !          | !     | !     | !     | !     | !                                                                             | !                                                | !                    | !                                  | !                             | !                         | !                    | !                  | !                       | !                         | !              | !                  | !                                         | !                                | -                    | -                  | -               | -                 | -                | -                   | -                  | -              | -              |
