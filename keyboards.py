import telebot
from telebot import types
import sqlite3

keyboard_restart = types.ReplyKeyboardMarkup(
                        resize_keyboard=True, one_time_keyboard=False
                    )
keyboard_restart.row("Я передумал")

keyboard_again = types.ReplyKeyboardMarkup(
                        resize_keyboard=True, one_time_keyboard=False
                    )
keyboard_again.row("Дополнить идею")

keyboard_first =types.ReplyKeyboardMarkup(
                        resize_keyboard=True, one_time_keyboard=False
                    )
keyboard_first.row("Да", "Нет")

keyboard_adm = types.ReplyKeyboardMarkup(
                        resize_keyboard=True, one_time_keyboard=False
                    )
keyboard_adm.row("Адаптация", "Пользователи", "Вопрос/Ответ")
keyboard_adm.row("Рассылка", "Ссылки", "Контакты")
keyboard_adm.row("Обратная связь")

keyboard_user = types.ReplyKeyboardMarkup(
                        resize_keyboard=True, one_time_keyboard=False
                    )
keyboard_user.row("Вопрос/Ответ", "Документы")
keyboard_user.row("Важные контакты", "Важные ссылки")
keyboard_user.row("Забронировать аудиторию")
keyboard_user.row("Навигация по университету")
keyboard_user.row("Обратная связь")

keyboard_adapt = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=False
        )
keyboard_adapt.row("Добавить", "Редактировать", "Удалить")
keyboard_adapt.row("Просмотр ответов", "Новые пользователи")
keyboard_adapt.row("Список адаптаций")
keyboard_adapt.row("🔙 Назад")

keyboard_adapt_edit = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=False
        )
keyboard_adapt_edit.row("Название", "Дата", "День")
keyboard_adapt_edit.row("Время", "Текст", "Действие")
keyboard_adapt_edit.row("🔙 Вернуться в главное меню")

keyboard_admin_users = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=False
        )
keyboard_admin_users.row("Добавить", "Редактировать", "Удалить")
keyboard_admin_users.row("Список пользователей")
keyboard_admin_users.row("Подразделения", "Назад")

keyboard_admin_links = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=False
        )
keyboard_admin_links.row("Добавить", "Редактировать", "Удалить")
keyboard_admin_links.row("Список ссылок")
keyboard_admin_links.row("Вернуться в главное меню")

keyboard_admin_contacts = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=False
        )
keyboard_admin_contacts.row("Добавить", "Редактировать", "Удалить")
keyboard_admin_contacts.row("Список контактов")
keyboard_admin_contacts.row("🔙 Вернуться в главное меню")

keyboard_admin_question_answer = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=False
        )
keyboard_admin_question_answer.row("Добавить","Редактировать", "Удалить" )
keyboard_admin_question_answer.row("Список вопросы/ответы")
keyboard_admin_question_answer.row("Категории", "🔙 Назад")

keyboard_admin_mailing = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=False
        )
keyboard_admin_mailing.row("Добавить", "Редактировать", "Удалить")
keyboard_admin_mailing.row("Список рассылок", "Отправить")
keyboard_admin_mailing.row("🔙 Назад")

keyboard_accept_decline = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=False
        )
keyboard_admin_mailing.row("Да", "Нет")


keyboard_user_documents = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=False
        )
keyboard_user_documents.row("Инструкции")
keyboard_user_documents.row("Положения")
keyboard_user_documents.row("Прочие")
keyboard_user_documents.row("🔙 Вернуться в главное меню")
        
def generate_keyboard_new_user():
    with sqlite3.connect("users.db") as con:
        cur = con.cursor()
        cur.execute(f"SELECT full_name FROM users WHERE type_user = 'new_user'")
        myresult = cur.fetchall()
        keyboard = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=False
        )
        for x in myresult:
            button_cont = types.KeyboardButton(text=f"{x[0]}")
            keyboard.add(button_cont)
        button_cont = types.KeyboardButton(text=f"Вернуться в раздел 'Адаптации'")
        keyboard.add(button_cont)
        return keyboard