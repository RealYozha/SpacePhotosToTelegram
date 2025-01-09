```txt
   _____                          ____  __          __                ______         ______     __                              
  / ___/____  ____ _________     / __ \/ /_  ____  / /_____  _____   /_  __/___     /_  __/__  / /__  ____ __________ _____ ___ 
  \__ \/ __ \/ __ `/ ___/ _ \   / /_/ / __ \/ __ \/ __/ __ \/ ___/    / / / __ \     / / / _ \/ / _ \/ __ `/ ___/ __ `/ __ `__ \
 ___/ / /_/ / /_/ / /__/  __/  / ____/ / / / /_/ / /_/ /_/ (__  )    / / / /_/ /    / / /  __/ /  __/ /_/ / /  / /_/ / / / / / /
/____/ .___/\__,_/\___/\___/  /_/   /_/ /_/\____/\__/\____/____/    /_/  \____/    /_/  \___/_/\___/\__, /_/   \__,_/_/ /_/ /_/ 
    /_/                                                                                            /____/                       
```

# Space photos to Telegram
> Readme for `3.1.0-beta.5`

> - [English](#english)
> - [Русский](#русский)

# English
## Installation
Python3 should be already installed (tip: 3.12+ is recommended as <3.12 might break stuff).
The installation consists of 3 parts (if you have Python3 and pip3).
1. Downloading;
2. Installing dependencies;
3. Getting API keys;
To get the source, simply download it as a ZIP Package from GitHub.
Use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```bash
pip install -r requirements.txt
```
Then, rename the `.env.copy` file to `.env`.
Go to [NASA API](<https://api.nasa.gov/>) and get an API key. Paste it into the `.env` file on line 3, after you delete the placeholder.
Go to [BotFather @ Telegram](<https://t.me/BotFather/>) and get your bot's token. Paste it into the `.env` file on line 2, instead of the placeholder.
Make sure to check `.env` and ensure you've set it up:
```env
IMAGES_DIRECTORY=("./images" or any other directory)
TG_BOT_TOKEN=(Your BotFather @ Telegram token)
NASA_API_TOKEN=(Your NASA API key)
STANDALONE_PUBLISHING_INTERVAL_MINUTES=(Interval time in minutes)
STANDALONE_PUBLISHING_ENABLED=(0 = NO, 1 = YES)
```

## Examples

## `main.py`
The main file. Combines all of the modules.
Running it will result in the program downloading photos from SpaceX, NASA: APOD and NASA: EPIC, running the standalone publishing script.
```bash
.../SpacePhotosToTelegram> python main.py
.../SpacePhotosToTelegram> <HTTP request data or any other debug data>
.../SpacePhotosToTelegram> <completed>
```
Final result:
- Downloaded photos
- Saved photos to .../SpaceToTelegram/SpaceImages (or your directory name in `.env`)
- Connected to a Telegram bot
- If the bot is in channels, automatically post photos every set amount of time.

## `apod.py` and `epic.py`
Downloads APOD / EPIC correspondingly.
```bash
.../SpacePhotosToTelegram> python apod.py
.../SpacePhotosToTelegram> <HTTP request data or any other debug data>
.../SpacePhotosToTelegram> <downloaded images into imgdir>
.../SpacePhotosToTelegram> python epic.py
.../SpacePhotosToTelegram> <HTTP request data or any other debug data>
.../SpacePhotosToTelegram> <downloaded images into imgdir>
```

### `get_apod(api_key: str, number: int)` and `get_epic(api_key: str, number: int)`
Gets a set amount of APODs / EPICs using the API, with no edits.

Parameters:
- `api_key`: `str`; The API key.
- `number`: `int`; The amount of pictures.
Returns:
- `file_url`: `url`; The file URL.

### `get_apods(api_key: str, count: int)` and `get_epics(api_key: str)`
Yields the current thread until got any response from `get_apod()` or `get_epic()` with a tickrate of 6 requests per minute.

Parameters:
- `api_key`: `str`; The API key.
- `count`: `int`; The amount of pictures.

## `spacex_launches.py`
Downloads SpaceX launches.
```bash
.../SpacePhotosToTelegram> python spacex.py -id 8080
.../SpacePhotosToTelegram> <HTTP request data or any other debug data>
.../SpacePhotosToTelegram> <completed>
```

### `fetch_launch(id?: int or str)`
Fetches the launch by ID or the latest launch.
Parameters:
- `id`?: `int` or `str`; The launch ID.

## `filestream.py`
A library for required file operations.

### `remake_directory(path: str)`
Destroys and then creates a directory within the current path which results in the images being flushed.

Parameters:
- `path`: `str`; The path. (*Example: ./New_Folder Name/123/*)

### `get_file_extension(file_link: str)`
Gets the file extenstion.
Parameters:
- `file_link`: `str`; The file link. Can be a URL or a local path.

### `get_filename_from_url(url: str)`
Gets the filename from a URL.
Parameters:
- `url`: `str`; The file URL. Can be a local path.

### `download_image(url: str, file_path_and_ext: str, dir: str=ENV.IMAGES_DIRECTORY)`
Yields the current thread until got any response from the required URL with a tickrate of 12 requests per minute and the max possible attempts being 100.
Parameters:
- `url`: `str`; The file URL.
- `file_path_and_ext`: `str`; The path and filename where the file should be downloaded.
 - Requires the file's extension!

## `convert.py`
Required for `epic.py` to work.

### `change_splitter(before: str, current_splitter: str, next_splitter: str)`
Changes a symbol in a string to another symbol.
*Example: change_splitter("file/name", "/", "_") --> "file_name"*
Parameters:
- `before`: `str`; The string.
- `current_splitter`: `str`; The current splitter in the string.
- `next_splitter`: `str`; The new splitter character.

## `telegram_shorthands.py`
The file for Telegram Bot creations and operations.

### `Bot`
A Telegram Bot instance.
```bash
.../SpacePhotosToTelegram> <Creating object Bot with token X>
.../SpacePhotosToTelegram> <RET << obj Bot with its functions>
```
#### `__init__(self, token: str)`
Setups the class instance.
Parameters:
- `token`: `str`; The Telegram Bot token.

#### `publish_photo(self, chat_id: str, path: str)`
Publishes the given photo in the given chat.
Parameters:
- `chat_id`: `str`; The chat ID. (*Example: "@MyChannel, aBcD123"*)
- `path`: `str`; The image path.

## `standalone_publishing.py`
The standalone publishing script.

### `run_standalone_bot(bot: Bot, wait_mins: int)`
Runs the standalone publishing bot.
Parameters:
- `bot`: `telegram_shorthands.Bot`; The bot.
- `wait_mins`: `int`; The amount of time to wait.

# Русский
## Установка
Python3 уже должен быть установлен (совет: рекомендуется 3.12+, так как <3.12 может сломать что-то).
Установка состоит из 3 частей (если у вас есть Python3 и pip3).
1. Загрузка;
2. Установка зависимостей;
3. Получение ключей API;
Чтобы получить исходный код, просто загрузите его в виде ZIP-пакета с GitHub.
Используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:
```bash
pip install -r requirements.txt
```
Затем переименуйте файл `.env.copy` в `.env`.
Перейдите в [NASA API](<https://api.nasa.gov/>) и получите ключ API. Вставьте его в файл `.env` в строке 3 после удаления заполнителя.
Перейдите на [BotFather @ Telegram](<https://t.me/BotFather/>) и получите токен вашего бота. Вставьте его в файл `.env` на строке 2 вместо заполнителя.
Не забудьте проверить `.env` и убедиться, что вы настроили его:
```env
IMAGES_DIRECTORY=("./images" или любой другой каталог)
TG_BOT_TOKEN=(Ваш токен BotFather @ Telegram)
NASA_API_TOKEN=(Ваш ключ API NASA)
STANDALONE_PUBLISHING_INTERVAL_MINUTES=(Интервал времени в минутах)
STANDALONE_PUBLISHING_ENABLED=(0 = НЕТ, 1 = ДА)
```

## Примеры

## `main.py`
Основной файл. Объединяет все модули.
Запуск приведет к загрузке программой фотографий из SpaceX, NASA: APOD и NASA: EPIC, запуску автономного скрипта публикации.

```bash
.../SpacePhotosToTelegram> python main.py
.../SpacePhotosToTelegram> <данные HTTP-запроса или любые другие отладочные данные>
.../SpacePhotosToTelegram> <завершено>
```
Конечный результат:
- Загруженные фотографии
- Сохраненные фотографии в .../SpaceToTelegram/SpaceImages (или в имя вашего каталога в `.env`)
- Подключен к боту Telegram
- Если бот находится в каналах, автоматически публикует фотографии через заданное время.

## `apod.py` и `epic.py`
Загружает APOD / EPIC соответственно.

```bash
.../SpacePhotosToTelegram> python apod.py
.../SpacePhotosToTelegram> <данные HTTP-запроса или любые другие отладочные данные>
.../SpacePhotosToTelegram> <загруженные изображения в imgdir>
.../SpacePhotosToTelegram> python epic.py
.../SpacePhotosToTelegram> <данные HTTP-запроса или любые другие отладочные данные>
.../SpacePhotosToTelegram> <загруженные изображения в imgdir>
```

### `get_apod(api_key: str, number: int)` и `get_epic(api_key: str, number: int)`
Получает заданное количество APOD/EPIC с помощью API, без редактирования.

Параметры:
- `api_key`: `str`; Ключ API.
- `number`: `int`; Количество изображений.
Возвращает:
- `file_url`: `url`; URL-адрес файла.

### `get_apods(api_key: str, count: int)` и `get_epics(api_key: str)`
Возвращает текущий поток, пока не будет получен ответ от `get_apod()` или `get_epic()` с частотой 6 запросов в минуту.

Параметры:
- `api_key`: `str`; Ключ API.
- `count`: `int`; Количество изображений.

## `spacex_launches.py`
Загрузки запусков SpaceX.

```bash
.../SpacePhotosToTelegram> python spacex.py -id 8080
.../SpacePhotosToTelegram> <данные HTTP-запроса или любые другие отладочные данные>
.../SpacePhotosToTelegram> <завершено>
```

### `fetch_launch(id?: int или str)`
Выбирает запуск по идентификатору или последний запуск.
Параметры:
- `id`?: `int` или `str`; Идентификатор запуска.

## `filestream.py`
Библиотека для необходимых операций с файлами.

### `remake_directory(path: str)`
Уничтожает и затем создает каталог в текущем пути, что приводит к очистке изображений.

Параметры:
- `path`: `str`; Путь. (*Пример: ./New_Folder Name/123/*)

### `get_file_extension(file_link: str)`
Получает расширение файла.

Параметры:
- `file_link`: `str`; Ссылка на файл. Может быть URL или локальным путем.

### `get_filename_from_url(url: str)`
Получает имя файла из URL.

Параметры:
- `url`: `str`; URL файла. Может быть локальным путем.

### `download_image(url: str, file_path_and_ext: str, dir: str=ENV.IMAGES_DIRECTORY)`
Возвращает текущий поток, пока не будет получен ответ от требуемого URL с частотой 12 запросов в минуту и ​​максимально возможным количеством попыток 100.
Параметры:
- `url`: `str`; URL-адрес файла.
- `file_path_and_ext`: `str`; Путь и имя файла, куда следует загрузить файл.
- Требуется расширение файла!

## `convert.py`
Требуется для работы `epic.py`.

### `change_splitter(before: str, current_splitter: str, next_splitter: str)`
Заменяет символ в строке на другой символ.

*Пример: change_splitter("file/name", "/", "_") --> "file_name"*
Параметры:
- `before`: `str`; Строка.
- `current_splitter`: `str`; Текущий разделитель в строке.
- `next_splitter`: `str`; Новый символ разделителя.

## `telegram_shorthands.py`
Файл для создания и работы бота Telegram.

### `Bot`
Экземпляр бота Telegram.
```bash
.../SpacePhotosToTelegram> <Создание объекта Bot с токеном X>
.../SpacePhotosToTelegram> <RET << obj Bot с его функциями>
```
#### `__init__(self, token: str)`
Настраивает экземпляр класса.
Параметры:
- `token`: `str`; Токен бота Telegram.

#### `publish_photo(self, chat_id: str, path: str)`
Публикует указанную фотографию в указанном чате.

Параметры:
- `chat_id`: `str`; Идентификатор чата. (*Пример: "@MyChannel, aBcD123"*)
- `path`: `str`; Путь к изображению.

## `standalone_publishing.py`
Автономный скрипт публикации.

### `run_standalone_bot(bot: Bot, wait_mins: int)`
Запускает автономного бота публикации.

Параметры:
- `bot`: `telegram_shorthands.Bot`; Бот.
- `wait_mins`: `int`; Время ожидания.

```
Made by
__/\\\________/\\\_______/\\\\\_______/\\\\\\\\\\\\\\\_____/\\\\\\\\\\\____/\\\\\\\\\\\\\\\_        
 _\///\\\____/\\\/______/\\\///\\\____\////////////\\\____/\\\/////////\\\_\///////\\\/////__       
  ___\///\\\/\\\/______/\\\/__\///\\\____________/\\\/____\//\\\______\///________\/\\\_______      
   _____\///\\\/_______/\\\______\//\\\_________/\\\/_______\////\\\_______________\/\\\_______     
    _______\/\\\_______\/\\\_______\/\\\_______/\\\/____________\////\\\____________\/\\\_______    
     _______\/\\\_______\//\\\______/\\\______/\\\/_________________\////\\\_________\/\\\_______   
      _______\/\\\________\///\\\__/\\\______/\\\/____________/\\\______\//\\\________\/\\\_______  
       _______\/\\\__________\///\\\\\/______/\\\\\\\\\\\\\\\_\///\\\\\\\\\\\/_________\/\\\_______ 
        _______\///_____________\/////_______\///////////////____\///////////___________\///________
© YOZST, 2024-2025.
```
