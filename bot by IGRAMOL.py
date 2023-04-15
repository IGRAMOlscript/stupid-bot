import logging
import random
import time


def chatgpt():

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    logger.info('Starting chatbot without GPT-3 Simple')

    #Cписок ответов
    responses = ["Hi there!",
                 "How are you?",
                 "What can I do for you?",
                 "I'm sorry, I don't understand.",
                 "I'm not sure what you mean.",
                 "Can you elaborate on that?"]

    # Начало разговор
    print("Hello, I'm a chatbot. How can I help you?")

    # Продолжение разговора
    while True:
        user_input = input("\n> ")

        # Проверка команды
        if user_input == "exit":
            break


        response = random.choice(responses)
        print(response)

        # инфо
        logger.info('User: %s | Bot: %s', user_input, response)

        # время
        time.sleep(1)

    print("Goodbye!")


if __name__ == "__main__":
    chatgpt()

