*** IncludeMe - A Slack chatbot to answer your diversity questions without the fear of being judged! ***

** Components and how to integrate: **

  a. The bot is powered by Google dialog flow. Please refer [here](https://dialogflow.com/) for details. 
  b. The Anon.zip contains the required files to recreate the bot in Google dialog flow. This ZIP can be imported following the steps mentioned [here](https://dialogflow.com/docs/best-practices/import-export-for-versions).
  c. Integrations with third party applications is achieved via AWS lambdas, details of which can be found [here](https://aws.amazon.com/lambda/features/).
  d. The utilities.zip inside contains the ZIP package that will be input to recreate AWS lambda which are used to serve the fulfillments.
  e. The AWS lambda needs to be deployed via [AWS API gateway](https://aws.amazon.com/api-gateway/) to expose the API endpoint.
  f. The endpoint for the API needs to be updated as the fulfillment URL in the Google Dialog flow console.


** Description of the code files: **
The files inside AWS_lambdas contains the following:
  a. ```get_fulfillment.py```: Contains the code to route the intent to the fulfillment based on the intent name
  b. ```intenthandlers.py```: This file contains the code for handling the fulfillment of the various intents including integrations with Wikipedia, internal databases, etc.
  c. ```utilities.py```: This file contains utility code that is used in multiple places in the ```intenthandlers.py```
