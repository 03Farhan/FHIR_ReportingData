# FHIR_Reporting
An API for generating data for reports and an application which generates graphs to be used in reports using the data provided by the API.

The API is the ReportDataAPI.py file and the application for generating graphs is the ReportGraphs.py file.

# Setup

Firstly, please review the following deployment guide link which contains the instructions and source code for the FHIR standard access at Great Ormond St Hospital: https://github.com/goshdrive/FHIRworks_2020

Once you have the dotnet app running, clone or download this folder.
Open up a terminal and navigate to the cloned/downloaded folder. In this folder, you will need to setup a virtual environment (https://docs.python.org/3/tutorial/venv.html).

Once the virtual environrnment has been setup, enter the virtual environment and run the command 'pip3 install -r requirements.txt'. Once all the requirements have been installed, you can run the API from the environment using 'python3 ReportDataAPI.py'. To generate the graphs, use the command 'python3 ReportGraphs.py'. Once this has finished running, 3 new images will appear in the directory, each of which will be a graph displaying the data from the API. 
