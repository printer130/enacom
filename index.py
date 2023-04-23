from constants.list import list_to_scan
import requests
import json
import time

API_KEY = "5HNJDXmP1poJQU0VBLvahdiDgmMI0B0DemcsuqLC"

def get_data():
  for i, value in enumerate(list_to_scan):
    title = value[0]
    url = value[1]
    result = requests.get(url)

    with open(f"datasets/enacom_{str(i)}.json", 'w') as f:
      print(f'{i + 1} Dumping -> {title}')
      start = time.time()
      json.dump(result.json(), f)
      end = time.time()
      print("Time to fetch -> ", round(end - start, 5),"s")
      print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

get_data()