"""Interactive Django management command for chatting with CampusBot."""

from django.core.management.base import BaseCommand

from chatbot_app.services import create_chatbot


class Command(BaseCommand):
    """Run an interactive conversation in the terminal."""

    help = "Start the ChatterBot terminal client."

    def add_arguments(self, parser) -> None:
        """Add an option to skip training when the database already exists."""
        parser.add_argument(
            "--no-train",
            action="store_true",
            help="Start without retraining the chatbot.",
        )

    def handle(self, *args, **options) -> None:
        """Read messages until the user enters exit or quit."""
        self.stdout.write(self.style.SUCCESS("CampusBot terminal client"))
        self.stdout.write("Training the bot..." if not options["no_train"] else "Loading the bot...")

        bot = create_chatbot(train=not options["no_train"])

        self.stdout.write(self.style.SUCCESS("Ready! Type 'exit' or 'quit' to stop.\n"))

        while True:
            try:
                user_message = input("user: ").strip()
            except (EOFError, KeyboardInterrupt):
                self.stdout.write("\nbot: Goodbye! Have a great day.")
                break

            if not user_message:
                self.stdout.write("bot: Please enter a message.")
                continue

            if user_message.casefold() in {"exit", "quit"}:
                self.stdout.write("bot: Goodbye! Have a great day.")
                break

            response = bot.get_response(user_message)
            self.stdout.write(f"bot: {response}")
