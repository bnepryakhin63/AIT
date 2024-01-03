import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def process_image(input_path, output_path, class_labels):
    # Загрузка изображения
    input_image = Image.open(input_path)

    # Предварительная обработка изображения
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)  # добавляем размерность пакета

    # Загрузка предобученной модели ResNet
    model = resnet50(pretrained=True)
    model.eval()

    # Получение предсказаний
    with torch.no_grad():
        output = model(input_batch)

    # Преобразование выходных данных в вероятности и индекс предсказанного класса
    softmax = torch.nn.Softmax(dim=1)
    probabilities = softmax(output)[0]
    predicted_prob, predicted_class = torch.max(output, 1)

     # Получение текстового описания предсказанного класса
    class_description = class_labels[predicted_class.item()]

    # Создание изображения с подписью
    image_with_label = transforms.ToPILImage()(input_tensor.squeeze(0))

    # Создание объекта ImageDraw
    draw = ImageDraw.Draw(image_with_label)

    # Определение шрифта для подписи
    font = ImageFont.load_default()

    # Вывод предсказания на изображение
    label_text = f"Predicted Class: {class_description} (Probability: {predicted_prob.item():.2f})"
    draw.text((10, 10), label_text, (255, 255, 255), font=font)
    print(label_text)
    # Сохранение результата в файл
    image_with_label.save(output_path)

if __name__ == "__main__":
    input_image_path = "/usr/local/Dev/image/img2.jpg"
    output_result_path = "/usr/local/Dev/image/output/output_img2.jpg"

    # Загрузка классов ImageNet
    url = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
    response = requests.get(url)
    class_labels = response.json()

    process_image(input_image_path, output_result_path, class_labels)