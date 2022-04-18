import requests
import json


def main():
    """An example request for the model predictions from the API."""

    # Setup the request body with two vectors we want to request predictions for
    request_body = [
        {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        },
        {
            "sepal_length": 5.7,
            "sepal_width": 3.1,
            "petal_length": 4.9,
            "petal_width": 2.2
        }
    ]

    # Post request to url
    response = requests.post("http://127.0.0.1:8080/predict", json=request_body)
    
    # Print response
    print(json.loads(response.content))


if __name__ == "__main__":
    main()