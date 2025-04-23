# helpers.py (COMPLETO)
import ssl
import urllib.request

def is_reachable(url):
    try:
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE

        with urllib.request.urlopen(url, context=ssl_ctx) as response:
            return response.status == 200
    except Exception as e:
        print(e)
        return False

