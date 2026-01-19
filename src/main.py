from pyswip import Prolog
import statement
import question

prolog = Prolog()
prolog.consult("prolog.pl")

def print_goodbye():
    print("\n           Goodbye!")
    print("===============================")

print("===============================")
print("    Welcome to the Chatbot!\n")

while True:
    user_input = input("> ")
    
    if user_input.endswith('.'):
        statement.process_statement(user_input, prolog)
    elif user_input.endswith('?'):
        question.process_question(user_input, prolog)
    elif "bye!" in user_input.lower() or user_input == "0":
        print_goodbye()
        break
    else:
        print("I don't understand.")
        