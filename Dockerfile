# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# COPYRIGHT https://github.com/TeamKillerX/DarkWeb
# CREATE CODING BY https://t.me/xtsea

# YOU BUILT YOUR OWN DOCKER YOU STUPID BRAIN

FROM rendyprojects/python:latest


RUN apt -qq update
RUN apt -qq install -y --no-install-recommends \
    curl \
    git \
    gnupg2 \
    unzip \
    wget \
    python3-pip \
    python3-dev \
    python3-venv \
    ffmpeg \
    libgl1-mesa-glx \
    python3-pymediainfo

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade pykillerx
RUN pip3 install --upgrade opencv-python setuptools pip


CMD [ "python3", "-m", "TigerX"]
