# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import logging

class ActionLicences(Action):

     def name(self) -> Text:
         return "action_licences"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         logging.info("action_licences")
         
         dispatcher.utter_message(text="Aqui está o preço para 100 licenças de Jira: R$ 145.000,00")
         dispatcher.utter_message(text="Internamente abrimos um chamado para que possamos gerar uma quote. Normalmente este processo leva 24h e assim que tivermos pronto enviaremos ao seu e-mail.")

         return []
