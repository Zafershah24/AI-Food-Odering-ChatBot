# VIDEO DEMONSTRATION OF THE CHATBOT.
![Video-Demonstration-of-the-Worki](https://user-images.githubusercontent.com/32811341/105641064-23055200-5ea8-11eb-8a54-a6d1d5235c1a.gif)

# STEPS TO FOLLOW FOR RUNNING THE AI PIZZA CHATBOT.

1) Download "AI" Folder in your Local Directory, then Open The COMMAND PROMPT(CMD).
2) cd AI
3) python3 -m venv myvenv      (creating Environment Variable)
4) myvenv\Scripts\activate      (for Windows machine)
5) python -m pip install --upgrade pip
6) pip install rasa         (installing RASA library) 

# After Completing the Above Steps, run the below commands to test the chatbot -

7) cd pizzaBot
8) rasa shell (in One Terminal)

# Open ANOTHER CMD Terminal and run the Following Commands-  (to run the BACKEND SERVER)

9) cd AI
10) myvenv\Scripts\activate  
11) cd pizzaBot
12) rasa run actions


# Now the BOT can Successfully Interact with its Backend.

# Architecture of the ChatBot
![Screenshot (228)](https://user-images.githubusercontent.com/32811341/105641149-94dd9b80-5ea8-11eb-81f7-4c0d55023ce6.png)
