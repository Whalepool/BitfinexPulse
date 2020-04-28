from bfxapi import Client

class BfxPulseClient:

  def __init__(self, API_KEY='', API_SECRET='', logLevel='DEBUG'):
    self.client = Client(API_KEY=API_KEY, API_SECRET=API_SECRET, logLevel=logLevel)

  async def write(self, title, content, isPublic=0, isPin=0, attachments=[]):
    # https://docs.bitfinex.com/reference#rest-auth-pulse-add
    endpoint = 'auth/w/pulse/add'
    payload = {
      'title': title,  # 16-120 characters
      'content': content,  # > 16 characters
      'isPublic': isPublic,  # 0 or 1
      'isPin': isPin,  # 0 or 1
      'attachments': attachments  # list of base64 strings
    }

    try:
      # [ PID, MTS, None, PUID, None, TITLE, CONTENT, None, None, IS_PIN, IS_PUBLIC, None, TAGS[], ATTACHMENTS[], None, LIKES, None, None, UID_LIKED ]
      response = await self.client.rest.post(endpoint, payload)
    except Exception as e:
      print("pulse/write error: ", e)
    else:
      return response


  async def history(self, isPublic):
    endpoint = 'auth/r/pulse/hist'
    payload = {
      'isPublic': isPublic
    }
    try:
      # response is list of post history
      response = await self.client.rest.post(endpoint, payload)
    except Exception as e:
      print("pulse/hist error: ", e)
    else:
      return response


  async def delete(self, pid):
    endpoint = 'auth/w/pulse/del'
    payload = {
      'pid': pid
    }
    try:
      # response is [1] if successful or [0] if pid not found
      response = await self.client.rest.post(endpoint, payload)
    except Exception as e:
      print("pulse/del error: ", e)
    else:
      return response
