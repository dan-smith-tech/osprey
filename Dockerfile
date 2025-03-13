FROM node:22-alpine AS client-builder 
WORKDIR /client
COPY client/package*.json ./
RUN npm install
COPY client/ ./
RUN npm run build

FROM python:3.9-slim
WORKDIR /server
COPY server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY server/*.py ./
COPY server/static ./static
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "index:app"]
