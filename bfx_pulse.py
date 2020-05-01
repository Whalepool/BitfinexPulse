from bfxapi.rest.bfx_rest import BfxRest

class BfxPulseClient:

  def __init__(self, API_KEY=None, API_SECRET=None, loop=None, logLevel='DEBUG', *args, **kwargs):
    self.rest = BfxRest(API_KEY=API_KEY, API_SECRET=API_SECRET, loop=loop, logLevel=logLevel, *args, **kwargs)

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

    if len(title) < 16 or len(title) > 120:
      raise Exception("Title must be 16-120 characters (was: {length})".format(length=len(title)))
    try:
      # [ PID, MTS, None, PUID, None, TITLE, CONTENT, None, None, IS_PIN, IS_PUBLIC, None, TAGS[], ATTACHMENTS[], None, LIKES, None, None, UID_LIKED ]
      response = await self.rest.post(endpoint, payload)
    except Exception as e:
      print("pulse/write error: ", e)
      raise
    else:
      return response


  async def history(self, isPublic):
    endpoint = 'auth/r/pulse/hist'
    payload = {
      'isPublic': isPublic
    }
    try:
      # response is list of post history
      response = await self.rest.post(endpoint, payload)
    except Exception as e:
      print("pulse/hist error: ", e)
      raise
    else:
      return response


  async def delete(self, pid):
    endpoint = 'auth/w/pulse/del'
    payload = {
      'pid': pid
    }
    try:
      # response is [1] if successful or [0] if pid not found
      response = await self.rest.post(endpoint, payload)
    except Exception as e:
      print("pulse/del error: ", e)
      raise
    else:
      return response
