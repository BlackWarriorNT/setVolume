# SetVolume: Easy Volume Control

SetVolume — это простой скрипт для управления громкостью системы и отображения уведомлений с текущей громкостью, предназначенный для работы в Windows 10.

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/ваш_пользователь/SetVolume.git
    cd SetVolume
    ```

2. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

## Использование

Запустите скрипт с аргументом `plus` или `minus` для увеличения или уменьшения громкости, или укажите конкретное значение громкости от 0 до 100:

### Примеры

Увеличение громкости:

    python setVolume.py plus

Уменьшение громкости:

    python setVolume.py minus

Установка громкости на 50%:

    python setVolume.py 50
