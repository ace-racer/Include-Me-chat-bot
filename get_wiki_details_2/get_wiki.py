import wikipedia
import json
import boto3

DISAMBIGUATION_KEYWORDS = []

def get_wiki_response(event, context):
    print("Event: " + str(event))
    event_body = event.get("body")
    wiki_summary = ""
    if event_body is not None:
        print(event_body)
        if isinstance(event_body, str):
            event_body = json.loads(event_body)

        query_result = event_body.get("queryResult")
        parameters = query_result.get("parameters")
        if parameters:
            demonym = parameters.get("Demonym")
            demonym = demonym.lower()
            wiki_search_text = demonym + "_culture"
            wiki_summary = get_wikipedia_summary(wiki_search_text)
            print(wiki_summary)
    
    response_payload = generate_response_payload(wiki_summary)
    response = {}
    response["statusCode"] = 200
    response["headers"] = { "Access-Control-Allow-Origin": "*" }
    response["body"] = json.dumps(response_payload)
    response["isBase64Encoded"] = False
    return response
            


def get_wikipedia_summary(text, level=2):
        if text and level > 0:
            try:
                wiki_summary = wikipedia.summary(text)
                return wiki_summary
            except wikipedia.exceptions.DisambiguationError as disambiguationError:
                print("Disambiguation in Wikipedia occurred for {0}".format(text))
            except Exception as ex:
                print("An error occurred while trying to retrieve details from Wikipedia for {0}. Error details: {1}".format(text, str(ex)))

        return None

def generate_response_payload(summary_text):
    if summary_text:
        response = { "fulfillmentText": "Here is what I found from Wikipedia: " + summary_text }
        return (response)
    return ""