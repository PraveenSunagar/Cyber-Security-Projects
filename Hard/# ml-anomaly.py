
# ml/anomaly.py

import numpy as np
from sklearn.ensemble import IsolationForest


class AnomalyDetector:

    def __init__(self):

        self.model = IsolationForest(
            n_estimators=200,
            contamination=0.05,
            random_state=42
        )

        self.trained = False

    def train(self, data):

        self.model.fit(np.array(data))

        self.trained = True

    def predict(self, features):

        if not self.trained:
            return {
                "anomaly": False,
                "score": 0
            }

        x = np.array([features])

        prediction = self.model.predict(x)[0]
        score = self.model.decision_function(x)[0]

        return {
            "anomaly": prediction == -1,
            "score": float(score)
        }
