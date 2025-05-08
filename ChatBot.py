import gradio as gr
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# nltk.download('punkt')
# nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

intents = {
    "menu":["menu", "items", "coffee", "tea", "drinks"],
    "order":["buy", "get", "want", "order", "have"],
    "location":["location", "where", "address", "place"],
    "hours":["hours", "time", "timing", "close", "open"],
    "greetings":["hi", "hey", "hello"],
    "bye":["bye", "goodbye", "see you"]
}

responses = {
    "menu":"Our menu includes expresso, latte, capaccino, teas, hearbal brews",
    "order":"Sure tell me what you would like to order",
    "location":"We are located at 123 Brew Street, NY",
    "hours":"We are open from 8am till 8pm",
    "greetings":"Hello! Welcome to Cafe Brew, what you would like to order?",
    "bye":"Goodbye! and have a great day",
    "default": "Sorry, I didn't get that. Can you please rephrase?"
}

def preprocess(text):

    tokens = word_tokenize(text.lower())
    lemma = []
    for token in tokens:
        lemma.append(lemmatizer.lemmatize(token))

    return lemma


def get_intent(user_input):

    lemmas = preprocess(user_input)

    for intent, keywords in intents.items():
        if any(word in lemmas for word in keywords):
            return intent
        
    return "default"

def respond(message, chat_history):

    intent = get_intent(message)
    bot_response = responses[intent]
    chat_history.append((message, bot_response))
    return "", chat_history


with gr.Blocks(title = "Cafe Brew Chatbot") as demo:
    gr.Markdown("### Welcome to Cafe Brew!, how can I help you?")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Enter a text and press Enter")
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()


