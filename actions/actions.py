from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionPlayRPC(Action):

    def name(self) -> Text:
        return 'action_send_request'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_cartoon = tracker.get_slot("cartoon")
        user_background = tracker.get_slot("background")
        user_face = tracker.get_slot("face")

        dispatcher.utter_message(text=f'you chose {user_cartoon}')
        dispatcher.utter_message(text=f'you chose {user_background}')
        dispatcher.utter_message(text=f'you chose {user_face}')

        return []
