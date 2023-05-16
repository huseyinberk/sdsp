## Install Project

It is a web application that uses a disease prediction model developed with machine learning. 
It makes certain classifications on diseases from the given data set and asks the user the parameters found on the data set as questions. According to the answers given, it predicts the disease that the user may have. You can view how the prediction algorithm was created in the model directory.

* Changing the parameters in the given data set does not prevent the model from working. 

### Prerequisites
* python3
* pip3

### Installation

Go to main directory, run the code below to create a new venv named *env* in your directory

	python -m venv env

To activate env,
* *Windows*

		env\Scripts\activate
* Linux

		source env/bin/activate

To install requirements,

	pip install -r back\requirements.txt

To run project,

	cd back
	python manage.py runserver

## Building a New Model

``` 
If you want to create a new model using a different dataset, you need to run the notebook named 'SDSPModel.ipynb' in the Model folder again. You can change the file named 'sdsp_patients.xlsx' for rerun. Changing the file or features will not affect the execution of the code. However, it must have a 'Diseases' feature. When this file is recompiled using a different dataset, run the code below in the /back.
```
	python manage.py collectstatic

