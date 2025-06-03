import time
import os

class Animation:
    def __init__(self,
                 default_text: str = 'Hello world!',
                 print_delay: float = 1/60,
                 fade_delay: int = 5
                 ):
        """
        :param default_text: the default text to be animated
        :param print_delay: time between each "frame"
        Examples:
            - 1/{fps}
            - 0.01

        :param fade_delay: time to wait before fading the text away
        """
        self.text = default_text
        self.print_delay = print_delay
        self.fade_delay = fade_delay
    
    def animate(self, text: str | None = None):
        if text: self.text = text

        current_text = ''

        print('\x1b[?25h]', flush=True)
        
        while current_text != self.text:
            for char in map(chr, range(32, 127)):
                print(current_text + char)
                time.sleep(self.print_delay)

                if char == self.text[len(current_text)]:
                    current_text += char
                    break
            
            else:
                current_text += self.text[len(current_text)]
                print(current_text)
        
        self._fill(self.text)
        time.sleep(self.fade_delay)
        self._fill('')

        print('\x1b[?25h')

    def _fill(self, text: str):
        """
        fills the screen with given text
        """
        rows = os.get_terminal_size()[0]
        for _ in range(rows):
            print(text)
            time.sleep(self.print_delay)
