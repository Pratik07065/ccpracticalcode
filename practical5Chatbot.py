def farming_chatbot():
    print("Welcome to the Farming Guidance Chatbot!")
    print("Ask me anything about crops, irrigation, soil, fertilizers, etc.")
    print("Type 'exit' anytime to end the chat.")
    print("---------------------------------------------------------------")
    while True:
        user_input = input("You: ").lower()
        if 'exit' in user_input:
            print("Chatbot: Thank you for visiting! Happy Farming!")
            break
        elif "crop" in user_input:
            print("Chatbot: In summer, crops like maize, cotton, and rice are ideal.")
            print("In winter, wheat, mustard, and peas are commonly grown.")
        elif "irrigation" in user_input:
            print("Chatbot: Drip irrigation saves water and is best for fruit crops.")
            print("Sprinkler irrigation is suitable for large fields like wheat.")
        elif "soil" in user_input:
            print("Chatbot: Loamy soil is best for most crops.")
            print("Regular addition of compost and organic matter improves soil health.")
        elif "fertilizer" in user_input:
            print("Chatbot: Use NPK fertilizers based on your soil test report.")
            print("Organic fertilizers like cow dung and compost are also very helpful.")
        elif "pest" in user_input or "disease" in user_input:
            print("Chatbot: Neem oil spray works naturally for pests.")
            print("For major diseases, consult a local agriculture officer.")
        else:
            print("Chatbot: I'm sorry, I don't have information on that. Please ask about crops, soil, irrigation, or fertilizers.")

farming_chatbot()