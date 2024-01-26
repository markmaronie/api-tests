FROM python:3.12
WORKDIR /autotestsapi/
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD python -m pytest -s tests/