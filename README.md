# Telegram AI Chatbot with Gemini API

![Gemini AI Bot](https://png.pngtree.com/background/20231030/original/pngtree-d-render-of-an-adorable-ai-bot-helper-ideal-for-business-picture-image_5810378.jpg)


An asynchronous Python Telegram bot that integrates with Gemini AI to provide dynamic content generation and image summarization. The bot utilizes MongoDB for efficient data storage and retrieval.

## Features

- **User Registration**: Automatically registers users using their Telegram profile information (first name, username, and chat ID) and then prompts them to provide their phone number.
- **Gemini Chat**: Integrates with Gemini AI to generate dynamic content based on user queries, enabling interactive and intelligent responses.

- **Image Analysis**: Allows users to send images, which are then processed by Gemini AI to generate descriptive summaries.

- **Web Search /websearch <query>**: Performs web searches based on user queries and returns AI-generated summaries with top web links.

- **Sentiment Analysis**: Analyzes the sentiment of user messages and appends corresponding emojis (😊 for positive, 😞 for negative). **No emoji is appended for neutral sentiment**.

## Tools and Resources Used

- **ChatGPT**: Utilized ChatGPT for gathering resources and learning how to create and improve the project, including structuring the code and solving problems.
- **GitHub Copilot**: Used GitHub Copilot to enhance the code quality and make it more efficient by suggesting improvements and reducing repetitive code.
- **Gemini API**: Integrated the Gemini API to generate content dynamically based on user queries, enabling more interactive and intelligent responses.
- **Gemini API Documentation**: Referenced the official Gemini API documentation to understand the capabilities and limitations of the API and to implement it correctly in the project.
- **Custom Search API**: Implemented the Google Custom Search API to fetch relevant web search results based on user queries.
- **Search Engine ID**: Configured in the project to query the Custom Search Engine.

## How It Works

1. **User Input**: The bot receives user input through Telegram and interacts with the Gemini API to generate relevant responses.
2. **User Registration**: It handles user registration and stores user data for future interactions.
3. **Image Analysis**: Users can send images that the bot processes using the Gemini API to generate descriptive summaries.
4. **File Analysis**: Users can send PDF filess that the bot processes using Gemini API to generate descriptive summaries.
5. **Web Search**: The bot can perform web searches based on user requests and provide AI-generated summaries with top search links.
6. **Sentiment Analysis**: It analyzes the sentiment of user messages and appends appropriate emojis to enhance engagement.

## Getting Started

To run the bot, follow these steps:

1. **Install Python** (if not already installed):
   - Download and install Python from [here](https://www.python.org/downloads/).

2. **Set up a Virtual Environment**:
    ```bash
    py -m venv env
    ```

3. **Activate the Virtual Environment**:
    - For **Mac/Linux** users:
      ```bash
      source env/bin/activate
      ```
    - For **Windows** users:
      ```bash
      .\env\Scripts\activate
      ```

4. **Install the Dependencies**:
   ```bash
   pip install -r requirements.txt
    ```

5. **Create a `.env` file** in the project root directory with the following content:
    ```env
    TELEGRAM_TOKEN=<your_telegram_api_key>
    GEMINI_TOKEN=<your_gemini_api_key>
    MONGO_URI=<your_mongodb_uri>
    GOOGLE_SEARCH_TOKEN=<your_google_custom_search_key>
    GOOGLE_SEARCH_ENGINE_ID=<your_search_engine_id>
    ```

6. **Run the Bot**:
    ```bash
    py bot.py
    ```

Now, your bot should be running and accessible on Telegram!

## Example Commands

- `/start`: Start the bot and register your details.
- `/websearch <query>`: Perform a web search and receive AI-generated summaries with the top web links.


This should cover everything you need for your project setup, from dependencies to the `.env` configuration and running the bot.

Let me know if anything else needs adjustment!
