***IncludeMe - A Slack chatbot to answer your diversity questions without the fear of being judged!***

Team members: 
1. Anurag Chatterjee [LinkedIn](https://www.linkedin.com/in/anurag-chatterjee/)
2. Apurv Garg [LinkedIn](https://www.linkedin.com/in/apurv-garg-49659274/)
3. Kapil Shukla [LinkedIn](https://www.linkedin.com/in/kapil-shukla-519bb47/)
4. Rajiv Hemanth [LinkedIn](https://www.linkedin.com/in/rajiv-hemanth-07878411/) 
5. Zaira Hossain [LinkedIn](https://www.linkedin.com/in/zaira-hossain-6454308b/)

**Components and how to integrate:**

  1. The bot is powered by Google dialog flow. Please refer [here](https://dialogflow.com/) for details. 
  2. The Anon.zip contains the required files to recreate the bot in Google dialog flow. This ZIP can be imported following the steps mentioned [here](https://dialogflow.com/docs/best-practices/import-export-for-versions).
  3. Integrations with third party applications is achieved via AWS lambdas, details of which can be found [here](https://aws.amazon.com/lambda/features/).
  4. The utilities.zip inside contains the ZIP package that will be input to recreate AWS lambda which are used to serve the fulfillments.
  5. The AWS lambda needs to be deployed via [AWS API gateway](https://aws.amazon.com/api-gateway/) to expose the API endpoint.
  6. The endpoint for the API needs to be updated as the fulfillment URL in the Google Dialog flow console.


**Description of the code files:**
The files inside AWS_lambdas contains the following:
  1. ```get_fulfillment.py```: Contains the code to route the intent to the fulfillment based on the intent name
  2. ```intenthandlers.py```: This file contains the code for handling the fulfillment of the various intents including integrations with Wikipedia, internal databases, etc.
  3. ```utilities.py```: This file contains utility code that is used in multiple places in the ```intenthandlers.py```
