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
    pass

def handle_weather_intent(parameters):
    pass

def handle_work_environment_intent(parameters):
    pass