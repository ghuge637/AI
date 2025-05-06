pip install chatterbot==1.0.5
pip install chatterbot_corpus

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create chatbot instance
chatbot = ChatBot("QuickShopBot")

# Train chatbot with English corpus data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")

# Start chatbot interaction
print("Welcome to QuickShopBot! Type 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("QuickShopBot: Thank you for visiting! Have a great day. 👋")
        break
    response = chatbot.get_response(user_input)
    print("QuickShopBot:", response)
