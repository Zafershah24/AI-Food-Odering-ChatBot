from typing import Any, Text, Dict, List




from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType, Form
from rasa_sdk.executor import CollectingDispatcher
# from database import DataUpdate1,DataUpdate2
import requests
import random

from rasa_sdk.forms import FormAction




class ActionOrderId(Action):
    def name(self) -> Text:
        return "action_order_id"

    async def run(
    self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        order_id=tracker.sender_id
        dispatcher.utter_message("Your Order Number is {}".format(order_id))
        return []
    

# class ActionFormInfoPizza(Action):
#     def name(self) -> Text:
#         return "form_info_pizza"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         required_slots = ["food","size","topping","crust_type","quantity","name"]

#         for slot_name in required_slots:
#             if tracker.slots.get(slot_name) is None:
#                 # The slot is not filled yet. Request the user to fill this slot next.
#                 return [SlotSet("requested_slot", slot_name)]

#         # All slots are filled.
#         return [SlotSet("requested_slot", None)]

# class ActionSubmitPizza(Action):
#     def name(self) -> Text:
#         return "action_submit_pizza"

#     def run(
#         self,
#         dispatcher,
#         tracker: Tracker,
#         domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_food", quantity=tracker.get_slot('quantity'),size=tracker.get_slot('size'),food=tracker.get_slot('food'),topping=tracker.get_slot('topping'),
#                                  crust_type=tracker.get_slot('crust_type'))

        
# class ActionFormInfoSide(Action):
#     def name(self) -> Text:
#         return "form_info_side"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         required_slots = ["side","quantity","name"]

#         for slot_name in required_slots:
#             if tracker.slots.get(slot_name) is None:
#                 # The slot is not filled yet. Request the user to fill this slot next.
#                 return [SlotSet("requested_slot", slot_name)]

#         # All slots are filled.
#         return [SlotSet("requested_slot", None)]

# class ActionSubmitSide(Action):
#     def name(self) -> Text:
#         return "action_submit_side"

#     def run(
#         self,
#         dispatcher,
#         tracker: Tracker,
#         domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_sideorder", quantity=tracker.get_slot('quantity'),side=tracker.get_slot('side')
    
                             
        

class ActionFormInfoPizza(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_info_pizza"

    @staticmethod
    def required_slots(tracker: Tracker): 
    # -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["food","size","topping","crust_type","quantity","name","number"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) :
    # -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_thanks", name=tracker.get_slot('name'),
                                 order=tracker.sender_id)
        dispatcher.utter_message(template="utter_food", quantity=tracker.get_slot('quantity'),size=tracker.get_slot('size'),food=tracker.get_slot('food'),topping=tracker.get_slot('topping'),
                                 crust_type=tracker.get_slot('crust_type'))
        # DataUpdate1(tracker.get_slot('name'),tracker.get_slot('number'),tracker.get_slot('vegpizza'),
        #            tracker.get_slot('nvegpizza'),tracker.get_slot('size'),tracker.get_slot('topping'),
        #            tracker.get_slot('crust_type'),tracker.get_slot('quantity'))
        return []

    def slot_mappings(self):
    # -> Dict[Text,Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "name": [self.from_entity(entity="name", intent='provide_name'),
                     self.from_text()],
            "food": [self.from_entity(entity="food", intent="food"),
                        self.from_text()],
            "size": [self.from_entity(entity="size", intent="psize"),
                        self.from_text()],
            "topping": [self.from_entity(entity="topping", intent="ptopping"),
                        self.from_text()],
            "crust_type": [self.from_entity(entity="crust_type", intent="pcrust"),
                        self.from_text()],
            "quantity": [self.from_entity(entity="quantity", intent="pquantity"),
                        self.from_text()],
            "number": [self.from_entity(entity="number", intent="provide_number"),
                        self.from_text()],
        }
        
        

class ActionFormInfoSide(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_info_side"

    @staticmethod
    def required_slots(tracker: Tracker) :
    # -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["side","quantity","name","number"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) :
    # -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_thanks", name=tracker.get_slot('name'),
                                 order=tracker.sender_id)

        dispatcher.utter_message(template="utter_sideorder", quantity=tracker.get_slot('quantity'),side=tracker.get_slot('side'))
                                 
        # DataUpdate2(tracker.get_slot('name'),tracker.get_slot('number'),tracker.get_slot('side'),
        #            )
        return []




    def slot_mappings(self):
    # -> Dict[Text,Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "name": [self.from_entity(entity="name", intent='provide_name'),
                     self.from_text()],
            "quantity": [self.from_entity(entity="quantity", intent="pquantity"),
                        self.from_text()],
            "side": [self.from_entity(entity="side", intent="order_side_menu"),
                        self.from_text()],
            "number": [self.from_entity(entity="number", intent="provide_number"),
                        self.from_text()],
        }