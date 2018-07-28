import wikipedia

def get_wikipedia_summary(text, level=2):
        if text and level > 0:
            try:
                wiki_summary = "Here is what I found from Wikipedia: " + wikipedia.summary(text)
                return wiki_summary
            except wikipedia.exceptions.DisambiguationError as disambiguationError:
                print("Disambiguation in Wikipedia occurred for {0}".format(text))
            except Exception as ex:
                print("An error occurred while trying to retrieve details from Wikipedia for {0}. Error details: {1}".format(text, str(ex)))

        return None

def generate_response_payload(fulfil_text, fulfil_messages = "", source = "", payload = ""):
    response = {}
    if fulfil_text:
        response["fulfillmentText"] = fulfil_text 
    if fulfil_messages:
        response["fulfillmentMessages"] = fulfil_messages
    if source:
        response["source"] = source
    if payload:
        response["payload"] = payload
    return (response)

#demonym = parameters.get("Demonym")
#country = parameters.get("geo-country")
#food = parameters.get("Food")
#officetime = parameters.get("OfficeTime")
#religious_practices = parameters.get("Religiouspractices")
#work_culture = parameters.get("Workculture")
#acceptable_practices = parameters.get("Acceptablepractices")