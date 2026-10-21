# Titanic Survival Prediction

An end-to-end machine learning project predicting passenger survival on the Titanic. This repository documents the iterative process from raw data processing to advanced feature engineering.

## Tech Stack
* **Language:** Python
* **Data Processing:** Pandas
* **Machine Learning:** Scikit-Learn (Decision Trees)

## Current Progress & Results
* **Baseline Established:** Cleaned raw data by imputing missing values (Median for `Age`, Mode for `Embarked`). 
* **Data Leakage Prevented:** Removed high-cardinality identifiers (`Name`, `Ticket`).
* **Model Accuracy:** Achieved **79.88%** testing accuracy using a constrained Decision Tree (`max_depth=4`) to prevent overfitting.

## Next Steps
* Engineer custom features to improve model generalization.
