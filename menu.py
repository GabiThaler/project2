import pandas as pd
from typing import Dict, Any


class NaiveBayesClassifier:
    """Simple categorical Naive Bayes classifier with Laplace smoothing.

    Designed for a binary target column (default: "PlayTennis").
    """

    def __init__(self, data: pd.DataFrame, target_col: str = "PlayTennis") -> None:
        self.df = data.copy()
        self.target_col = target_col

        # will be populated in fit()
        self.d_yes: Dict[str, Dict[Any, float]] = {}
        self.d_no: Dict[str, Dict[Any, float]] = {}
        self.amount_of_rows: int = 0
        self.amount_of_yes: int = 0
        self.amount_of_no: int = 0
        self.fitted: bool = False

    # ------------------------------------------------------------------
    # Training (fitting)
    # ------------------------------------------------------------------
    def fit(self) -> None:
        """Compute conditional‑probability tables for each feature."""
        df = self.df

        # split to YES / NO classes
        yes_mask = df[self.target_col] == "Yes"
        df_yes = df[yes_mask].drop(columns=[self.target_col])
        df_no = df[~yes_mask].drop(columns=[self.target_col])

        # basic counts
        self.amount_of_rows = len(df)
        self.amount_of_yes = len(df_yes)
        self.amount_of_no = len(df_no)

        # build probability dictionaries with Laplace (add‑one) smoothing
        self.d_yes, self.d_no = {}, {}
        for col in df_yes.columns:
            unique_vals = df[col].unique()
            k = len(unique_vals)

            # YES class probabilities
            counts_yes = {val: 1 for val in unique_vals}  # initial add‑one
            counts_yes.update(df_yes[col].value_counts().to_dict())
            denom_yes = self.amount_of_yes + k
            self.d_yes[col] = {val: cnt / denom_yes for val, cnt in counts_yes.items()}

            # NO class probabilities
            counts_no = {val: 1 for val in unique_vals}
            counts_no.update(df_no[col].value_counts().to_dict())
            denom_no = self.amount_of_no + k
            self.d_no[col] = {val: cnt / denom_no for val, cnt in counts_no.items()}

        self.fitted = True

    # ------------------------------------------------------------------
    # Prediction
    # ------------------------------------------------------------------
    def _get_prob(self, table: Dict[str, Dict[Any, float]], col: str, value: Any, default: float) -> float:
        """Safely extract P(value|class,feature) with a default for unseen values."""
        return table[col].get(value, default)

    def predict(self, outlook: str, temperature: str, humidity: str, windy: bool) -> str:
        """Return 'Yes' or 'No' prediction for the given feature values."""
        if not self.fitted:
            raise RuntimeError("Model must be fitted first (call fit()).")

        # k per feature for unseen defaults
        k = {col: len(self.df[col].unique()) for col in self.df.columns if col != self.target_col}
        default_yes = {col: 1 / (self.amount_of_yes + k[col]) for col in k}
        default_no = {col: 1 / (self.amount_of_no + k[col]) for col in k}

        yes_prob = (
            self._get_prob(self.d_yes, 'Outlook', outlook, default_yes['Outlook']) *
            self._get_prob(self.d_yes, 'Temperature', temperature, default_yes['Temperature']) *
            self._get_prob(self.d_yes, 'Humidity', humidity, default_yes['Humidity']) *
            self._get_prob(self.d_yes, 'Windy', windy, default_yes['Windy']) *
            (self.amount_of_yes / self.amount_of_rows)
        )

        no_prob = (
            self._get_prob(self.d_no, 'Outlook', outlook, default_no['Outlook']) *
            self._get_prob(self.d_no, 'Temperature', temperature, default_no['Temperature']) *
            self._get_prob(self.d_no, 'Humidity', humidity, default_no['Humidity']) *
            self._get_prob(self.d_no, 'Windy', windy, default_no['Windy']) *
            (self.amount_of_no / self.amount_of_rows)
        )

        return "Yes" if yes_prob > no_prob else "No"

    # ------------------------------------------------------------------
    # Representation helpers
    # ------------------------------------------------------------------
    def __repr__(self) -> str:  # pragma: no cover
        status = "fitted" if self.fitted else "not fitted"
        return f"<NaiveBayesClassifier ({status}) rows={self.amount_of_rows}>"


# -----------------------------
# Example usage (manual test)
# -----------------------------
if __name__ == "__main__":
    csv_path = r"C:\\Users\\gmth0\\OneDrive\\Pictures\\Screenshots\\PlayTennis.csv"
    df = pd.read_csv(csv_path)

    model = NaiveBayesClassifier(df)
    model.fit()

    # prompt user
    outlook     = input("Outlook (Sunny/Rainy/Overcast): ").strip()
    temperature = input("Temperature (Hot/Mild/Cool): ").strip()
    humidity    = input("Humidity (High/Normal): ").strip()
    windy       = input("Windy (True/False): ").strip() == "True"

    print("Prediction:", model.predict(outlook, temperature, humidity, windy))
