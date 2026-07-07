# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

def _get_version():
    if "packageVersion" in os.environ:
        return os.environ["packageVersion"]
    # botbuilder/integration/aiohttp/about.py → 3 levels up to sdist root
    pkg_info = os.path.join(os.path.dirname(__file__), "..", "..", "..", "PKG-INFO")
    try:
        import email.parser
        with open(pkg_info, encoding="utf-8") as f:
            return email.parser.Parser().parse(f)["Version"]
    except Exception:
        return "4.15.0"

__title__ = "botbuilder-integration-aiohttp"
__version__ = _get_version()
__uri__ = "https://www.github.com/Microsoft/botbuilder-python"
__author__ = "Microsoft"
__description__ = "Microsoft Bot Framework Bot Builder"
__summary__ = "Microsoft Bot Framework Bot Builder SDK for Python."
__license__ = "MIT"
