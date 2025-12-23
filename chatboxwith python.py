import random
responses = {

        "hii":"hii!",
        "how are you":"i am fine",
        "bye": "good bye"
        }
def chatbot():
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" :
            print("Chatbot: Hii!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "what is your name":
            print("Chatbot: I am a simple Python chatbot.")
        elif user_input == "bye":
            print("Chatbot: Goodbye! hope have a good conversation between us ")
        
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()
