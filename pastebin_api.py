# pastebin_api.py

import requests

def create_paste(title, body, duration, publicly_listed):
    """
    Creates a new PasteBin paste and returns the url.

    Parameters
    ----------
    title : str
        The title of the paste.
    body : str
        The body of the paste.
    duration : int
        The expiration duration of the paste.
        Should be one of the following:
        - 1 : 10 minutes
        - 2 : 1 hour
        - 4 : 1 day
        - 5 : 1 week
        - 6 : 2 weeks
        - 7 : 1 month
    publicly_listed : bool
        Whether the paste should be publicly listed or not.

    Returns
    -------
    str or None
        The URL of the newly created paste, or None
        if the creation failed.
    """
    data = {
        'title': title,
        'body': body,
        'expire': duration,
        'public': publicly_listed
    }
    url = 'https://pastebin.com/api/api_post.php'
    r = requests.post(url, data=data)
    if r.status_code == 200:
        return r.text
    else:
        print('Response code: {}'.format(r.status_code))
        return None
