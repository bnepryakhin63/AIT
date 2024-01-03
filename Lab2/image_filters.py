import numpy as np
import os
import cv2
print("Версия OpenCV:", cv2.__version__)

# Путь к директории для сохранения результатов
output_directory = '/usr/local/Dev/output/'
os.makedirs(output_directory, exist_ok=True)

# Путь к изображению внутри контейнера
image_path = '/usr/local/Dev/image/krasn.jpg'

def contrast_image(image, alpha, beta):
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted_image

def threshold_image(image, threshold_value):
    _, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return thresholded_image

# Загрузка изображения с помощью OpenCV
original_image = cv2.imread(image_path)

# Установка множителя контраста и смещения
contrast_multiplier = 1.5
contrast_offset = 30

# Применение контраста
result_image_contrast = contrast_image(original_image, contrast_multiplier, contrast_offset)

# Полный путь к файлу
output_path = os.path.join(output_directory, 'contrast_result.jpg')

# Сохранение изображения после контрастирования
cv2.imwrite(output_path, result_image_contrast)

# Установка значения порога
threshold_value = 127

# Применение пороговой обработки
result_image_threshold = threshold_image(original_image, threshold_value)

# Полный путь к файлу
output_path = os.path.join(output_directory, 'threshold_result.jpg')

# Сохранение изображения после пороговой обработки
cv2.imwrite(output_path, result_image_threshold)