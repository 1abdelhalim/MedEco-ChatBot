FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

ENV OPENAI_API_KEY="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"