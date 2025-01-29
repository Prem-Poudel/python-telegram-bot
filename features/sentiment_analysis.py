import google.generativeai as genai
import emoji


# Function to analyze sentiment using Gemini API
def analyze_sentiment(text):
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    response = model.generate_content(f"Analyze the sentiment of the following text: '{text}'")
    if response and hasattr(response, 'text'):
        return response.text.strip().lower()
    return "neutral"

# Function to add emoji based on sentiment
def add_emoji_based_on_sentiment(text):
    sentiment = analyze_sentiment(text)
    if "positive" in sentiment:
        return text + " " + emoji.emojize(':smile:', language='alias')
    elif "negative" in sentiment:
        return text + " " + emoji.emojize(':disappointed:', language='alias')
    else:
        return text