# gcp-cloudrun-bikeshare-model-repo
Code repo to deploy the machine learning model of bike sharing in cloudrun.

## Steps to create ML model with the coupon data.
* This dataset contains the hourly and daily count of rental bikes between years 2011 and 2012 in Capital bikeshare system with the corresponding weather and seasonal information.
  * https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset
  * hour.csv.

* Requirement text file has all the dependency python package libraries.

* model-training.py contains the code of data cleaning and model creation.
  * Local model creation.
  * Model used is RandomForest.
  * Generate the joblib file of the model and store in the same folder.
  * Push the model to cloud strorage bucket

* The model is going to be served via the Flask app.

* Local Testing - 
  * Execute the flask app.
  * Run the first coomand for the model prediction from "deploy-curl-command.sh".

* Docker image
  * Containerize the flask app.
  * Push the model to GCP Artifact registry.
  * Auto build the new docker image with the Cloud Build.

* Deploy the code
  * Cloud build will deploy the code on Cloud Run.
  * Run the second command from "deploy-curl-commands.sh" for the model prediction.
