def chatbot():
    print("Welcom to the chatbot")
    print("to exit say 'bye' \n")

    while True:
        user=input("You:").lower()

        if user == "hello" :
            print("Chatbot: Hi how can i help you ?")

        elif user == "how are you" :
            print("Chatbot: I'm fine, what about you ?")

        elif user == "good" :
            print("Chatbot: yes, How can i assist you?")

        elif user == "what is your name" :
            print("Chatbot: I'm chatbot")
        
        elif user == "bye" :
            print("Chatbot: see you again , bye")
            break

        else:
            print("I'm not trained for this will confiremd and back to you soon")
    
chatbot()
        
