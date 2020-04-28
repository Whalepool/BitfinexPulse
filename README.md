# Bitfinex Pulse API Client

Extension of bitfinex-api-py to support the Bitfinex Pulse news feed

Supports the write, del, and hist methods

## Installation
clone it
```sh
pip3 install -r requirements.txt
python3 setup.py install
```

## Quickstart
```python
from bfx_pulse import BfxPulseClient
import asyncio

client = BfxPulseClient(
  API_KEY=''
  API_SECRET=''
)

response = await client.write('your first message title', 'message content')
t = asyncio.ensure_future(run())
asyncio.get_event_loop().run_until_complete(t)
```

