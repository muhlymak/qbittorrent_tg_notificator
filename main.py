import sys
import os
import requests
from dotenv import dotenv_values


def telegram_notication(bot_token, chat_id, text_message) -> None:
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": text_message}
    requests.post(url, data=data)


def main():
    # Проверяем, есть ли аргументы командной строки
    if len(sys.argv) < 2:
        print("Usage: python script.py arg1 arg2 ...")
        return
    absolute_path = os.path.abspath(__file__)
    directory_path = os.path.dirname(absolute_path)
    env_vars = dotenv_values(f"{directory_path}/.env")

    # Получаем переданные аргументы
    args = sys.argv[1:]
    text_message = f"Торрент {args} скачан"
    telegram_notication(
        bot_token=env_vars["BOT_TOKEN"],
        chat_id=env_vars["MESSAGE_TO"],
        text_message=text_message,
    )


if __name__ == "__main__":
    main()

# Тестовое из nvim + lazygit
