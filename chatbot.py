import re

def chatbot():
    print("Welcome to Pizza Planet!")
    while True:
        user_input = input("You: ").lower()

        if re.search(r"\b\d{4}\b", user_input) or "zip" in user_input or "zip code" in user_input:
            print("Chatbot: Thank you for your order, it will be ready shortly! Goodbye!")
            break

        if "order" in user_input:
            print("Chatbot: Great! What size of pizza would you like? (small, medium, large, extra large)")

        elif "small" in user_input or "medium" in user_input or "large" in user_input or "extra large" in user_input:
            print("Chatbot: What toppings would you like?")

        elif "toppings" in user_input or "kind" in user_input:
            print("Chatbot: We offer pepperoni, mushrooms, onions, sausage, bacon, cheese, & peppers.")

        elif "pepperoni" in user_input or "mushrooms" in user_input or "onions" in user_input or "sausage" in user_input or "bacon" in user_input or "cheese" in user_input or "peppers" in user_input or "none" in user_input:
            print("Chatbot: Is that all for you today?")

        elif "no" in user_input: print("Chatbot: What else can I get for you today?")

        elif "thats all" in user_input or "yes" in user_input or"nothing" in user_input or "thats it" in user_input or "thats everything" in user_input or "I'm done" in user_input: print("Chatbot: May I please have your address and zipcode?")
        else:
          print("Chatbot: I'm sorry, I didn't catch that. Can you please rephrase that request?")

chatbot()
