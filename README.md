# Demo Vibe Coding 🚀

This repository contains a demonstration of Vibe Coding with two agents: `simple_agent` and `image_agent`.
The main idea is to start with the `simple_agent` and evolve to `image_agent` through prompts using GEMINI Code Assist: Chat 🚀 https://developers.google.com/gemini-code-assist/docs/overview.

For this demo, I have used the following. Prerequisites to run the demo:

- Python 3.13.3 https://www.python.org/downloads/
- Google ADK https://google.github.io/adk-docs/get-started/python/
- A Google Developers program account https://developers.google.com/
- GEMINI API KEY https://aistudio.google.com or GCP Account https://console.cloud.google.com/
- Visual Studio Code https://code.visualstudio.com/
- The GEMINI Code Assist: Chat extension https://developers.google.com/gemini-code-assist/docs/use-gemini-code-assist-chat

## Setup Instructions 🛠️

Follow these steps to set up and run the demo:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/demoVibeCoding.git
    cd demoVibeCoding
    ```

2.  **Create a virtual environment:**
    It's recommended to use a virtual environment to manage dependencies.
    ```bash
    python3 -m venv .venv
    ```

3.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```

4.  **Install dependencies:**
    Install the required Python packages using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure environment variables:**
    Copy the example environment file and fill in your API keys or other necessary configurations.
    
    ⚠️ **WARNING:** Remember to create the `.env` file *outside* the `demoVibeCoding` directory. ⚠️
    ```bash
    cp .env.example ../.env
    ```
    Open the newly created `.env` file and add your specific environment variables (e.g., Google API Key, etc.).

    ```bash
    source ../.env
    ```

## Running the Agents ▶️

(Instructions on how to run `image_agent` and `simple_agent` will go here.)
```bash
adk web
```
