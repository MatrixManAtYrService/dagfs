import re

import dagfs


def test_provider_info() -> None:
    provider_info = dagfs.get_provider_info()
    for version in provider_info["versions"]:
        assert re.match(r"[0-9]+\.[0-9]+\.[0-9]+.*", version)
