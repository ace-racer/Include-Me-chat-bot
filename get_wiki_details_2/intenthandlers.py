import utilities

def handle_etiquette_intent(parameters):
    pass


def handle_food_generic_intent(parameters):
    demonym = parameters.get("Demonym")
    demonym = demonym.lower()
    wiki_search_text = demonym + "_cuisine"
    url, title, summary, image = utilities.get_wikipedia_summary(wiki_search_text)
    fulfillment_messages = []
    fulfillment_message = {}
    fulfillment_message["card"] = {}
    fulfillment_message["card"]["title"] = title
    fulfillment_message["card"]["imageUri"] = image
    fulfillment_message["card"]["buttons"] = []
    fulfillment_message["card"]["buttons"].append(
         {
            "text": title,
            "postback": url
          }
    )

    fulfillment_messages.append(fulfillment_message)

    return utilities.generate_response_payload(summary, fulfillment_messages)


def handle_languages_intent(parameters):
    pass

def handle_religious_practices_intent(parameters):
    pass

def handle_time_intent(parameters):
    demonym = parameters.get("Demonym")
    country = parameters.get("geo-country")
    
    demonym = demonym.lower() if demonym is not None else 'no demonym'
    country = country.lower() if country is not None else 'no country'
    if demonym in ("british","french") or country in ("england","france"):
        response = "The normal working hours are 9:00am - 5:00pm. People very rarely work after office hours."
    elif demonym in ("chinese","japanese") or country in ("china", "japan"):
        response = "The normal working hours are 8:00am - 5:00pm. People very rarely work after office hours only on encountering high severity live incidents."
    elif demonym == "indian" or country == "india":
        response = "The normal working hours are 9:00am - 6:00pm. Though, people do tend to flex their working hours subject their work load and availability"
    return utilities.generate_response_payload(response)


def handle_weather_intent(parameters):
    pass

def handle_work_environment_intent(parameters):
    pass