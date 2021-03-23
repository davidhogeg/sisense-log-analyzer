# sisense-log-analyzer

## Installation

1. Open the Sisense Web application.
2. In the Admin tab, click **"Feature Management"** and enable **"Custom Code"**
![image](https://user-images.githubusercontent.com/81238182/112159139-31799c80-8bbf-11eb-8265-e2c5fd1d7bfb.png)

3. Open a web browser and navigate to https://<Your Sisense URL>/app/diag/tree/work/storage_notebooks/custom_code_notebooks/notebooks
4. Create a new folder named **"LogAnalyzerNotebook"**.
![image](https://user-images.githubusercontent.com/81238182/112159706-d300ee00-8bbf-11eb-8a14-e390884694f2.png)

5. Open the "LogAnalyzerNotebook" folder and upload the following files:
- LogAnalyzerNotebook_new.ipynb
- expression.yaml
- functions.py
- LogAnalyzerNotebook.json
- patterns.yaml

6. Open the Sisense Wep application and go to the Data tab.
7. Click on **"Import Model"** and import the **"Logs Analysis.smodel"** file.
![image](https://user-images.githubusercontent.com/81238182/112160883-fc6e4980-8bc0-11eb-8ed1-ed73a0702ee4.png)

8. Open the imported model and click **"Build"** to build the model.
9. Open the **"Analytics"** tab then click **"+"** > **"Import Dashboard**.
![image](https://user-images.githubusercontent.com/81238182/112161771-d4331a80-8bc1-11eb-90e0-af6f6aedc35b.png)

10. Import the **"LogAnalysis.dash"** dashboard. 



