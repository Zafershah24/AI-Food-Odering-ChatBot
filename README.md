# Yoyo-AI-pizzaBot

# STEPS TO FOLLOW FOR RUNNING THE YOYO PIZZA CHATBOT.

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
