FROM autogluon/autogluon:0.6.1-cpu-framework-ubuntu20.04-py3.8
ENTRYPOINT ["/bin/bash", "-l", "-c"]
WORKDIR /repository
COPY . .
RUN apt update -y
RUN apt install -y libpq-dev
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python uvicorn app.main:app --host 0.0.0.0 --port 8000