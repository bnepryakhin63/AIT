#!/bin/bash

# Определение переменных
export ubuntu_ver=22.04
export cuda_ver=12-2
export cuda_distro=ubuntu2204
export cuda_arch=x86_64
export ocv_ver=4.8.0
export build_thread_count=1
export image_tag=bn_tag
export dockerfile=Dockerfile

# Проверка существования образа
if docker image inspect ubuntu:$ubuntu_ver 1>/dev/null; then
  echo "Docker image ubuntu:$ubuntu_ver is found."
else
  echo "Pulling docker image ubuntu:$ubuntu_ver..."
  docker pull ubuntu:$ubuntu_ver
fi

# Сборка Docker-образа
echo "Building docker image..."
docker build --tag $image_tag \
             --build-arg ubuntu_ver=$ubuntu_ver \
             --build-arg cuda_ver=$cuda_ver \
             --build-arg cuda_distro=$cuda_distro \
             --build-arg cuda_arch=$cuda_arch \
             --build-arg ocv_ver=$ocv_ver \
             --build-arg build_thread_count=$build_thread_count \
             -f $dockerfile .
