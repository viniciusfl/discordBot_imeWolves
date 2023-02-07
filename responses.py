from random import random
import re

def handle_response(message) -> str:
    p_message = message.lower()

    if re.match("a*[au]u", p_message):
        f = int(5*random())
        s = int(10*random())

        msg = "a"*f + "u"*s
        return msg

    if p_message == "oi":
        return "oi"

    if p_message == 'roll':
        return str(random.randInt(1,6))
    
    if p_message == 'help':
        return "`This is a help message that you can modify`"

