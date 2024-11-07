from utils import load_model, generate_response

# Load the model once
model = load_model()

print("Chatbot: Hi! I'm here to chat with you. Type 'bye' to end the conversation.\n")

while True:
    # Get user input
    user_input = input("You: ")

    # Exit the chat if the user says "bye"
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! It was nice chatting with you.")
        break

    # Generate and print the chatbot's response
    bot_response = generate_response(model, user_input)
    print(f"Chatbot: {bot_response}\n")
