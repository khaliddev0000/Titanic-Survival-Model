### Model Performance
* **Current Accuracy:** 81.0%
* **Hyperparameters:** DecisionTreeClassifier with `max_depth=4` (optimized to prevent overfitting).
* **Feature Engineering:**
  * **Family_Size:** Combined `SibSp` and `Parch` (dropping the originals) to consolidate passenger relationships into a single metric.
  * **Family_fare:** Multiplied `Fare` by the new `Family_Size` feature to create a unified wealth/status signal, successfully pushing the baseline score from 79.88% to 81.0%.
