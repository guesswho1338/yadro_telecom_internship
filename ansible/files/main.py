import requests
import logging

logging.basicConfig(
        filename='log',
        encoding='utf-8',
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.INFO)

# функция задания url для получения рандомного статус кода (можно передавать свой список нужных статус кодов)
def generate_url(code_range: str = "100-103,200-208,226,300-308,400-431,440,444,449-451,460,463,494-499,500-511,520-527,530,561") -> str:
    return f"https://httpstat.us/random/{code_range}"

# функция обработки запроса
def query(response) -> int:
    try:
        if response.status_code // 100 in (1,2,3):
            logging.info(f"Status code: {response.status_code}, Body: {response.text}")
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as err:
        logging.error(f"Request error: {err}")
        print(f'Error during doing request: {err}')

    return response.status_code

codes = {'1xx':0,'2xx':0,'3xx':0,'4xx':0,'5xx':0}

# выполнение и обработка запросов, подсчет статус кодов
logging.info("Script started")
for i in range(5):
    try:
        r = requests.get(generate_url(), timeout=15)
        logging.info(f"Request {i+1} sent to {r.url}")
        codes[str(query(r))[0]+"xx"]+=1
    except requests.exceptions.ReadTimeout: # если попадаются статус коды 100 или 103, то выкидываем Exception, так как будет вечное ожидание
        logging.warning(f"Requests {i+1} timed out")
        print(f"Request {i+1} timed out")


# вывод результата работы скрипта
print("Result of script:")
logging.info(f"Result of script: {codes}")
for i, j in codes.items():
    print(i, ": ", j, sep='')
