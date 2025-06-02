# your text message here:
text = "Hello World!"
print_delay = 1/60 # 1/{fps} | {seconds} (0.01)

import time

current_text = ""

print(end='\x1b[?25l', flush=True)

while current_text != text:
    for char in map(chr, range(32, 127)):
        print(current_text + char)
        time.sleep(print_delay)

        if char == text[len(current_text)]:
            current_text += char
            break

    else:
        current_text += text[len(current_text)]
        print(current_text)

print('\x1b[?25h')
