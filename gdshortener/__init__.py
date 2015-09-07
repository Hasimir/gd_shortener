import sys

if sys.version_info[0] == 2:
    from gdshortener_py2 import _IS_GD_SHORTENER_URL_
    from gdshortener_py2 import _V_GD_SHORTENER_URL_
    from gdshortener_py2 import GDBaseException
    from gdshortener_py2 import GDMalformedURLError
    from gdshortener_py2 import GDShortURLError
    from gdshortener_py2 import GDRateLimitError
    from gdshortener_py2 import GDGenericError
    from gdshortener_py2 import GDBaseShortener
    from gdshortener_py2 import ISGDShortener
    from gdshortener_py2 import VGDShortener
elif sys.version_info[0] == 3:
    from .gdshortener_py3 import _IS_GD_SHORTENER_URL_
    from .gdshortener_py3 import _V_GD_SHORTENER_URL_
    from .gdshortener_py3 import GDBaseException
    from .gdshortener_py3 import GDMalformedURLError
    from .gdshortener_py3 import GDShortURLError
    from .gdshortener_py3 import GDRateLimitError
    from .gdshortener_py3 import GDGenericError
    from .gdshortener_py3 import GDBaseShortener
    from .gdshortener_py3 import ISGDShortener
    from .gdshortener_py3 import VGDShortener
else:
    print("Something broke.")
