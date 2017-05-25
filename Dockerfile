FROM python
WORKDIR /home
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get install git -y
RUN rm -rf /var/lib/apt/lists/*
RUN git clone https://github.com/GabrielRocha/desafio-back-end.git
WORKDIR /home/desafio-back-end
RUN pip install -r requirements.pip
CMD gunicorn app:app -b 0.0.0.0:5000
EXPOSE 5000