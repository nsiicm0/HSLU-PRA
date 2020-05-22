# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher

from typing import Any, Dict, List, Text, Union, Optional

class ChangeForm(FormAction):
    """Collects change information"""

    def name(self):
        return "change_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "setting",
            "direction",
            "amount"
        ]
    
    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict]:
        dispatcher.utter_template('utter_submit', tracker)
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "setting": [
                self.from_entity(
                    entity="setting", intent=["inform", "serve"]
                ),
            ],
            "direction": [
                self.from_entity(
                    entity="direction", intent=["inform", "serve"]
                ),
            ],
            "amount": [
                self.from_entity(
                    entity="amount", intent=["inform", "serve"]
                ),
            ],
        }