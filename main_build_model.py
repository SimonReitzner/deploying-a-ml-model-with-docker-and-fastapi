from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import pickle


def main():
    """Build a simple model to host it later.
    
    Model is neither tuned nor evaluated. The focus is on deploying it.
    """
    
    # Load iris data and get features and target
    data = load_iris(as_frame=True)
    X, y = data.data.values, data.target

    # Train a random forest classification model
    model = RandomForestClassifier(random_state=0)
    model.fit(X, y)

    # Save the model as pickle
    with open("example_model.pkl", "wb") as f:  
        pickle.dump(model, f)


if __name__ == "__main__":
    main()