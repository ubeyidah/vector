import os
import sys
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types
from src.config import MEMORY_FILE


class ChatAssistant:
    """
    Manages the Gemini chat session, including initialization,
    history, and streaming responses.
    """

    def __init__(self, model_name: str, system_prompt: str):
        self.model_name = model_name
        self.system_prompt = system_prompt

        try:
            self.client = self._initialize_client()
            self.chat_session = self._create_chat_session()
        except (EnvironmentError, ConnectionError) as e:
            print(f"Startup Error: {e}")
            sys.exit(1)

    def _load_api_key(slef):
        """Loads the api key from .env"""
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise EnvironmentError("Error: GEMINI_API_KEY not found in .env file.")

    def _initialize_client(self):
        """Init the genai.Client."""
        self._load_api_key()
        try:
            return genai.Client()
        except Exception as e:
            raise ConnectionError(f"Error initializing Gemini client: {e}")

    def _create_chat_session(self):
        """creates a new chat session with the system prompt"""
        history = self._load_history()
        gen_config = types.GenerateContentConfig(system_instruction=self.system_prompt)
        print(f"Initializing chat with {self.model_name}...")
        return self.client.chats.create(
            model=self.model_name, config=gen_config, history=history
        )

    def send_message_stream(self, prompt: str):
        """sends a message and yields the response chunks."""
        try:
            res_stream = self.chat_session.send_message_stream(prompt)
            for chunk in res_stream:
                yield chunk.text
        except Exception as e:
            print(f"\n[Stream Error: {e}]")

    def _load_history(self):
        """Loads chat history from the JSON memory file."""
        if not os.path.exists(MEMORY_FILE):
            return []

        try:
            with open(MEMORY_FILE, "r") as f:
                serializable_history = json.load(f)

            print(f"[Memory loaded from {MEMORY_FILE}]")

            # Reconstruct 'types.Content' objects (simplified for text-only)
            loaded_history = []
            for item in serializable_history:
                parts = [
                    types.Part(text=part_data["text"]) for part_data in item["parts"]
                ]
                loaded_history.append(types.Content(role=item["role"], parts=parts))

            return loaded_history

        except Exception as e:
            print(f"Error loading memory: {e}. Starting fresh.")
            return []

    def save_history(self):
        """Saves the current chat history to the JSON memory file."""
        try:
            serializable_history = []
            for content in self.chat_session.history():
                parts_list = [
                    {"text": part.text} for part in content.parts if part.text
                ]

                if parts_list:
                    serializable_history.append(
                        {"role": content.role, "parts": parts_list}
                    )

            with open(MEMORY_FILE, "w") as f:
                json.dump(serializable_history, f, indent=4)

            print(f"\n[Memory saved to {MEMORY_FILE}]")

        except Exception as e:
            print(f"\nError saving memory: {e}")
