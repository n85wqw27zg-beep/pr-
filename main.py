import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import KeyboardButton, InputMediaPhoto, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove

from config import MANAGER_ID, TOKEN
from keyboards.main_menu import main_menu, start_menu

ACCOUNT_MANAGER_ID = 688774573

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())


class ApplicationForm(StatesGroup):
    name = State()
    age = State()
    city = State()
    height = State()
    experience = State()
    photos = State()
    contact = State()
    motivation = State()
    confirm = State()

experience_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Да")],
        [KeyboardButton(text="❌ Нет")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

photo_type_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📸 Да")],
        [KeyboardButton(text="📷 Только обычные")],
        [KeyboardButton(text="❌ Пока нет")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

confirm_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Отправить"), KeyboardButton(text="⬅️ Назад")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🏠 Добро пожаловать!\n\n"
        "Рады приветствовать вас в PRESIDENT.\n\n"
        "Нажмите кнопку ниже, чтобы познакомиться с PRESIDENT.",
        reply_markup=start_menu
    )


@dp.message(lambda message: message.text == "📖 О агентстве")
async def about(message: Message):
    await message.answer(
        "📖 О PRESIDENT\n\n"
        "Добро пожаловать в PRESIDENT. ✨\n\n"
        "PRESIDENT — это приватное модельное агентство, которое помогает девушкам уверенно начать карьеру в индустрии моделинга.\n\n"
        "Мы сопровождаем наших моделей на каждом этапе сотрудничества: от первого знакомства до профессионального развития.\n\n"
        "🤝 Для нас важны безопасность, конфиденциальность, комфорт и уважительное отношение к каждой модели.\n\n"
        "Наша цель — создать условия, в которых каждая девушка сможет раскрыть свой потенциал, развиваться и достигать поставленных целей вместе с нашей командой. 💙"
    )


@dp.message(lambda message: message.text == "💎 Наши преимущества")
async def advantages(message: Message):
    await message.answer(
        "💎 Наши преимущества\n\n"
        "✨ Индивидуальный подход к каждой модели.\n\n"
        "🤝 Персональный менеджер и поддержка на каждом этапе.\n\n"
        "📈 Помощь в профессиональном развитии.\n\n"
        "🔒 Полная конфиденциальность.\n\n"
        "🛡 Комфортные и безопасные условия сотрудничества.\n\n"
        "💬 Всегда остаёмся на связи и готовы помочь."
    )


@dp.message(lambda message: message.text == "📋 Требования")
async def requirements(message: Message):
    await message.answer(
        "📋 Требования\n\n"
        "🔞 Возраст от 18 лет.\n\n"
        "✨ Ухоженный внешний вид.\n\n"
        "💬 Коммуникабельность и ответственность.\n\n"
        "📱 Наличие Telegram для связи.\n\n"
        "💙 Опыт работы приветствуется, но не обязателен — всему обучим и подробно расскажем о сотрудничестве."
    )


@dp.message(lambda message: message.text == "💼 Условия сотрудничества")
async def cooperation(message: Message):
    await message.answer(
        "💼 Условия сотрудничества\n\n"
        "🤝 За каждой моделью закрепляется персональный менеджер.\n\n"
        "📅 Индивидуальный график сотрудничества.\n\n"
        "💬 Постоянная поддержка команды.\n\n"
        "🔒 Конфиденциальность и уважение личных границ.\n\n"
        "💙 Мы создаём максимально комфортные условия для сотрудничества."
    )


@dp.message(lambda message: message.text == "💰 Доход и выплаты")
async def income(message: Message):
    await message.answer(
        "💰 Доход и выплаты\n\n"
        "💳 Выплаты осуществляются своевременно.\n\n"
        "📈 Доход зависит от активности, опыта и графика.\n\n"
        "🤝 Все условия обсуждаются заранее.\n\n"
        "💙 Мы придерживаемся честных и прозрачных условий сотрудничества."
    )


@dp.message(lambda message: message.text == "🛡 Безопасность")
async def safety(message: Message):
    await message.answer(
        "🛡 Безопасность\n\n"
        "🔒 Конфиденциальность каждой модели является нашим главным приоритетом.\n\n"
        "🤝 Персональный менеджер всегда находится на связи.\n\n"
        "💬 Мы готовы ответить на любые вопросы и помочь в любой ситуации.\n\n"
        "💙 Наша задача — создать комфортные и безопасные условия для каждой модели."
    )


@dp.message(lambda message: message.text == "❓ FAQ")
async def faq(message: Message):
    await message.answer(
        "❓ Часто задаваемые вопросы\n\n"
        "❔ Нужен ли опыт?\n"
        "Нет. Мы готовы работать как с начинающими, так и с опытными моделями.\n\n"
        "❔ Есть ли обучение?\n"
        "Да. Мы подробно расскажем обо всех этапах сотрудничества.\n\n"
        "❔ Можно ли совмещать с учёбой или работой?\n"
        "Да. График обсуждается индивидуально.\n\n"
        "❔ Как попасть в агентство?\n"
        "Нажмите кнопку «📝 Подать заявку» и заполните анкету."
    )


@dp.message(lambda message: message.text == "📞 Контакты")
async def contacts(message: Message):
    await message.answer(
        "📞 Контакты\n\n"
        "👤 Менеджер:\n"
        "@lowrider38\n\n"
        "💬 Мы всегда готовы ответить на ваши вопросы.\n\n"
        "🕘 Работаем ежедневно.",
        reply_markup=main_menu
    )


@dp.message(lambda message: message.text == "🤝 Познакомиться с PRESIDENT")
async def meet_president(message: Message):
    await message.answer(
        "🤝 Познакомиться с PRESIDENT\n\n"
        "Добро пожаловать в PRESIDENT! Это приватное модельное агентство, которое помогает девушкам уверенно начать карьеру в индустрии модельного бизнеса.\n\n"
        "Выберите интересующий раздел или нажмите кнопку \"📝 Подать заявку\" для участия.",
        reply_markup=main_menu
    )


@dp.message(lambda message: message.text == "📝 Подать заявку")
async def application(message: Message, state: FSMContext):
    await state.set_state(ApplicationForm.name)
    await message.answer(
        "Спасибо за интерес к агентству PRESIDENT! 💙\n\n"
        "Пожалуйста, ответьте на несколько вопросов.\n\n"
        "**1. Как вас зовут?**\n\n"
        "✍️ Введите имя.\n\n"
        "---\n\n"
        "**2. Сколько вам лет?**\n"
        "🔞 Укажите полный возраст.\n\n"
        "**3. В каком городе вы проживаете?**\n"
        "📍 Напишите город.\n\n"
        "**4. Какой у вас рост?**\n"
        "📏 Например: 172 см.\n\n"
        "**5. Есть ли опыт работы моделью?**\n"
        "- ✅ Да\n"
        "- ❌ Нет\n\n"
        "**6. Есть ли у вас профессиональные фотографии?**\n"
        "- 📸 Да\n"
        "- 📷 Только обычные\n"
        "- ❌ Пока нет\n\n"
        "**7. Прикрепите 2–5 фотографий**\n"
        "Желательно:\n"
        "- портрет;\n"
        "- фото в полный рост;\n"
        "- без сильной обработки.\n\n"
        "**8. Ссылка на Instagram или Telegram (по желанию)**\n"
        "📱 Напишите ссылку или никнейм.\n\n"
        "**9. Почему вы хотите стать моделью в PRESIDENT?**\n"
        "✍️ Коротко расскажите о себе.\n\n"
        "Начнем с первого вопроса: как вас зовут?",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(ApplicationForm.name)
async def answer_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ApplicationForm.age)
    await message.answer(
        "2. Сколько вам лет?\n\n🔞 Укажите полный возраст.",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(ApplicationForm.age)
async def answer_age(message: Message, state: FSMContext):
    if not message.text or not message.text.isdigit():
        await message.answer("Пожалуйста, укажите возраст цифрами, например 23.")
        return

    await state.update_data(age=message.text)
    await state.set_state(ApplicationForm.city)
    await message.answer("3. В каком городе вы проживаете?\n\n📍 Напишите город.")


@dp.message(ApplicationForm.city)
async def answer_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    await state.set_state(ApplicationForm.height)
    await message.answer("4. Какой у вас рост?\n\n📏 Например: 172 см.")


@dp.message(ApplicationForm.height)
async def answer_height(message: Message, state: FSMContext):
    await state.update_data(height=message.text)
    await state.set_state(ApplicationForm.experience)
    await message.answer(
        "5. Есть ли опыт работы моделью?",
        reply_markup=experience_keyboard,
    )


@dp.message(ApplicationForm.experience)
async def answer_experience(message: Message, state: FSMContext):
    await state.update_data(experience=message.text)
    await state.set_state(ApplicationForm.photos)
    await message.answer(
        "6. Есть ли у вас профессиональные фотографии?",
        reply_markup=photo_type_keyboard,
    )


@dp.message(ApplicationForm.photos)
async def answer_photos(message: Message, state: FSMContext):
    if message.text and message.text in ["📸 Да", "📷 Только обычные", "❌ Пока нет"]:
        await state.update_data(photo_type=message.text)
        # If user has professional photos, ask them to attach 2-5 photos now.
        if message.text == "📸 Да":
            await state.set_state(ApplicationForm.photos)
            await state.update_data(photos=[])
            await message.answer(
                "7. Прикрепите 2–5 фотографий.\n\n"
                "Вы можете отправить их одним альбомом или по одному сообщению.\n"
                "Когда закончите — отправьте слово 'Готово'.",
                reply_markup=ReplyKeyboardRemove(),
            )
            return

        # For "Только обычные" or "Пока нет" — skip photo upload and ask for social/contact link.
        await state.set_state(ApplicationForm.contact)
        await message.answer(
            "8. Ссылка на Instagram или Telegram (по желанию).\n\n"
            "📱 Напишите ссылку или никнейм.",
        )
        return

    # If user sends 'Готово' to finish attaching photos
    if message.text and message.text.strip().lower() in ["готово", "done"]:
        data = await state.get_data()
        photos = data.get('photos') or []
        if len(photos) >= 2:
            await state.set_state(ApplicationForm.contact)
            await message.answer(
                "8. Ссылка на Instagram или Telegram (по желанию).\n\n"
                "📱 Напишите ссылку или никнейм.",
            )
            return
        await message.answer("Пожалуйста, прикрепите минимум 2 фотографии перед завершением (или отправьте ещё).")
        return

    # If message contains photos (single or album items), accumulate them
    if message.photo:
        # Get current list from state
        data = await state.get_data()
        current = data.get('photos') or []
        # Use the highest-resolution photo in this message
        file_id = message.photo[-1].file_id
        current.append(file_id)
        # Trim to max 5
        if len(current) > 5:
            await message.answer("Вы превысили лимит в 5 фотографий. Пожалуйста, отправьте заново (максимум 5).")
            await state.update_data(photos=[])
            return

        await state.update_data(photos=current)
        if 2 <= len(current) <= 5:
            # Automatically proceed when we have at least 2 photos
            await state.set_state(ApplicationForm.contact)
            await message.answer(
                "Фотографии получены.\n\n8. Ссылка на Instagram или Telegram (по желанию).\n📱 Напишите ссылку или никнейм.",
            )
            return

        # Ask for more photos if not enough yet
        await message.answer(f"Получено {len(current)} фото. Пришлите ещё {2 - len(current)} фото, или отправьте 'Готово' когда закончите.")
        return

    await message.answer(
        "Пожалуйста, выберите вариант или прикрепите фотографии.",
        reply_markup=photo_type_keyboard,
    )


@dp.message(ApplicationForm.contact)
async def answer_contact(message: Message, state: FSMContext):
    await state.update_data(contact=message.text)
    await state.set_state(ApplicationForm.motivation)
    await message.answer(
        "9. Почему вы хотите стать моделью в PRESIDENT?\n\n"
        "✍️ Коротко расскажите о себе."
    )


@dp.message(ApplicationForm.motivation)
async def answer_motivation(message: Message, state: FSMContext):
    await state.update_data(motivation=message.text)
    await state.set_state(ApplicationForm.confirm)
    await message.answer(
        "Проверьте пожалуйста данные и нажмите «✅ Отправить», чтобы отправить заявку.\n"
        "Если хотите отменить и вернуться назад, нажмите «⬅️ Назад».",
        reply_markup=confirm_keyboard,
    )


@dp.message(ApplicationForm.confirm)
async def confirm_submission(message: Message, state: FSMContext):
    if message.text == "✅ Отправить":
        data = await state.get_data()
        application_text = (
            f"Новая заявка от {data.get('name')}\n"
            f"Возраст: {data.get('age')}\n"
            f"Город: {data.get('city')}\n"
            f"Рост: {data.get('height')}\n"
            f"Опыт работы моделью: {data.get('experience')}\n"
            f"Профессиональные фотографии: {data.get('photo_type')}\n"
            f"Контакт: {data.get('contact')}\n"
            f"Почему хочет стать моделью: {data.get('motivation')}\n"
        )
        photos = data.get('photos') or []
        media = [InputMediaPhoto(media=file_id) for file_id in photos[:10]]
        try:
            if media:
                await bot.send_media_group(
                    chat_id=-1004453241318,
                    media=media,
                )
            await bot.send_message(
                chat_id=-1004453241318,
                text=application_text,
                parse_mode="Markdown",
            )
            print("✅ Анкета отправлена в канал")
        except Exception as e:
            print(f"❌ Ошибка отправки в канал: {e}")

        await state.clear()

        await message.answer(
            "✅ Спасибо!\n\n"
            "Ваша анкета успешно отправлена менеджеру.",
            parse_mode="Markdown",
        )
        await message.answer(
            "Если хотите, вы можете вернуться в меню и выбрать другой раздел.",
            reply_markup=main_menu
        )
        return

    if message.text == "⬅️ Назад":
        await state.clear()
        await message.answer(
            "Вы вернулись назад. Вы можете выбрать раздел или начать заявку снова.",
            reply_markup=main_menu,
        )
        return

    await message.answer(
        "Пожалуйста, используйте кнопки «✅ Отправить» или «⬅️ Назад».",
        reply_markup=confirm_keyboard,
    )


async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())