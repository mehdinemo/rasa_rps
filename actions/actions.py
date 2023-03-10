from typing import Any, Text, Dict, List
import random
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionPlayRPC(Action):

    def name(self) -> Text:
        return 'action_play_rps'

    def computer_choice(self):
        generatednum = random.randint(1, 3)
        computerchoice = ''
        if generatednum == 1:
            computerchoice = 'rock'
        elif generatednum == 2:
            computerchoice = 'paper'
        elif generatednum == 3:
            computerchoice = 'scissors'

        return (computerchoice)

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_choice = tracker.get_slot("choice")
        dispatcher.utter_message(text=f'you chose {user_choice}')
        comp_choice = self.computer_choice()
        dispatcher.utter_message(text=f'the computer chose {comp_choice}')

        if user_choice == 'rock' and comp_choice == 'scissors':
            dispatcher.utter_message(text='Congrats, you won!')
        elif user_choice == 'rock' and comp_choice == 'paper':
            dispatcher.utter_message(text='The computer won this round.')
        elif user_choice == 'paper' and comp_choice == 'scissors':
            dispatcher.utter_message(text='The computer won this round.')
        elif user_choice == 'paper' and comp_choice == 'rock':
            dispatcher.utter_message(text='Congrats, you won!')
        elif user_choice == 'scissors' and comp_choice == 'rock':
            dispatcher.utter_message(text='The computer won this round.')
        elif user_choice == 'scissors' and comp_choice == 'paper':
            dispatcher.utter_message(text='Congrats, you won!')
        else:
            dispatcher.utter_message(text='It was a tie!')

        return []