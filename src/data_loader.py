from sklearn.datasets import fetch_california_housing


def load_housing_data():
    housing = fetch_california_housing(as_frame=True)
    return housing.frame