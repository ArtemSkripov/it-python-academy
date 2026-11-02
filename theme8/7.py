from typing import Callable


def send_notification(message: str, notify_func: Callable) -> None:
    notify_func(message, 3)


def send_email(message: str, count: int) -> None:
    for _ in range(count):
        print("Отправлено письмо: ", message)


def send_push(message: str) -> None:
    print("Отправлено push: ", message)


# send_notification("Ваш заказ доставлен", send_email)
send_notification("Ваш заказ доставлен", send_push)

