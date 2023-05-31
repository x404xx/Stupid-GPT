<div align="center">

<img src="https://stupidgpt.lol/StupidGPT%20V2%20.png" width="auto" height="auto">

A command-line tool for interacting with StupidGPT chatbot. (https://stupidgpt.lol)

<img src="https://github.com/x404xx/Stupid-GPT/assets/114883816/e37f1e3d-cc37-47e8-863b-e606bb73ec50" width="auto" height="auto">

## **"This is not an official API"**

> **Note**
> This _**StupidGPT**_ can be hilarious, and sometimes it can also generate code for you just like the normal gpt..

</div>

## **Requirements**

```
pip install httpx
```

## **Usage**

You can find an example of how to use this API in the (_**example.py**_) file or you can do like the following code

```python
from time import sleep

from api import StupidGPT


StupidGPT.clean_console()
print('DOUBLE "enter" to send a message')

while True:
    prompt = StupidGPT.get_query('\n\033[38;5;20mYou\033[0m: ').lower()

    if prompt == '!quit':
        break

    results = StupidGPT.send_message(prompt=prompt)
    #! Print it like a streaming
    for result in results:
        print(f'\033[38;5;121m{result}\033[0m', end='', flush=True)
        sleep(0.004)
    print()

StupidGPT.close_session()
```

## **Legal Disclaimer**

> **Note**
> This was made for educational purposes only, nobody which directly involved in this project is responsible for any damages caused. **_You are responsible for your actions._**
