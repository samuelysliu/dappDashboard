#
FROM tiangolo/uvicorn-gunicorn:python3.8

ENV ENV_FILE=.env

#
WORKDIR /app

#
COPY ./requirements.txt /app/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#
COPY ./conf /app/conf
COPY ./controllers /app/controllers
COPY ./models /app/models
COPY ./router /app/router
COPY ./views /app/views
COPY ./main.py /app/main.py
COPY ./.env /app/.env

EXPOSE 5000
#
#CMD ["/start-reload.sh"]
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]
