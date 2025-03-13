response = {
    "hello": "Hello! How can I help you today?",
    "tell me about [place]": "I can provide information about places. Please specify the place you're interested in.",
    "bye": "goodbye! havr a great day!",
    "default": "I'm sorry, I do not understand your question. Please try again."
}
def get_bot_response(user_message):
    user_message = user_message.lower()
    if user_message in response:
        return response[user_message]
    elif "tell me about" in user_message:
        return response["tell me about [place]"]
    else:
        return response["default"]

def main():

    print("welcome to chats! how can i help you today? type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("chat:" + response["bye"])
            break
        bot_response = get_bot_response(user_input)
        print(bot_response)

    print("thank you for using chats!")

if __name__ == "__main__":
    main()