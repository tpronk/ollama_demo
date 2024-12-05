# Using a local LLM using Python
This repo contains two simple python scripts that use a local instance of llama3.2 (and supporting models). `hello_world.py` offers a basic prompt-response demo, while `parse_directory.py` processes a bunch of `docx` and `pptx` files to run semantic search on.

The demos were tested on Python 3.12; Python 3.13 was not supported (yet).

# Installing dependencies
1. Install [Ollama](https://ollama.com/)
2. Start a terminal session and run `ollama pull llama3.2`
3. Start Ollama
4. Install python requirements by running `pip install -r requirements.txt`

You're now good to go! Run one of the two Python scripts to try them out. 
