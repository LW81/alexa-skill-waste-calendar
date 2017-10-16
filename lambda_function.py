# -*- coding: utf-8 -*-

import os
import locale
import datetime

if os.name == 'nt':
    locale.setlocale(locale.LC_ALL, 'deu_deu')
else:
    locale.setlocale(locale.LC_ALL, 'de_DE')

# --------------- Main handler ------------------


def lambda_handler(event, context):
    # if (event["session"]["application"]["applicationId"] !=
    #        "[APP_ID]"):
    #        raise ValueError("Invalid Application ID")

    if event["session"]["new"]:
        on_session_started({"requestId": event["request"]["requestId"]}, event["session"])

    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    print ("Starting new session.")


def on_launch(launch_request, session):
    return get_welcome_response()


def on_intent(intent_request, session):
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]

    if intent_name == "GetWaste":
        return get_waste(intent)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    print ("Ending session.")
    # Cleanup goes here...


# --------------- Functions that control the skill's behavior ------------------

def handle_session_end_request():
    card_title = "Müllkalender Hasselroth"
    speech_output = "Bis zum nächsten mal !"
    should_end_session = True

    return build_response({},
                          build_speechlet_response(card_title,
                                                   speech_output,
                                                   None,
                                                   should_end_session))


def get_welcome_response():
    session_attributes = {}
    card_title = "Müllkalender Hasselroth"
    speech_output = "Willkommen zum Müllkalender von Hasselroth. " \
                    "Du kannst mich fragen welche Tonne als nächstes geleert wird, oder " \
                    "an welchem Tag eine bestimmte Tonne geleert wird."
    reprompt_text = "Bitte frage mich, wann das nächste mal eine Tonne geleert wird."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_waste(intent):
    session_attributes = {}
    card_title = "Müllkalender Hasselroth - Nächste Leerung."
    reprompt_text = ""
    should_end_session = True

    tonnen = ["schwarze", "blaue", "gelbe", "braune", "blaue"]

    dates = {
             datetime.date(2017, 2, 6): "gelbe",
             datetime.date(2017, 2, 10): "schwarze",
             datetime.date(2017, 2, 17): "braune",
             datetime.date(2017, 2, 20): "blaue",
             datetime.date(2017, 2, 24): "schwarze",
             datetime.date(2017, 3, 3): "braune",
             datetime.date(2017, 3, 6): "gelbe",
             datetime.date(2017, 3, 10): "schwarze",
             datetime.date(2017, 3, 17): "braune",
             datetime.date(2017, 3, 20): "blaue",
             datetime.date(2017, 3, 24): "schwarze",
             datetime.date(2017, 3, 31): "braune",
             datetime.date(2017, 4, 3): "gelbe",
             datetime.date(2017, 4, 7): "schwarze",
             datetime.date(2017, 4, 7): "schwarze",
             datetime.date(2017, 4, 13): "braune",
             datetime.date(2017, 4, 18): "blaue",
             datetime.date(2017, 4, 21): "schwarze",
             datetime.date(2017, 4, 28): "braune",
             datetime.date(2017, 5, 2): "gelbe",
             datetime.date(2017, 5, 5): "schwarze",
             datetime.date(2017, 5, 12): "braune",
             datetime.date(2017, 5, 15): "blaue",
             datetime.date(2017, 5, 19): "schwarze",
             datetime.date(2017, 5, 26): "braune",
             datetime.date(2017, 5, 29): "gelbe",
             datetime.date(2017, 6, 2): "schwarze",
             datetime.date(2017, 6, 9): "braune",
             datetime.date(2017, 6, 12): "blaue",
             datetime.date(2017, 6, 17): "schwarze",
             datetime.date(2017, 6, 23): "braune",
             datetime.date(2017, 6, 26): "gelbe",
             datetime.date(2017, 6, 30): "schwarze",
             datetime.date(2017, 8, 18): "braune",
             datetime.date(2017, 8, 21): "gelbe",
             datetime.date(2017, 8, 25): "schwarze",
             datetime.date(2017, 9, 1): "braune",
             datetime.date(2017, 9, 4): "blaue",
             datetime.date(2017, 9, 8): "schwarze",
             datetime.date(2017, 9, 15): "braune",
             datetime.date(2017, 9, 18): "gelbe",
             datetime.date(2017, 9, 22): "schwarze",
             datetime.date(2017, 9, 29): "braune",
             datetime.date(2017, 10, 2): "blaue",
             datetime.date(2017, 10, 7): "schwarze",
             datetime.date(2017, 10, 13): "braune",
             datetime.date(2017, 10, 16): "gelbe",
             datetime.date(2017, 10, 20): "schwarze",
             datetime.date(2017, 10, 27): "braune",
             datetime.date(2017, 10, 28): "blaue",
             datetime.date(2017, 11, 3): "schwarze",
             datetime.date(2017, 11, 10): "braune",
             datetime.date(2017, 11, 13): "gelbe",
             datetime.date(2017, 11, 17): "schwarze",
             datetime.date(2017, 11, 24): "braune",
             datetime.date(2017, 11, 27): "blaue",
             datetime.date(2017, 12, 1): "schwarze",
             datetime.date(2017, 12, 8): "braune",
             datetime.date(2017, 12, 11): "gelbe",
             datetime.date(2017, 12, 15): "schwarze",
             datetime.date(2017, 12, 22): "braune",
             datetime.date(2017, 12, 27): "blaue",
             datetime.date(2017, 12, 29): "schwarze",
             }

    today = datetime.date.today()

    if ('value' in intent['slots']['Tonne']) and (intent['slots']['Tonne']['value'] in tonnen):
        query_type = "specific"
        tonne = intent['slots']['Tonne']['value']
    else:
        query_type = "generic"

    for key in sorted(dates.keys()):
            if (key >= today):
                day = key.strftime("%A")
                date = key.strftime("%d. %B")

                # Get the emphasis based on the delta
                if ((key - today).days <= 6) and ((key - today).days > 1):
                    emphasis = "kommenden"
                elif (key - today).days == 1:
                    emphasis = "morgigen"
                elif (key - today).days == 0:
                    emphasis = "heutigen"
                else:
                    emphasis = ""

                # Now we want to see what we have
                if (query_type == "specific") and (dates[key] == tonne):
                    speech_output = "Am %s %s dem %s wird die %s Tonne geleert." % (emphasis,
                                                                                    str(day),
                                                                                    str(date),
                                                                                    tonne)
                    break
                elif (query_type == "generic"):
                    speech_output = "Als nächstes wird am %s %s dem %s die " \
                                    "%s Tonne geleert." % (emphasis,
                                                           str(day),
                                                           str(date),
                                                           dates[key])

                    break

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": output
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt_text
            }
        },
        "shouldEndSession": should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }
