FROM nikolaik/python-nodejs:latest

WORKDIR /app

COPY API/package*.json ./
COPY generator/requirements.txt ./

RUN npm install
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "node", "API/." ]