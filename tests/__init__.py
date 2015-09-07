import sys

if sys.version_info[0] == 2:
    from gdshortener_test_py2 import GDShortenerTest
elif sys.version_info[0] == 3:
    from .gdshortener_test_py3 import GDShortenerTest
else:
    print("Something broke.")
