# Health Management - Anomaly Detection and Classification
---

<br/>
<div>
  
  ![ntnu_bredde_eng](https://user-images.githubusercontent.com/44703456/222424176-cb7248c2-33d5-49cd-8e0c-742bab24c4c1.png)

</div>
<br/>

## About
This repository contains the code which were produced for a bachelor project at the <a href="https://www.ntnu.edu">Norwegian University of Science and Technology</a> (NTNU) during the spring of 2024. 
The project was conducted by three students at the computer science bachelor programme.
Authors:
* Jørgen Finsveen - <a href="https://github.com/jorgenfinsveen">jorgenfinsveen</a>
* Harald Wangsvik Fredriksen - <a href="https://github.com/Haraldwangsvik">haraldwangsvik</a>
* Even Johan Pereira Haslerud - <a href="https://github.com/ejhasler">ejhasler</a>
<br/>
Supervisors:

* <a href="https://www.ntnu.edu/employees/alaliyat.a.saleh">Saleh Abdel-Afou Alaliyat</a>
* <a href="https://www.ntnu.edu/employees/muhammad.u.hassan">Muhammad Umair Hassan</a>
<br/>
The project addresses a machine learning approach for anomaly detection and classification for engines in marine vessels on behalf of <a href="https://www.kongsberg.com/maritime/">Kongsberg Maritime</a>. Five LSTM models targeting different subsystems in a ship engine were made.
All models predicts certain attributes in each subsystem based on other attributes. The idea was that anomalies could be detected by comparing the predicted state of these attributes with the actual state, where a significant difference in
these two would indicate anomalies. Classification was not conducted in this project due to lack of data.

<br/><br/>

![kongsberg_maritime_logo](https://coveocean.com/wp-content/uploads/2023/05/KONGSBERG_logo_horisontal_BW_neg.png)

<br/>

## Structure
This repository contains some documentation such as cooperation agreement, project proposal and description of labels in the dataset. 
Furthermore, the repository contains scalers, exported models, and Jupyter Notebook files which were used to train the models.

## Datasets
Note that the models are already trained, and that it is not possible to run the scripts or make predictions. This is because the datasets given to the group by Kongsberg Maritime contains sensitive information, and it was agreed upon
that these were not to be included in this repository.

## Models
All models are Long Short-Term Memory models which in this project has been used for supervised machine learning. The scripts were made using <a href="https://jupyter.org">Jupyter Notebook</a> in 
<a href="https://colab.research.google.com">Google Colab</a> using <a href="https://www.python.org">Python</a>. There are five different models trained, which are located in the 
<a href="https://github.com/Bachelor-9/anomaly-detection/tree/master/colab">colab</a> directory. The trained models has also been exported to .h5 files, and are located in the 
<a href="https://github.com/Bachelor-9/anomaly-detection/tree/master/models">models</a> directory.

## Google Colab
The project was not under version control. This repository only contains the final results achieved in this project. The project in its entirety was conducted using <a href="https://colab.research.google.com">Google Colab</a>, 
which replaced the need for version control. All files, including datasets and model scripts, were stored and regularly updated in <a href="https://www.google.com/drive/">Google Drive</a>, which is the default solution when working 
with Google Colab. It is therefore not possible to inspect the groups progress, issues or other information by looking at this repository, due to this repository only contains the final results. 

## Project Management
In order to see how the project was conducted, including sprint reports, issue-tracking, meeting notices, etc. Please refer to the following pages:
* Atlassian Jira - <a href="https://jira.iir.ntnu.no/projects/HMADC">Homepage</a>
* Atlassian Confluence - <a href="https://confluence.iir.ntnu.no/display/HMADC">Homepage</a>
<br/>
Note, in order to visit these webpages, it may be necessary to be granted access by NTNU.
