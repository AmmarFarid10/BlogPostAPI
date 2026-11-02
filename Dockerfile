FROM python:3.12-slim
WORKDIR /srv
COPY requirements.lock .
RUN pip install --no-cache-dir -r requirements.lock && useradd --uid 10001 --create-home app
COPY mysite ./mysite
RUN chown -R app /srv
USER app
EXPOSE 8000
CMD ["python", "mysite/manage.py", "runserver", "0.0.0.0:8000"]
