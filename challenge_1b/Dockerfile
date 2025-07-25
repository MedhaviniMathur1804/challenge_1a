FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get upgrade -y && apt-get clean
RUN pip install --no-cache-dir PyMuPDF==1.23.9 scikit-learn numpy

CMD ["python", "main.py", "docs", "PhD Researcher", "Prepare a comprehensive literature review"]
