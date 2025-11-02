from src.config import (
    ASSISTANT_NAME,
    MODEL_NAME,
    USER_NAME,
    SYSTEM_PROMPT,
    EXIT_WORD_LIST,
)
from src.assistant import ChatAssistant


def run_terminal_chat():
    """
    The main function to run the terminal-based chat UI.

    This function is now only responsible for:
    1. Setting up the assistant instance.
    2. Running the command-line input/output loop.
    """
    assistant = ChatAssistant(MODEL_NAME, SYSTEM_PROMPT)
    print(f"{ASSISTANT_NAME} is online. Type 'exit' or 'quit' to end.")

    while True:
        try:
            user_prompt = input(f"{USER_NAME}: ")
            if user_prompt.lower() in EXIT_WORD_LIST:
                print(f"Goodbye from {ASSISTANT_NAME}!")
                break
            print(f"{ASSISTANT_NAME}: ", end="", flush=True)
            for chunk in assistant.send_message_stream(user_prompt):
                print(chunk, end="", flush=True)
            print()
        except Exception as e:
            print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    run_terminal_chat()
