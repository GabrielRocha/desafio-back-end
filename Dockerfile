FROM python
WORKDIR /home
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ADD requirements.pip /home
RUN pip install -r requirements.pip