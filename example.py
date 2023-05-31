from time import sleep

from api import StupidGPT


def main():
    StupidGPT.clean_console()
    print('DOUBLE "enter" to send a message')

    while True:
        prompt = StupidGPT.get_query('\n\033[38;5;20mYou\033[0m: ').lower()

        if prompt == '!quit':
            break

        results = StupidGPT.send_message(prompt=prompt)
        # Print it like a streaming
        for result in results:
            print(f'\033[38;5;121m{result}\033[0m', end='', flush=True)
            sleep(0.004)
        print()

    StupidGPT.close_session()


if __name__ == "__main__":
    main()