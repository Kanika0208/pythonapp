Hello,

This is readme file for Python, Flask and Mysql app.

-We installed minikube and kubectl
 
>>minikube start --memory=3000mb
>>kubectl get nodes

There are three files in App directory front2.py, requirements.txt and docker file.

Front2.py has two route:
1. / -  shows Ilcome page 
2. /read - shows the data from database(in our case mysql)

Requirements.txt - will install both the connectors flask and sql

Then I build this code using docker and we have our docker file for that
To build docker, we need to run following commands:

- docker build -t kanika02/python:v1 .
- docker push kanika02/apprepo:v1

Thats how I got the image, I took this image url and put it in our deployment file of python 
and I are using base mysql image for sql deployment.



YAML Directory:

mysql.yaml - for mysql deployment, volume, pv and pvc
sqlsecrets- to create secret for our DB password 
python.yaml - for python deployment

HELM:
Python Chart:

I installed helm v3.0, so it doesnt require any tiller account.
I created helm chart for our deployments using below commands:

- helm create pythonchart
This will create a pythonchart directory which contains templates dir in which we have
mentioned all the yaml files and helper.tpl file which has templates defined 
which we have used in our deployment.yaml and some values are fetching from values.yaml

-Firstly, we create a namespace for our deployment:

>>>kubectl create namespace ame

>> helm install -name python pythonchart

- To check all the pods and db are running we need to run following commands:
>>> kubectl get po --namespace ame
>>> kubectl get svc --namespace ame
>>> kubectl get pvc --namespace ame
>>> kubectl get pv --namespace ame

EXEC into the sql pod, create a table and insert into table.
>>>kubectl exec -it --namespace ame python-pythonchart-mysql-7cb9698d95-j4fkb /bin/bash
Note: Change the pod name by the newly generated sql pod name

Run the mysql query in it:

>>mysql -u webuser-h localhost -p password123

>>CREATE TABLE `webapp`.`employee` (   `id` int NOT NULL,   `name` varchar(50) NOT NULL,   PRIMARY KEY (`id`) );

>>INSERT INTO `webapp`.`employee` VALUES (1,'hi');

exit from sql
exit from pod

We can now run minikube command to check our application.

>>minikube service python-pythonchart-app --namespace ame

This will open Welcome page

To check the db page put /read at the end of the url. It will show the DB data











