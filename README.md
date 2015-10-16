#EMC CF/Photon.io Demo #

The focus of this project is to demonstrate the ease of Pivotal Cloud Foundry to create a small 'IoT-Lite' application.

We will be using a Spark Particle Photon protyping board to sample the ambient temperature in a room, and display those readings on a Python Flask web app.  Readings will be posted to a REST API and stored in a redis key/value store on Cloud Foundry.

##Requirements:##
  * Laptop with the following installed:
    * Pivotal Web Services account - https://run.pivotal.io. Sign up for the 60 day free trial.
    * Cloud Foundry CLI - Available from Pivotal Web Services portal, directly from the main console page.
    * Git binaries to clone source code: https://git-scm.com/download/win
    * Account created on https://build.particle.io - for registering Photon and pushing code.

