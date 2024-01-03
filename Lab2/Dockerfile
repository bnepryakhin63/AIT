# Загрузка базового образа
ARG ubuntu_ver
FROM docker.io/library/ubuntu:${ubuntu_ver}

# Определение переменных среды
ENV DEBIAN_FRONTEND=noninteractive
ENV CUDA_VERSION=12.2
ENV CUDA_DISTRO=ubuntu2204
ENV CUDA_ARCH=x86_64
ENV OPENCV_VERSION=4.8.0
ENV BUILD_THREAD_COUNT=1

# Установка зависимостей
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    wget \
    unzip \
    yasm \
    pkg-config \
    libswscale-dev \
    libtbb2 \
    libtbb-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libavformat-dev \
    libpq-dev \
    libxine2-dev \
    libglew-dev \
    libtiff5-dev \
    zlib1g-dev \
    libjpeg-dev \
    libavcodec-dev \
    libavformat-dev \
    libavutil-dev \
    libpostproc-dev \
    libswscale-dev \
    libeigen3-dev \
    libtbb-dev \
    libgtk2.0-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    && rm -rf /var/lib/apt/lists/*

# Установка OpenCV
WORKDIR /opt/
RUN wget --no-check-certificate https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip && \
    unzip ${OPENCV_VERSION}.zip && \
    rm ${OPENCV_VERSION}.zip && \
    wget --no-check-certificate https://github.com/opencv/opencv_contrib/archive/${OPENCV_VERSION}.zip && \
    unzip ${OPENCV_VERSION}.zip && \
    rm ${OPENCV_VERSION}.zip && \
    mkdir /opt/opencv-${OPENCV_VERSION}/build && cd /opt/opencv-${OPENCV_VERSION}/build && \
    cmake \
        -DOPENCV_EXTRA_MODULES_PATH=/opt/opencv_contrib-${OPENCV_VERSION}/modules \
        -DWITH_CUDA=ON \
        -DCUDA_ARCH_BIN=${CUDA_ARCH} \
        -DCMAKE_BUILD_TYPE=RELEASE \
        -DCMAKE_INSTALL_PREFIX=/usr/local \
        .. && \
    make -j"${BUILD_THREAD_COUNT}" && \
    make install && \
    ldconfig && \
    rm -rf /opt/opencv-${OPENCV_VERSION} /opt/opencv_contrib-${OPENCV_VERSION}

# Установка python3-pip
RUN apt-get update && apt-get install -y python3-pip

# Установка библиотеки cv2 (OpenCV)
RUN pip3 install opencv-python

# Установка библиотеки cv2 (OpenCV) и конкретной версии NumPy
RUN pip3 install opencv-python==4.8.0.74 numpy==1.21.2

# Копирование кода в контейнер
COPY image_filters.py /usr/local/Dev/

# Копирование изображения в контейнер
COPY krasn.jpg /usr/local/Dev/image/krasn.jpg

# Команда по умолчанию
CMD ["python3", "/usr/local/Dev/image_filters.py"]
