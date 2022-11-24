import pickle


def load_model():

    with open("artifacts/model.pickle", "rb") as f:
        estimator = pickle.load(f)

    return estimator
