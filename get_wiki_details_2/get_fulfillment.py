
import json
import boto3
import intenthandlers
import utilities

def fulfill_response(event, context):
    print("Event: " + str(event))
    event_body = event.get("body")
    response_payload = ""
    if event_body is not None:
        print(event_body)
        if isinstance(event_body, str):
            event_body = json.loads(event_body)

        query_result = event_body.get("queryResult")
        parameters = query_result.get("parameters")
        intent = query_result.get("intent")
        if intent:
            intent_display_name = intent.get("displayName")
            if intent_display_name == "Food Generic":
                response_payload = intenthandlers.handle_food_generic_intent(parameters)
            elif intent_display_name == "Etiquette":
                response_payload = intenthandlers.handle_etiquette_intent(parameters)
            elif intent_display_name == "Religiouspractices":
                response_payload = intenthandlers.handle_religious_practices_intent(parameters)
            elif intent_display_name == "Timings":
                response_payload = intenthandlers.handle_time_intent(parameters)
            elif intent_display_name == "Weather":
                response_payload = intenthandlers.handle_weather_intent(parameters)
            elif intent_display_name == "Work Environment":
                response_payload = intenthandlers.handle_work_environment_intent(parameters)      
    
    response = {}
    response["statusCode"] = 200
    response["headers"] = { "Access-Control-Allow-Origin": "*" }
    response["body"] = json.dumps(response_payload)
    response["isBase64Encoded"] = False
    return response