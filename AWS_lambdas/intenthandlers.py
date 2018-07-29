import utilities

KNOW_MORE = "Know More"

def handle_etiquette_intent(parameters):
    demonym = parameters.get("Demonym")
    demonym = demonym.lower()
    parameter_two = parameters.get("Acceptablepractices_Casual")
    parameter_three = parameters.get("Acceptablepractices_respect")
    
    western = ("british", "american", "french")
    eastern = ("indian", "chinese", "japanese")
    image_url = ""
    more_url = ""
    if demonym in western:
        if parameter_two:
            text_response = "It is an acceptable practice"
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Handshake_%28Workshop_Cologne_%2706%29.jpeg/220px-Handshake_%28Workshop_Cologne_%2706%29.jpeg"
            more_url = "https://www.youtube.com/watch?v=x2dGVrOtDtw"
        else:
            text_response = "It is not an acceptable practice"
    if demonym in eastern:
        if parameter_three:
            text_response = "It is an acceptable practice"
            image_url = "https://www.tripsavvy.com/thmb/tfN5t_RfvGpuMy2RKdD1ETc2tuo=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/japanese-bow-56787ce95f9b586a9e6f2904.jpg"
            more_url = "https://www.youtube.com/watch?v=ytmdQC6OxPU"
        else:
            text_response = "It is not an acceptable practice"
    
    fulfillment_messages = []
    if image_url or more_url:
        fulfillment_message = {}
        fulfillment_message["card"] = {}
        fulfillment_message["card"]["title"] = text_response
        fulfillment_message["card"]["imageUri"] = image_url
        fulfillment_message["card"]["buttons"] = []
        fulfillment_message["card"]["buttons"].append(
            {
                "text": KNOW_MORE,
                "postback": more_url
            }
        )

        fulfillment_messages.append(fulfillment_message)
    return utilities.generate_response_payload(text_response, fulfillment_messages)


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
    fulfillment_messages = []
    fulfillment_message = {}
    fulfillment_message["card"] = {}
    fulfillment_message["card"]["title"] = response
    fulfillment_message["card"]["buttons"] = []
    fulfillment_message["card"]["buttons"].append(
         {
            "text": KNOW_MORE,
            "postback": "https://www.youtube.com/watch?v=2Qs0EL6JWD0"
          }
    )

    fulfillment_messages.append(fulfillment_message)
    return utilities.generate_response_payload(response, fulfillment_messages)


def handle_company_stats(parameters):
    d={"china": 25, "India": 50, "Singapore": 40}
    country = parameters.get("sys.geo-country")
    text_response = str(d[country])+"%" + "Female"
    return utilities.generate_response_payload(text_response)

def handle_work_environment_intent(parameters):
    demonym = parameters.get("Demonym")
    country = parameters.get("geo-country")
    work_culture = parameters.get("Workculture").lower()
    
    if demonym is not None:
        x=demonym
    else:
        x=country
    
    demonym = demonym.lower() if demonym is not None else 'no demonym'
    country = country.lower() if country is not None else 'no country'
    
    if demonym in ("british","french") or country in ("england","france"):
        if work_culture == "environment":
            response = "The "+x+ "office is usually quiet with people focussing on their work alone"
        elif work_culture == "workplace eating customs":
            response = "People usually eat alone often at their desks. While for tea break they may go out in small groups of 2"
        elif work_culture == "collaboration":
            response = "People prefer to work independently and then collaborate to integrate their results"
    elif demonym in ("chinese","japanese") or country in ("china", "japan"):
        if work_culture == "environment":
            response = "The "+x+ "office is usually quiet"
        elif work_culture == "workplace eating customs":
            response = "People usually eat together atleast in groups of 2. Same is true for tea."
        elif work_culture == "collaboration":
            response = "People tend to work together and discuss solutions 30% of their time, while the remaining time they utilise to work independently"
    elif demonym == "indian" or country == "india":
        if work_culture == "environment":
            response = "The "+x+ "office is realively louder as people tend to interact and collaborate more often"
        elif work_culture == "workplace eating customs":
            response = "People usually eat together in groups (ranging from 2 to 8 people). Same is true for tea breaks."
        elif work_culture == "collaboration":
            response = "People often collaborate & discuss while working"
    return utilities.generate_response_payload(response)
