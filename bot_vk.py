from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

token = 'cb281c6199a51bf04d9b606245f5791e5b64d0e9f7d50fbb5b815fb77776483919116a0a3e82e1b8271e3'
session = VkApi(token=token)
session._auth_token()
b = True


def get_docs_info(q, count):
    post = {
        "q": q,
        "search_own": 1,
        "count": count,
        "scope": "docs",
    }

    return session.method("docs.search", post)

def send_message(user_id, message_content, q, keyboard=None):
    media_id = get_docs_info(q, 1)["items"][0]["id"]
    post = {
        "user_id": user_id,
        "message": message_content,
        "random_id": 0,
        "attachment": f"doc-206029109_{media_id}"
    }

    if keyboard != None:
        post["keyboard"] = keyboard.get_keyboard()
    else:
        post = post

    session.method("messages.send", post)

for event in VkLongPoll(session).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id,
        text = event.text.lower()
        peer_id = event.peer_id

        keyboard = VkKeyboard(one_time=False)
        keyboard.add_openlink_button(label='Наш сайт', link='https://coolermgdn.github.io')
        keyboard.add_line()
        keyboard.add_button("Информация о школе", color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button("Связаться с менеджером", color=VkKeyboardColor.POSITIVE)

        keyboard1 = VkKeyboard(one_time=False)
        keyboard1.add_button("Математика ОГЭ", color=VkKeyboardColor.POSITIVE)
        keyboard1.add_line()
        keyboard1.add_button("Физика ОГЭ", color=VkKeyboardColor.POSITIVE)
        keyboard1.add_line()
        keyboard1.add_button("Математика ЕГЭ", color=VkKeyboardColor.POSITIVE)
        keyboard1.add_line()
        keyboard1.add_button("Физика ЕГЭ", color=VkKeyboardColor.POSITIVE)
        keyboard1.add_line()
        keyboard1.add_button("Назад", color=VkKeyboardColor.NEGATIVE)

        keyboard2 = VkKeyboard(one_time=False)
        keyboard2.add_button("Закончить опрос", color=VkKeyboardColor.NEGATIVE)

        keyboard3 = VkKeyboard(one_time=False)
        keyboard3.add_button("15", color=VkKeyboardColor.POSITIVE)
        keyboard3.add_button("16", color=VkKeyboardColor.POSITIVE)
        keyboard3.add_line()
        keyboard3.add_button("17", color=VkKeyboardColor.POSITIVE)
        keyboard3.add_button("18", color=VkKeyboardColor.POSITIVE)
        keyboard3.add_line()
        keyboard3.add_button("Закончить опрос", color=VkKeyboardColor.NEGATIVE)

        keyboard4 = VkKeyboard(one_time=False)
        keyboard4.add_button("Мск - 1", color=VkKeyboardColor.POSITIVE)
        keyboard4.add_button("Мск + 0", color=VkKeyboardColor.POSITIVE)
        keyboard4.add_line()
        keyboard4.add_button("Мск + 1", color=VkKeyboardColor.POSITIVE)
        keyboard4.add_button("Мск + 2", color=VkKeyboardColor.POSITIVE)
        keyboard4.add_line()
        keyboard4.add_button("Мск + 3", color=VkKeyboardColor.POSITIVE)
        keyboard4.add_button("Мск + 4", color=VkKeyboardColor.POSITIVE)
        keyboard4.add_line()
        keyboard4.add_button("Мск + 5", color=VkKeyboardColor.POSITIVE)
        keyboard4.add_button("Мск + 6", color=VkKeyboardColor.POSITIVE)
        keyboard4.add_line()
        keyboard4.add_button("Мск + 7", color=VkKeyboardColor.POSITIVE)
        keyboard4.add_button("Мск + 8", color=VkKeyboardColor.POSITIVE)
        keyboard4.add_line()
        keyboard4.add_button("Мск + 9", color=VkKeyboardColor.POSITIVE)
        keyboard4.add_button("Закончить опрос", color=VkKeyboardColor.NEGATIVE)

        keyboard5 = VkKeyboard(one_time=False)
        keyboard5.add_button("ОГЭ", color=VkKeyboardColor.POSITIVE)
        keyboard5.add_line()
        keyboard5.add_button("ЕГЭ", color=VkKeyboardColor.POSITIVE)
        keyboard5.add_line()
        keyboard5.add_button("Закончить опрос", color=VkKeyboardColor.NEGATIVE)

        keyboard6 = VkKeyboard(one_time=False)
        keyboard6.add_button("Математика", color=VkKeyboardColor.POSITIVE)
        keyboard6.add_line()
        keyboard6.add_button("Физика", color=VkKeyboardColor.POSITIVE)
        keyboard6.add_line()
        keyboard6.add_button("Закончить опрос", color=VkKeyboardColor.NEGATIVE)

        # Example
        if text == 'информация о школе':
            send_message(user_id, 'Выберите курс, который Вам интересен', 0, keyboard1)

        elif text == 'математика огэ':
            send_message(user_id, 'Всю информацию Вы можете найти на нашем сайте: https://coolermgdn.github.io/math_oge.html', 1, keyboard1)

        elif text == 'физика огэ':
            send_message(user_id, 'Всю информацию Вы можете найти на нашем сайте: https://coolermgdn.github.io/physics_oge.html', 2, keyboard1)

        elif text == 'математика егэ':
            send_message(user_id, 'Всю информацию Вы можете найти на нашем сайте: https://coolermgdn.github.io/math_ege.html', 3, keyboard1)

        elif text == 'физика егэ':
            send_message(user_id, 'Всю информацию Вы можете найти на нашем сайте: https://coolermgdn.github.io/physics_ege.html', 4, keyboard1)

        elif text == 'назад':
            send_message(user_id, 'Возвращаемся в главное меню', 0, keyboard)

        elif text == 'закончить опрос':
            send_message(user_id, 'Опрос окончен! Скоро наш менеджер свяжется с тобой!', 0, keyboard)

        elif text == 'связаться с менеджером':
            send_message(user_id, 'Наш менеджер скоро с Вами свяжется. А пока можете рассказать о себе, чтобы было '
                                  'проще.', 0, keyboard2)
            send_message(user_id, 'Укажи свой возраст.', 0, keyboard3)

        elif text == '15' or text == '16' or text == '17' or text == '18':
            send_message(user_id, 'Отлично! Укажи свой часовой пояс!', 0, keyboard4)

        elif text == 'мск - 1' or text == 'мск + 0' or text == 'мск + 1' or text == 'мск + 2' or text == 'мск + 3' or text == 'мск + 4' or text == 'мск + 5' or text == 'мск + 6' or text == 'мск + 7' or text == 'мск + 8' or text == 'мск + 9':
            send_message(user_id, 'Отлично! Теперь выбери интересующий тебя уровень подготовки!', 0, keyboard5)

        elif text == 'огэ' or text == 'егэ':
            send_message(user_id, 'Отлично! Теперь выбери интересующий тебя предмет!', 0, keyboard6)

        elif text == 'математика' or text == 'физика':
            send_message(user_id, 'Спасибо за прохождение опроса! Наш менеджер скоро свяжется с тобой!', 0, keyboard)

        else:
            send_message(user_id, 'Прости, я тебя не понимаю! Нажми на интересующую тебя кнопку!', 0, keyboard)


