import os
from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
session = VkApi(token=token)
session._auth_token()

a = True
b = False

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
        "attachment": f"doc-204076641_{media_id}",
    }

    if keyboard != None:
        post["keyboard"] = keyboard.get_keyboard()
    else:
        post = post

    session.method("messages.send", post)

for event in VkLongPoll(session).listen():

    keyboard = VkKeyboard(one_time=False)
    keyboard.add_openlink_button(label='Наш сайт', link='https://antarestudy.ru/')
    keyboard.add_line()
    keyboard.add_button("Информация о курсах", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Пройти опрос!", color=VkKeyboardColor.POSITIVE)

    keyboard1 = VkKeyboard(one_time=False)
    keyboard1.add_button("Математика ЕГЭ", color=VkKeyboardColor.POSITIVE)
    keyboard1.add_button("Физика ЕГЭ", color=VkKeyboardColor.POSITIVE)
    keyboard1.add_line()
    keyboard1.add_button("Математика ОГЭ", color=VkKeyboardColor.POSITIVE)
    keyboard1.add_button("Физика ОГЭ", color=VkKeyboardColor.POSITIVE)
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
    keyboard4.add_button("Мск", color=VkKeyboardColor.POSITIVE)
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

    keyboard7 = VkKeyboard(one_time=False)
    keyboard7.add_button("9", color=VkKeyboardColor.POSITIVE)
    keyboard7.add_button("10", color=VkKeyboardColor.POSITIVE)
    keyboard7.add_line()
    keyboard7.add_button("11", color=VkKeyboardColor.POSITIVE)
    keyboard7.add_button("Закончить опрос", color=VkKeyboardColor.NEGATIVE)

    keyboard8 = VkKeyboard(one_time=False)
    keyboard8.add_button("ЕГЭ математика", color=VkKeyboardColor.POSITIVE)
    keyboard8.add_line()
    keyboard8.add_button("ЕГЭ физика", color=VkKeyboardColor.POSITIVE)
    keyboard8.add_line()
    keyboard8.add_button("ОГЭ математика", color=VkKeyboardColor.POSITIVE)
    keyboard8.add_line()
    keyboard8.add_button("ОГЭ физика", color=VkKeyboardColor.POSITIVE)
    keyboard8.add_line()
    keyboard8.add_button("Далее", color=VkKeyboardColor.PRIMARY)
    keyboard8.add_line()
    keyboard8.add_button("Закончить опрос", color=VkKeyboardColor.NEGATIVE)

    keyboard9 = VkKeyboard(one_time=False)
    keyboard9.add_button("Закончить опрос", color=VkKeyboardColor.PRIMARY)

    keyboard10 = VkKeyboard(one_time=False)
    keyboard10.add_button("Старт", color=VkKeyboardColor.POSITIVE)


    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id,
        text = event.text.lower()
        peer_id = event.peer_id

        if a == True:

            if text == 'старт':
                b = True
                send_message(user_id, 'Наши менеджеры уже зарегистрировали обращение от тебя и спешат ответить, однако пока не стоит тратить время зря: изучи возможности нашего бота-помощника ниже.'
                '\n\nМы ответим как можно скорее! 🚀', 0, keyboard)
                a = False

            else:
                send_message(user_id, 'Привет! Добро пожаловать в школу Антарес.'
                '\nНажми на кнопку "Старт", чтобы начать чат!', 0, keyboard10)

        elif b == True:
            if text == 'информация о курсах':
                send_message(user_id, 'Выбери курс, который тебе интересен 👇🏻', 0, keyboard1)

            elif text == 'математика огэ':
                send_message(user_id, 'Наш курс поможет тебе вместе с классными преподавателями в дружной группе получить знания по предмету и уверено подготовится к сдаче экзамена!😄'
                '\n\nЗагляни в учебный план из файла ниже, чтобы узнать подробно о распределении тем на занятиях.'
                '\n\nБолее подробное описание ты можешь прочитать на страничке курса на нашем сайте: https://antarestudy.ru/math_oge.html'
                '\n\nЕсли у тебя остались вопросы, не стесняйся их задавать здесь нашим менеджерам!', 'Математика ОГЭ.pdf', keyboard1)

                send_message(user_id, 'Также обрати внимание на фотографию с тарифами, которые можно выбрать при покупке курса:', 'Тарифы Математика ОГЭ.png', keyboard1)

            elif text == 'физика огэ':
                send_message(user_id, 'Наш курс поможет тебе вместе с классными преподавателями в дружной группе получить знания по предмету и уверено подготовится к сдаче экзамена!😄'
                '\n\nЗагляни в учебный план из файла ниже, чтобы узнать подробно о распределении тем на занятиях.'
                '\n\nБолее подробное описание ты можешь прочитать на страничке курса на нашем сайте: https://antarestudy.ru/physics_oge.html'
                '\n\nЕсли у тебя остались вопросы, не стесняйся их задавать здесь нашим менеджерам!', "Физика ОГЭ.pdf", keyboard1)

                send_message(user_id, 'Также обрати внимание на фотографию с тарифами, которые можно выбрать при покупке курса:', 'Тарифы Физика ОГЭ.png', keyboard1)

            elif text == 'математика егэ':
                send_message(user_id, 'Наш курс поможет тебе вместе с классными преподавателями в дружной группе получить знания по предмету и уверено подготовится к сдаче экзамена!😄'
                '\n\nЗагляни в учебный план из файла ниже, чтобы узнать подробно о распределении тем на занятиях.'
                '\n\nБолее подробное описание ты можешь прочитать на страничке курса на нашем сайте: https://antarestudy.ru/math_ege.html'
                '\n\nЕсли у тебя остались вопросы, не стесняйся их задавать здесь нашим менеджерам!', 'Математика ЕГЭ.pdf', keyboard1)

                send_message(user_id, 'Также обрати внимание на фотографию с тарифами, которые можно выбрать при покупке курса:', 'Тарифы Математика ЕГЭ.png', keyboard1)

            elif text == 'физика егэ':
                send_message(user_id, 'Наш курс поможет тебе вместе с классными преподавателями в дружной группе получить знания по предмету и уверено подготовится к сдаче экзамена!😄'
                '\n\nЗагляни в учебный план из файла ниже, чтобы узнать подробно о распределении тем на занятиях.'
                '\n\nБолее подробное описание ты можешь прочитать на страничке курса на нашем сайте: https://antarestudy.ru/physics_ege.html'
                '\n\nЕсли у тебя остались вопросы, не стесняйся их задавать здесь нашим менеджерам!', 'Физика ЕГЭ.pdf', keyboard1)

                send_message(user_id, 'Также обрати внимание на фотографию с тарифами, которые можно выбрать при покупке курса:', 'Тарифы Физика ЕГЭ.png', keyboard1)

            elif text == 'назад':
                send_message(user_id,
                'Пока наши менеджеры спешат закончить общение с другими учениками и ответить тебе, изучи функционал бота-помощника.'
                '\n\nОбрати внимание на прохождение небольшого опроса по кнопке ниже, твои ответы значительно ускорят работу наших менеджеров 🚀'
                '\n\nМы напишем как можно скорее!', 0, keyboard)

            elif text == 'закончить опрос':
                send_message(user_id, 'Опрос окончен! Скоро наш менеджер свяжется с тобой!', 0, keyboard)

            elif text == 'пройти опрос!':
                send_message(user_id, 'Наш менеджер скоро с тобой свяжется. А пока можешь рассказать о себе, чтобы нам было проще.', 0, keyboard2)
                send_message(user_id, 'Сколько тебе лет?', 0, keyboard3)

            elif text == '15' or text == '16' or text == '17' or text == '18':
                send_message(user_id, 'Здорово, выбери свой часовой пояс:', 0, keyboard4)

            elif text == 'мск - 1' or text == 'мск' or text == 'мск + 1' or text == 'мск + 2' or text == 'мск + 3' or text == 'мск + 4' or text == 'мск + 5' or text == 'мск + 6' or text == 'мск + 7' or text == 'мск + 8' or text == 'мск + 9':
                send_message(user_id, 'В каком классе ты учишься?', 0, keyboard7)

            elif text == '9' or text == '10' or text == '11':
                send_message(user_id, 'Какие курсы тебя интересуют?' '\n\nМожешь выбрать интересные тебе курсы с помощью зелёных кнопок.', 0, keyboard8)

            elif text == 'огэ' or text == 'егэ':
                send_message(user_id, 'Отлично! Теперь выбери интересующий тебя предмет!', 0, keyboard6)

            elif text == 'математика' or text == 'физика':
                send_message(user_id, 'Спасибо за прохождение опроса! Наш менеджер скоро свяжется с тобой!', 0, keyboard)

            elif text == 'далее':
                send_message(user_id, 'Почему ты обратил внимание именно на нашу школу?', 0, keyboard9)

            elif text == 'старт':
                send_message(user_id, 'Наши менеджеры уже зарегистрировали обращение от тебя и спешат ответить, однако пока не стоит тратить время зря: изучи возможности нашего бота-помощника ниже.'
                '\nМы ответим как можно скорее! 🚀', 0, keyboard)
                a = False