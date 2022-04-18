<div id="top"></div>

<br />
<h2 align="center">Deploying a ML Model with Docker and FastAPI</h2>
<br />
</div>

<!-- TABLE OF CONTENTS -->
1. [About the Project](#about-the-project)
2. [Build with](#build-with)
3. [Usage](#usage)
4. [Contact](#contact)

<br />


### About the Project <a id="about-the-project"></a>
This project demonstrates how to deploy a machine learning model with docker and fastapi.

<p align="right">(<a href="#top">back to top</a>)</p>


### Built with <a id="build-with"></a>
The project was built with **Python 3.9.12** and **Docker version 20.10.14**.
The python requirements are listed in **requirements.txt**.

The main packages are the following:

* [python](https://www.python.org/)
* [docker](https://www.docker.com/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [uvicorn](https://www.uvicorn.org/)
* [scikit-learn](https://scikit-learn.org/)
* [pandas](https://pandas.pydata.org/)
* [requests](https://docs.python-requests.org/) _for testing the API (main_request.py)_

<p align="right">(<a href="#top">back to top</a>)</p>


### Usage <a id="usage"></a>
The API is deployed to port `8080` and can be accessed by [http://localhost:8080](http://localhost:8080) and the docs by [http://localhost:8080/docs](http://localhost:8080/docs).

1. Clone the repository
   ```sh
   git clone https://github.com/SimonReitzner/deploying-a-ml-model-with-docker-and-fastapi.git
   ```
2. Access folder
   ```sh
   cd deploying-a-ml-model-with-docker-and-fastapi
   ```
3. Build the docker image
   ```sh
   docker build --tag ml_fastapi:latest .
   ```
4. Start the container
   ```sh
   docker run --detach --restart always -p 8080:8080 ml_fastapi:latest
   ```
5. Request prediction
   ```sh
   python main_request.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


### Contact <a id="contact"></a>
Project Link: [Deploying a ML Model with Docker and FastAPI](https://github.com/SimonReitzner/deploying-a-ml-model-with-docker-and-fastapi)

<p align="right">(<a href="#top">back to top</a>)</p>
