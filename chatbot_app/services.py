"""Chatbot construction and training services."""

from chatterbot import ChatBot
from chatterbot.tagging import LowercaseTagger
from chatterbot.trainers import ListTrainer
from django.conf import settings


TRAINING_CONVERSATIONS = [
    [
        "Good morning! How are you doing?",
        "I am doing very well, thank you for asking.",
        "You're welcome.",
        "Do you like hats?",
    ],
    [
        "Hello",
        "Hello! How can I help you today?",
        "What is your name?",
        "My name is CampusBot.",
    ],
    [
        "What can you do?",
        "I can have a conversation and learn from the examples used to train me.",
        "How do you learn?",
        "I compare your message with known statements and choose a related response.",
    ],
    [
        "Thank you",
        "You are welcome!",
        "Goodbye",
        "Goodbye! Have a great day.",
    ],
]


def create_chatbot(train: bool = True) -> ChatBot:
    """Create CampusBot and optionally train it with known conversations."""
    bot = ChatBot(
        "CampusBot",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        database_uri=settings.CHATTERBOT_DATABASE_URI,
        tagger=LowercaseTagger,
        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch",
                "default_response": "I am still learning. Could you rephrase that?",
                "maximum_similarity_threshold": 0.90,
            }
        ],
        preprocessors=["chatterbot.preprocessors.clean_whitespace"],
    )

    if train:
        trainer = ListTrainer(bot, show_training_progress=False)
        for conversation in TRAINING_CONVERSATIONS:
            trainer.train(conversation)

    return bot
