import utilities

def handle_etiquette_intent(parameters):
    pass


def handle_food_generic_intent(parameters):
    demonym = parameters.get("Demonym")
    demonym = demonym.lower()
    wiki_search_text = demonym + "_culture"
    wiki_summary = utilities.get_wikipedia_summary(wiki_search_text)
    return utilities.generate_response_payload(wiki_summary)


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