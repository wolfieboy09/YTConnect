# YTConnect

The Python module to get data from YouTube `v0.0.1` (beta)
This can get a YouTuber's subscriber count, views and more!

## Installation

`ytconnect` is currently not published on PyPi, but you can install it from source:

```bash
git clone https://github.com/Knightbot63-Github/YTConnect
cd YTConnect
pip install -e .
```

## Example usage

Fetching information from `MrBeast`:

```py
from ytconnect import User

user = User("MrBeast6000") 
print(user.subscriber_count())
print(user.view_count())
```
