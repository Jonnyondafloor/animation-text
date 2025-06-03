from modules.animation_text import Animation

import time

def ask(question: str, output_type: type = str):
    while True:
        print(question)
        user_input = input('> ')
        try:
            output = output_type(user_input)
            print()
            return output
        except ValueError:
            print(f'Expected: {output_type.__name__}')
            time.sleep(2)
            print()


default_text = ask('Default Text', str)
print_delay = ask('Print Delay', float)
fade_delay = ask('Fade Delay', int)

animation = Animation(default_text, print_delay, fade_delay)

while True:
    user_input = input('> ').split(' ')
    command = user_input[0]
    args = user_input[1:]

    if command.lower() == 'animate':
        animation.animate(' '.join(args))
