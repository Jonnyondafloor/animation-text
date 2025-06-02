# your text message here:
text = "Hello World!"
print_delay = 1/60 # 1/{fps} | {seconds} (0.01)

import time
import os

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

rows, columns = os.get_terminal_size()
for _ in range(rows):
    print(text)
    time.sleep(print_delay)


print('\x1b[?25h')
