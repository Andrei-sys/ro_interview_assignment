# region IMPORTS
from data_structures.datacenter import Datacenter
import json
import requests
import time
# endregion

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url: str, max_retries: int = 5, delay_between_retries: int = 1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.

    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """
    response = None
    if max_retries > 0:
        for i in range(max_retries):
            try:
                response = requests.get(url).content
            except Exception as e:
                print(f'Failed on retry# : {i} \nMessage : {e}')
                time.sleep(delay_between_retries)
    else:
        try:
            response = requests.get(url).content
        except:
            pass
    if response:
        return json.loads(response)
    else:
        return None


def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    pass  # the rest of your logic here


if __name__ == '__main__':
    main()
