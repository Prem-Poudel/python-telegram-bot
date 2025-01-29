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

## How It Works

1. The bot receives user input through Telegram and interacts with the Gemini API to generate relevant responses.
2. It handles user registration and stores user data for further interactions.
3. The bot can analyze files and perform web searches based on user requests.

## Getting Started

To run the bot, you need to set up the following:

1. Install virtual environment:
    ```bash
    py -m venv env
    ```

2. Activate the virtual environment:
    - For Mac/Linux users:
      ```bash
      source env/bin/activate
      ```
    - For Windows users:
      ```bash
      .\env\Scripts\activate
      ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
    ```

4. Add a `.env` file in the project root directory with the following content:

Finally, run the command:
    ```bash
    py bot.py
    ```


This should cover everything you need for your project setup, from dependencies to the `.env` configuration and running the bot.

Let me know if anything else needs adjustment!
