import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
import pickle
import pandas as pd


# Load the example model
with open("example_model.pkl", "rb") as f:  
    model = pickle.load(f)


class InputDataRow(BaseModel):
    """Object containing feature values for which predictions are requested."""
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    # Example values
    class Config:
        schema_extra = {
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2,
            }
        }

class OutputData(BaseModel):
    """Object containing predictions."""
    predictions: list[Union[int, float]]
    probabilities: list[list[Union[int, float]]]

# Instantiating the class FastAPI
app = FastAPI()

# Setup the root
@app.get("/")
def root() -> dict:
    """Message at the root endpoint.

    Returns:
        dict: Message.
    """
    return {"message": "Welcome to the iris classification API."}

# Expose the prediction endpoint
@app.post("/predict")
def predict(input_data: list[InputDataRow]) -> OutputData:
    """Prediction function that is exposed.

    Args:
        input_data (list[InputDataRow]): List of InputDataRows containing the feature values for which predictions are requested.

    Returns:
        OutputData: Output object with predictions and probabilites.
    """
    # Build an array from the input data
    X_new = pd.DataFrame([row.dict() for row in input_data]).values

    # Get a class predictions and probabilities
    pred = model.predict(X_new)
    prob = model.predict_proba(X_new)

    # Return the OutputData object, containing the predictions and probabilities
    return OutputData(predictions=pred.tolist(), probabilities=prob.tolist())


if __name__ == "__main__":
    # Start the API for development
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
