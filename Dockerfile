FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /iconic-task
RUN python --version
COPY requirements.txt /iconic-task/
RUN pip install -r requirements.txt
COPY . /iconic-task/
ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
