import schedule
import telebot
from telebot import types
import keyboards
import const
import random
import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

bot = telebot.TeleBot(const.token)

login = 'noreply@inbuh.kz'
password = 'atsjbdxbdlslgoub'
url = 'smtp.yandex.ru'
recipients = ['telebot.john@mail.ru', 'lseidaliyeva@inbuh.kz', 'leilimseidalieva@gmail.com']
topic = 'Ответ в чат-боте'
question = 'Что ты можешь предложить для оптимизации нашего сервиса?'
list = ['Добро пожаловать в матрицу, ','Приветствую, джедай ','Добро пожаловать в Готэм, ','Здравствуй, землянин по имени ','Давай вместе отправимся в Подземелье Inbuh, ','Привет, покемон-мастер, ','Добро пожаловать в Вестерос, ваше величество, ', 'Привет, хранитель меча, ', 'Здравствуй, живой мертвец ']

choice = random.choice(list)

@bot.message_handler(commands=["start"])
def con(message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    button_cont = types.KeyboardButton(
        text="Отправить контакт", request_contact=True)
    keyboard.add(button_cont)
    send = bot.send_message(
        message.chat.id,
        "🤖Привет, на связи бот Inbuh и я снова с тобой.\n\nТеперь моя задача изменилась. Хочешь узнать подробно? Жми на кнопочку ниже и отправь свой контакт.",
        reply_markup=keyboard,
    )
    bot.register_next_step_handler(send, con2)

def con2(message):
    global tel
    if message.contact is not None:
        if message.from_user.id == message.contact.user_id:
            print(
            "Добавлен контакт:\nID: {0}\nName: {1} {2}\nPhone number: {3}".format(
                message.contact.user_id,
                message.contact.last_name,
                message.contact.first_name,
                message.contact.phone_number,
            ))   
            last_name = message.from_user.last_name
            if last_name == None:
                last_name = "-"
            first_name = message.from_user.first_name
            if first_name == None:
                first_name = "-"
            tel = message.contact.phone_number
            send = bot.send_message(
                message.chat.id,
                choice + first_name +"!\n\n🌟Как я уже упоминал, моя цель - помочь тебе участвовать в развитии нашей компании и получать за это приятные бонусы.\n\n⌚ Для участия в данном мероприятии необходимо предложить свою крутую идею.\n\nТы готов?",
                reply_markup=keyboards.keyboard_first,
            )
            bot.register_next_step_handler(send, con3)
        else:
           print('.')
    else:
        send = bot.send_message(message.chat.id, 'Я не понимаю тебя. Пожалуйста, нажми кнопку "Отправить контакт".')
        bot.register_next_step_handler(send, con2)

def con3(message):
    if message.text is None:
        send = bot.send_message(
            message.chat.id,
            'Я не принимаю документы или фотографии. Воспользуйся кнопками.'
        )
        bot.register_next_step_handler(send, con3)
    elif "да" in message.text.lower():
        global question
        send = bot.send_message(
            message.chat.id,
            'Отлично, давай начнём! 🙌🏻\n\n '+question,
            reply_markup=types.ReplyKeyboardRemove(),
        )
        bot.register_next_step_handler(send, con4)
    elif "нет" in message.text.lower():
        send = bot.send_message(
            message.chat.id,
            "Очень жаль, что Вы приняли такое решение. Но всегда можно передумать. 😔",
            reply_markup=keyboards.keyboard_restart,
        )
        bot.register_next_step_handler(send, con8)
    
    else:
        send = bot.send_message(message.chat.id, 'Я не понимаю тебя. Воспользуйся кнопками ниже.')
        bot.register_next_step_handler(send, con3)
  
def con4(message):
    global tel
    global question
    if message.text is not None:
        if 'start' in message.text:
            print("ERROR")
            send = bot.send_message(
            message.chat.id,
                'Процесс запущен. Обратного пути нет. Вам некуда бежать Анастасия!'
            )
            bot.register_next_step_handler(send, con4)
        else:
            last_name = message.from_user.last_name
            if last_name == None:
                last_name = "-"
            first_name = message.from_user.first_name
            if first_name == None:
                first_name = "-"
            text = message.text
            send = bot.send_message(
                message.chat.id,
                "Спасибо за участие! 🩷\n\nВ скором времени ты получишь обратную связь от руководства",
                reply_markup=keyboards.keyboard_again,
            )
            print(message.text)
            bot.register_next_step_handler(send, con5)
            mail = """\
            <!DOCTYPE html>
            <link rel="stylesheet" href="style.css">
            <div id="DroppableDiv" class="layout droppable customer-email mobile-mail-repl ui-droppable ui-sortable"
                current-email-width="600" style="padding-top:20px; /* border: 1px solid red; */">
                <div class="line email-struc-item card-holder" id="line_1">
                    <div class="email-sized-wrapper email-columns card-holder"
                        style="width: 600px; border-left-width: 0px; border-right-width: 0px;">
                        <div class="droppable" id="droppable_2"
                            style="width: 600px; border: 0px; background-color: rgb(255, 255, 255);">
                            <div class="out_block email-text-out-block ui-draggable" data-element-type="text"
                                elemtype="mail_text_simple" id="out_block_2"
                                style="padding: 20px 30px; background-color: rgb(255, 255, 255);">
                                <div class="mob-hidden-handler-wrapper handler-wrapper constructor-menu-items js-mob-hidden-icon">
                                    <div class="handler-item"><img
                                            src="https://inbuh.kz/cms/uploads/file_1664182049_871427143.png" style="width: 144px;
                                        max-width: 600px; display: inline-block; vertical-align: top; padding: 10px;"
                                            alt="mobile hidden"></div>
                                </div>
                                <div><br></div>
                                
                                            <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">Вам пришёл ответ на вопрос в боте.</span></div>
                                            <div><br></div>
                                            <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">Имя: """+first_name+"""</span></div>
                                            <div><br></div>
                                            <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">Tel: """+tel+"""</span></div>
                                            <div><br></div>
                                            <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">Вопрос: """+question+"""<p>Текст: """+text+"""</p></span></div>
                                            <div><br></div>

                                <div class="mail_text_simple_border data_text email-text mce-content-body" id="mce_0">
                                    <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">Web:&nbsp;<a
                                                href="http://www.inbuh.kz/" rel="noopener noreferrer" target="_blank"
                                                data-link-id="2" data-mce-href="http://www.inbuh.kz/">www.inbuh.kz</a></span></div>
                                    <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">Email:&nbsp;<a
                                                href="mailto:info@inbuh.kz" rel="noopener noreferrer" target="_blank"
                                                data-mce-href="mailto:info@inbuh.kz">info@inbuh.kz</a>,&nbsp;<a
                                                href="mailto:support@inbuh.kz" rel="noopener noreferrer" target="_blank"
                                                data-mce-href="mailto:support@inbuh.kz">sales@inbuh.kz</a></span></div>
                                    <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">Tel:&nbsp;<a
                                                href="tel:+7(727)352-85-55" rel="noopener noreferrer" target="_blank"
                                                data-mce-href="tel:+7(727)352-85-55">+7 (727) 352-85-55</a>,&nbsp;<a
                                                href="tel:+7(777)270-46-33" rel="noopener noreferrer" target="_blank"
                                                data-mce-href="tel:+7(777)270-46-33">+7 (707) 350-02-32</a></span></div>
                                    <div><span style="font-size: 16px;"
                                            data-mce-style="font-size: 16px;">-------------------------------------------------------------------</span>
                                    </div>
                                    <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">Наши услуги:</span></div>
                                    <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">- Аренда конфигураций
                                            1С;</span></div>
                                    <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">- Ведение бухгалтерского и
                                            налогового учета;</span></div>
                                    <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">- Сдача налоговой
                                            отчетности;</span></div>
                                    <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">- Автоматическое
                                            формирование отчетов для руководителей и др.</span></div>
                                </div>
                            </div>
                            <div style="align-items: center;display: flex;justify-content: space-around;">
                                <div style="align-items: center;display: flex;justify-content: space-around;">
                                    <div class="social_element"><a href="https://www.facebook.com/inbuh/" target="_blank"><img src="https://login.sendpulse.com/img/constructor/social/round/facebook.png" hspace="5"
                                                vspace="5" width="32px"></a></div>
                                    <div class="social_element"><a href="https://www.instagram.com/inbuh/" target="_blank"><img src="https://login.sendpulse.com/img/constructor/social/round/twitter.png" hspace="5"
                                                vspace="5" width="32px"></a></div>
                                    <div class="social_element"><a href="https://t.me/inbuh" target="_blank"><img src="https://login.sendpulse.com/img/constructor/social/round/telegram.png" hspace="5"
                                                vspace="5" width="32px"></a></div>
                                    <div class="social_element"><a href="https://www.youtube.com/channel/UCTHT3en7CdRpNRjg3XlAu3Q" target="_blank"><img src="https://login.sendpulse.com/img/constructor/social/round/youtube.png" hspace="5"
                                                vspace="5" width="32px"></a></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="line email-struc-item card-holder" id="line_3">
                    <div class="move-handler-wrapper handler-wrapper constructor-menu-items">
                        <div class="move-handler-line handler-item"><span class="constr-icon icon-move"></span></div>
                    </div>
                    
                </div>
            </div>
            """
            msg = MIMEMultipart()

            msg['Subject'] = topic
            msg['From'] = login
            msg['To'] = ", ".join(recipients)
            body = mail
            msg.attach(MIMEText(body,'html'))

            server = root.SMTP_SSL(url, 465)
            server.login(login,password)
            server.sendmail(login,recipients,msg.as_string())
    elif message.text is None:
        send = bot.send_message(
            message.chat.id,
            'Я не принимаю документы или фотографии. Отправь свой ответ в виде текста.'
        )
        bot.register_next_step_handler(send, con4)
    else:
        print(message)
        send = bot.send_message(
            message.chat.id,
            'Вы уже отправили ответ. Но Вы можете воспользоваться кнопкой ниже "Дополнить идею".'
        )
        bot.register_next_step_handler(send, con5)

choice = random.choice(list)

def con5(message):
    if message.text is None:
        send = bot.send_message(
            message.chat.id,
            'Я не принимаю документы или фотографии. Воспользуйся кнопкой ниже.'
        )
        bot.register_next_step_handler(send, con5)
    elif "дополнить идею" in message.text.lower():
        send = bot.send_message(
            message.chat.id,
            "О, у тебя появилась новая идея? Я буду рад её услышать.",
            reply_markup=types.ReplyKeyboardRemove()
        )
        bot.register_next_step_handler(send, con4)
    else:
        send = bot.send_message(
            message.chat.id,
            'Вы уже отправили ответ. Но Вы можете воспользоваться кнопкой ниже "Дополнить идею".'
        )
        bot.register_next_step_handler(send, con5)

def con8(message):
    if message.text is None:
        send = bot.send_message(
            message.chat.id,
            'Я не принимаю документы или фотографии. Воспользуйся кнопкой ниже.'
        )
        bot.register_next_step_handler(send, con8)
    elif "я передумал" in message.text.lower():
        send = bot.send_message(
            message.chat.id,
            "Я рад, что ты решил передумать.\n\nВопрос звучит так: "+question+"",
            reply_markup=types.ReplyKeyboardRemove()
        )
        bot.register_next_step_handler(send, con4)
    else:
        send = bot.send_message(
            message.chat.id,
            "К сожалению я не понимаю тебя. Ты всё таки передумал? Воспользуйся кнопкой ниже."
        )
        bot.register_next_step_handler(send, con8)
        
if __name__ == "__main__":
    global btn_click
    btn_click = False
    schedule.run_pending()
    print("Бот успешно запущен!")
    bot.polling()