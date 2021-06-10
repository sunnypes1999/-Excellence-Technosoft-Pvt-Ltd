import requests
from requests.exceptions import HTTPError


def get_posts():
    """Function to fetch data from the posts url.

    :return JSON data
    :rtype list
    """
    response = requests.get(
        "https://my-json-server.typicode.com/typicode/demo/posts")
    if response.status_code == 200:
        return response.json()
    raise HTTPError


def get_comments():
    """Function to fetch data from the comments url.

    :return JSON data
    :rtype list
    """
    response = requests.get(
        "https://my-json-server.typicode.com/typicode/demo/comments")
    if response.status_code == 200:
        return response.json()
    raise HTTPError


def combine_data(posts: list, comments: list):
    """Function to combine posts and comments data.

    :param posts: Posts data
    :param comments: Comments data
    :return Combined data of posts/comments
    :rtype list
    """
    for comment in comments:
        for post in posts:
            if comment["postId"] == post["id"]:
                post['comments'] = []
                post['comments'].extend(comment.values())
                break
            else:
                post.append(comment)
    return posts


if __name__ == '__main__':
    try:
        posts = get_posts()
        comments = get_comments()
        print(combine_data(posts, comments))
    except HTTPError:
        print("Could not fetch data from the url")
    except ValueError:
        print("You have an internet issue. Please try again.")
