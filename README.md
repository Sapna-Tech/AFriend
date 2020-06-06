# A Friend

# SUMBISSION NAME  

A Friend: A WhatsApp chatbot with our inbuild corona tracker application

### Short description:
We have developed a Whatsapp Watson Assistant bot for covid-19 and a inbuilt corona tracker.

#### Long description: 

### What is the problem? 

Currently lot of people in this lockdown period are unaware of correct information. People do not have access to essential services, some are losing jobs and feeling demotivated. This product is a proper destination for all such users, where all information can be accessed. 

### How can technology help? 

Today technology is in the hands of massive amount of people in the form of mobiles. WhatsApp being a very powerful platform can be leveraged in providing assistance to people in need. 

### The idea: 

We ideate to integrate our chat assistance with WhatsApp which can provide all sorts of information to users. Just saving a WhatsApp number in the mobile can provide all sorts of information related to coronavirus and help to develop social wellbeing of the users. 

Developing our inbuild tracker to keep track of cases and statistics in understandable format. Backed by Cloud Foundry Apps, Watson Assistant, DB2, Cloud Object Storage we aspire to build a scalable product. 

### What have we developed?  

A chat assistant integrated with WhatsApp along with covid_19 tracker that will keep human emotional well-being and assist in providing suitable information 

1. Information related to covid-19 statistics  

2. To gear up people who are feeling unmotivated  

3. Providing essential services details  

4. Information for students related to building skills.  

5. Career motivation  

6. Guiding user to our internal corona- tracker application.  

7. This bot will talk, perform various other interacting skills, and provide valid responses to the user to help in this time of crisis.  

This will involve a machine learning model for effective responses which will indeed drive the conversation. 

### The architecture: 

![Architecture](https://covid-19-imageforafriend.s3.jp-tok.cloud-object-storage.appdomain.cloud/architecture.png)

1. The user saves the WhatsApp number. 

2. It types query to get information. 

3. The Twilio interface fetches the information of user mobile number and query and calls Python service. 

4. The Python service checks if the user session is new or old: 

     A) New session: Session id is developed and stored in DB2 with user number 

     B) Old session: The session id is fetched of the user. 

5 .The Python service calls Watson assistant which processes and provides the proper response. 

6. The Watson assistant is trained on our self-made dataset and have provided support of text and images. 

7. The response is provided to Twilio interface which eventually provides the response to user. 

8. The corona-tracker application link is also provided to users. 

9. The Global tracker application provides information such as case counts, statistics in bar graph, single day spike in cases in India and world, links to important resources related to symptom checker, donations, etc. 

10. The chat assistant is integrated in web application as well. 

### Solution roadmap: 

![Roadmap](https://covid-19-imageforafriend.s3.jp-tok.cloud-object-storage.appdomain.cloud/long_road_map.png)

### IBM Cloud Services or IBM Systems Used: 
Cloud Foundry Apps, Watson Assistant, DB2, Cloud Object Storage 

### A Friend Bot: 

1. Bot created at Watson Assistant: Intent, Entities and Dialogue flow 
2. Cloud Object Storage: Storages all data related to Responses which includes images and videos. 
3. DB2 database: Storing session ids  
4. Python Flask Application with Tornado functionality  

Application is made where Watson Assistant APIs were integrated (session and Message). which would maintain a session of users for conversation steadiness. 
Session IDs were linked to Mobile number and the data on runtime gets stored in DB2 database.
This API is linked with WhatsApp (Twilio Interface). 

### Twilio Interface: 

Twilio is a cloud communications platform to perform communication functions and have used it to call WhatsApp web service APIs. 
Node.js program to connect with Python service and WhatsApp.  

### Corona Tracker Application: 

1. Java Spring Boot Application   
2. John Hopkins data set and other open source APIs used to fetch real time data 
3. Serving Web Content with Spring MVC & Thymeleaf 
4. UI: HTML, CSS, JavaScript 

Watson chat assistant integrated on the Home page 

### Future Plans: 

1. Improve bot on IBM Assistant by improving and augmenting the dataset
2. Connect with various NGOs, Social Reformers and other services to be a part of our chatbot which will make our chatbot a central platform
3. Give Strong database functionalities 
4. Explore for all type of emotion detection
5. Expand to more calamities in order to make it scalable
6. Make a platform where information on any calamities and help at any time can be provided

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

1. Python
2. Java8

### Make IBM Account
[IBM Cloud account](https://console.ng.bluemix.net/registration/)

### Make a bot on IBM Watson Assitant
[IBM WATSON ASSISTANT](https://www.ibm.com/watson/how-to-build-a-chatbot)

### Create DB2
[DB2 DATABASE](https://cloud.ibm.com/docs/Db2onCloud?topic=Db2onCloud-getting-started)

### Make Twilio Account
[TWILIO ACCOUNT](https://www.twilio.com/blog/what-does-twilio-do)

# Add to config
1. coronavirus-bot
  
  a. Go to coronavirus-bot--->config--->config.json
    1. Add Basic Auth details(user can define) 
    2. Add all details that you get after creating IBM Watson Assitant in session and predict config
    3. Add all details regarding DB2 in db config
    4. Create table on IBM dashbord by adding anisession.text

2. Twilio
  
    a. All details regarding coronavirus(predict API) in whatsapp.js
    b. Copy this code to your twilio Account (Function--->Make API--->Copy the code)

### Set up python environment - coronavirus-bot:
Go to the folder, (pyCharm)
pip install -r requirements.txt

### Set up java environment - coronavirus-investigator :
git clone <GIT_URL>
Open in Spring tool Suite (IntelliJ)
mvn clean
mvn install

### Run command:
Go to the folder

1. coronavirus-bot
  a. cd coronavirus-bot/IBMBOT
  b. nohup python Inference.py

2. coronavirus-investigator
  a. cd /coronavirus-investigator/target &
  b. nohup java jar coronavirus-investigator-0.0.6-SNAPSHOT.jar & 
