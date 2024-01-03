FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-devel

# Установка необходимых библиотек
RUN pip install torch torchvision pillow

# Создание директории вывода
RUN mkdir -p /usr/local/Dev/image/output/

# Копирование скрипта обработки изображений в контейнер
COPY image_processing_script.py /app/image_processing_script.py

# Копирование изображения в контейнер
COPY img2.jpg /usr/local/Dev/image/img2.jpg

# Команда по умолчанию для выполнения скрипта при запуске контейнера
CMD ["python3", "/app/image_processing_script.py"]