## Install Project

For windows,
In main directory,
<DIR> back
<DIR> Model
<DIR> back
->python -m venv env
To activate env,
->env\Scripts\activate
To install requirements,
->pip install -r back\requirements.txt
To run project,
->cd back
->python manage.py runserver


For Linux,
In main directory,
back Model
->python -m venv env
To activate env,
->source env/bin/activate
To install requirements,
->pip install -r back\requirements.txt
To run project,
->cd back
->python manage.py runserver

Building a new model,
If you want to create a new model using a different dataset, 
you need to run the file named 'SDSPModel.ipynb' in the Model 
folder again. You can change the file named 'sdsp_patients.xlsx' 
for rerun. Changing the file or features will not affect the 
execution of the code. However, it must have a 'Diseases' feature. 
When this file is recompiled using a different dataset, the 
->python manage.py collectstatic 
method must be run in the back folder.
