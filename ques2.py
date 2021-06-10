import requests
from requests.exceptions import HTTPError


def get_data(page_num: int):
    """Function to fetch data from the url according to page number.

    :param page_num: Page Number
    :return Number of users in that page
    :rtype int
    """
    url = f"https://reqres.in/api/users?page={page_num}"
    response = requests.get(url)        # Get the data
    if response.status_code == 200:     # Check if status code is 200 or not
        # data is a list within the json response
        data = response.json()["data"]
        return len(data)
    raise HTTPError()


if __name__ == '__main__':
    num_of_users = 0
    try:
        for i in range(1, 13):
            num_of_users += get_data(i)
        print(f"Number of users : {num_of_users}")
    except HTTPError:
        print("Could not fetch data from the url")
    except Exception:
        print("You have an internet issue. Please try again.")
