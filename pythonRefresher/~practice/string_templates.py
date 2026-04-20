greeting = "Hello "
name = "Bob"
action = "clean the house"

f_string_sentence = f"{greeting} {name}. Please can you {action}?"

print(f_string_sentence)

phrase_template = "{} {}. Please can you {}"

formatted_sentence = phrase_template.format("Bye", "Jack", "close the door when you leave?")

print(formatted_sentence)