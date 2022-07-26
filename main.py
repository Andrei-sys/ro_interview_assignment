# from data_structures.datacenter import Datacenter
import requests
import json
import time

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """
    for _ in range(max_retries):
        content = requests.get(URL)
        if content.status_code != 200:
            time.sleep(1)
            print("Trying to connect...")
            continue
        else:
            break
    json_response = content.json()
    return json_response
    # pass  # the rest of your logic here


def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)
    print(data)
    if not data:
        raise ValueError('No data to process')

    # datacenters = [
    #     Datacenter(key, value)
    #     for key, value in data.items()
    # ]

    # pass  # the rest of your logic here


if __name__ == '__main__':
    main()
