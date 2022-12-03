import dagfs
import re

def test_provider_info():
    assert re.match(r"[0-9]\.[0-9]\.[0-9].*", dagfs.get_provider_info()["version"]
