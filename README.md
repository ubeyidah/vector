# Vector

A personal, streaming AI assistant built with Python and the Gemini API.

## Features

- **Streaming:** Responses appear word-by-word.
- **Memory:** Remembers the conversation history (session-only for now).
- **Persona:** Has a defined personality via a system prompt.

---

## Setup

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/ubeyidah/vector.git
    cd vector
    ```

2.  **Create Virtual Environment:**

    ```bash
    uv venv
    ```

3.  **Activate Environment:**

    - On macOS/Linux:
      ```bash
      source .venv/bin/activate
      ```
    - On Windows (PowerShell):
      ```bash
      .venv\Scripts\Activate.ps1
      ```

4.  **Install Packages:**

    ```bash
    uv pip install -r requirements.txt
    ```

5.  **Create `.env` File:**
    You need to provide your API key. Copy the example file:
    ```bash
    cp .env.example .env
    ```
    Now, open the `.env` file and paste in your secret API key.

---

## Run

Once everything is installed, just run `main.py`:

```bash
python main.py
```
