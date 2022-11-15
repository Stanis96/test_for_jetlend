from typing import Optional
from urllib.request import urlopen
import json


def get_public_ip() -> Optional[str]:
    url = "https://ipinfo.io"
    ip = None
    try:
        with urlopen(url) as response:
            body = response.read()
        result = json.loads(body)
        ip = result.get("ip")
    except Exception as exc:
        print(repr(exc))
    return ip


if __name__ == "__main__":
    print(get_public_ip())
