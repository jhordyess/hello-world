FROM python:3
ARG USER_NAME=jhordyess
ARG USER_UID=1000
ARG USER_GID=$USER_UID
# Update
RUN apt-get update --no-install-recommends \
  && apt-get upgrade -y \
  && apt-get autoremove --purge -y
# Add noon-root user, source: https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user
RUN groupadd --gid $USER_GID $USER_NAME \
  && useradd --uid $USER_UID --gid $USER_GID -m $USER_NAME
RUN apt-get install -y sudo \
  && echo $USER_NAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USER_NAME \
  && chmod 0440 /etc/sudoers.d/$USER_NAME
# Set locale and timezone
ENV DEBIAN_FRONTEND=noninteractive 
RUN apt-get install -y locales locales-all tzdata
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.en
ENV TZ=America/La_Paz
#
RUN apt-get install -y git
USER ${USER_NAME}
WORKDIR /home/${USER_NAME}
RUN echo "alias update='sudo apt-get update --no-install-recommends;sudo apt-get upgrade -y;sudo apt-get autoremove --purge -y'" >> ~/.bashrc
RUN echo "alias nosave='clear;history -c'" >> ~/.bashrc
# PlatformIO
ENV PATH="${PATH}:~/.platformio/penv/bin"
RUN python3 -c "$(curl -fsSL https://raw.githubusercontent.com/platformio/platformio/master/scripts/get-platformio.py)"