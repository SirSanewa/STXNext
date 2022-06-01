import requests
from .models import Book


def data_from_api(author_name):
    api_response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={author_name}")
    try:
        api_response.json()["items"]
    except KeyError:
        return False
    import_amount = len(api_response.json()["items"])
    dict_list = []
    for book in api_response.json()["items"]:
        try:
            year = int(book["volumeInfo"]["publishedDate"].split("-")[0])
        except KeyError:
            year = None
        data = {
            "external_id": book["id"],
            "title": book["volumeInfo"]["title"],
            "authors": book["volumeInfo"].get("authors", []),
            "published_year": year,
            "thumbnail": book["volumeInfo"]["infoLink"]
        }
        dict_list.append(data)
    return dict_list, import_amount
