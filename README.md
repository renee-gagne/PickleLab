#READ ME
### This repository demonstrates the process of modeling an ML pipeline and pickling it. After building, fitting, and pickling the model, we will build a simple Flask app that allows users to send HTTP POST requests. For this project, the Diabetes dataset is used, sourced from Open ML with id 37.

---

## INSTALLING WITH PIP
### The required installations are listed in the requirements.txt file. You can individually install each file using 'pip install package', or install the requirements.txt file.

## LAUNCHING JUPYTER LAB
### To launch Jupyter Lab, you will need to first install it into your virtual environment (pip install jupyterlab)(see above and requirements.txt). After installing, you can open Jupyter Lab in your browser by typing 'jupyter_lab' into your terminal in your virtual environment.

## FITTING A MODEL
### Fitting the model is done after building the pipeline in the test_pickle.py file.

## USING THE TEST FILE
### The test dataset is created by using the json package on a pandas data frame of the first row of data from the dataset.

## MAKING AN APP WITH FLASK
### To make a Flask app, first ensure that the previous steps for building and pickling a model have been completed. Also make sure that Flask and requests have been installed to your virtual environment(i.e. 'pip install Flask').

### Note that a great source to start building the app is the Flask Quick Start guide. Begin by creating a new python file and establishing environment variables (i.e 'FLASK_APP=filename.py flask run'). The environment variables function as key-value pairs that operate within your environment running for the application. In your new file, build a JSON route following the instructions outlined on the Quick Start Guide. Then, create another file that specifically uses the python requests library to run with the app. 
