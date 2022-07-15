FROM node:16
ARG USER_NAME=node
# Update
RUN apt-get update --no-install-recommends \
  && apt-get upgrade -y \
  && apt-get autoremove --purge -y
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
USER ${USER_NAME}
WORKDIR /home/${USER_NAME}
RUN echo "alias update='sudo apt-get update --no-install-recommends;sudo apt-get upgrade -y;sudo apt-get autoremove --purge -y'" >> ~/.bashrc
RUN echo "alias nosave='clear;history -c'" >> ~/.bashrc