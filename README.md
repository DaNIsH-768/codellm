# codellm

**codellm** is an AI-powered coding agent built using the Google GenAI SDK. It leverages Large Language Models (specifically `gemini-2.5-flash`) to act as a thought partner and execution engine for coding tasks. The agent can explore a workspace, read file contents, write new code, and execute Python scripts to solve problems autonomously.

## Features

* **Autonomous Coding Agent**: Acts as a helpful AI assistant that makes and executes plans to fix issues or fulfill user requests.
* **File Management**: Can list files/directories and read file contents within a restricted working directory.
* **Code Execution**: Executes Python scripts with optional arguments using a secure subprocess environment.
* **File Writing**: Can create or overwrite files in the local workspace.
* **Tool Integration**: Uses Google's Function Calling mechanism to map LLM intents to local Python functions.

## Directory Structure

* `main.py`: The entry point of the application, handling the chat loop and function dispatching.
* `prompts.py`: Contains the system instructions that define the agent's behavior and constraints.
* `functions/`: Contains the core tool implementations:
    * `get_files_info.py`: Lists files and metadata.
    * `get_file_content.py`: Reads file text.
    * `run_python_file.py`: Executes Python scripts.
    * `write_file.py`: Writes data to disk.
    * `call_function.py`: A wrapper that routes LLM function calls to the appropriate Python code.

## Prerequisites

* Python >= 3.12
* Google GenAI API Key (stored in a `.env` file)

## Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd codellm
    ```

2.  **Install dependencies**:
    The project uses `google-genai` and `python-dotenv`.
    ```bash
    pip install google-genai==1.12.1 python-dotenv==1.1.0
    ```

3.  **Configure Environment**:
    Create a `.env` file in the root directory and add your Gemini API key:
    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

## Usage

Run the agent by providing a user prompt as a command-line argument:

```bash
python main.py "your coding request here"
```bash

## options 
`--verbose`: Enable this flag to see detailed logs of token usage and function call execution.

## Security Note
The agent is constrained to a specific working directory (configured in `functions/call_function.py` as `./calculator`) to prevent unauthorized file access or execution outside the intended project scope.
