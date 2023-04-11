# Space-pictures-telegram-bot
Получает, сохраняет изображения от NASA API и SpaceX API, периодически отправляет изображение в Telegram.

- fetch_nasa_epic_images.py - получает и сохраняет изображения NASA EPIC.
- fetch_nasa_images.py - получает и сохраняет изображения от NASA API. 
- fetch_spacex_images.py - получает и сохраняет изображения от SpaceX API.
- space_pictures_telegram_bot.py - отправляет изображения в Telegram.
- nasa_api_utils.py - содержит несколько необходимых функций.
## Установка
Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
 
 ```
 pip install -r requirements.txt
 ```

## Настройка
Создать файл с расширением .env c переменными:
```
NASA_API_KEY=
TELEGRM_BOT_API_TOKEN=
```
- [NASA API](https://api.nasa.gov/)
- [Telegram API](https://core.telegram.org/api#bot-api)


## Запуск
Используйте `python` (или `python3`, есть конфликт с Python2) для запуска: 

```
python space_pictures_telegram_bot.py "id чата в Telegram"
``` 
- По умолчанию задан период отправки в 4 часа. Для изменения можно добавить аргумент `--p "количество часов"  ` 
- Для отправки конкретного файла используется аргумент `--f "путь к файлу"`
## Цели проекта
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте Devman.
