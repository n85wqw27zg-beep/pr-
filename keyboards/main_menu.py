from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🤝 Познакомиться с PRESIDENT")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📖 О агентстве")],
        [KeyboardButton(text="💎 Наши преимущества")],
        [KeyboardButton(text="📋 Требования")],
        [KeyboardButton(text="💼 Условия сотрудничества")],
        [KeyboardButton(text="💰 Доход и выплаты")],
        [KeyboardButton(text="🛡 Безопасность")],
        [KeyboardButton(text="❓ FAQ")],
        [KeyboardButton(text="📞 Контакты")],
        [KeyboardButton(text="📝 Подать заявку")],
    ],
    resize_keyboard=True
)