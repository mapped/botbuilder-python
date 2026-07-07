# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from setuptools import setup


def _resolve_version():
    # CI sets packageVersion when building the release sdist.
    if "packageVersion" in os.environ:
        return os.environ["packageVersion"]
    # When uv/pip rebuilds an already-published sdist, packageVersion is not set,
    # but PKG-INFO from the sdist is present next to setup.py; read Version from it
    # so the rebuilt wheel's metadata matches the sdist's index metadata (uv >=0.4
    # rejects mismatches with 'Package metadata version X does not match given Y').
    pkg_info = os.path.join(os.path.dirname(os.path.abspath(__file__)), "PKG-INFO")
    if os.path.isfile(pkg_info):
        import email.parser
        with open(pkg_info, encoding="utf-8") as f:
            version = email.parser.Parser().parse(f).get("Version")
            if version:
                return version
    return "4.15.0"


VERSION = _resolve_version()
REQUIRES = [
    "botbuilder-schema==4.14.0",
    "botframework-connector-forked>=1.0.15",
]

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, "botframework", "streaming", "about.py")) as f:
    package_info = {}
    info = f.read()
    exec(info, package_info)

with open(os.path.join(root, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=package_info["__title__"] + "-forked",
    version=VERSION,
    url=package_info["__uri__"],
    author=package_info["__author__"],
    description=package_info["__description__"],
    keywords=[
        "BotFrameworkStreaming",
        "bots",
        "ai",
        "botframework",
        "botframework",
    ],
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license=package_info["__license__"],
    packages=[
        "botframework.streaming",
        "botframework.streaming.payloads",
        "botframework.streaming.payloads.assemblers",
        "botframework.streaming.payloads.disassemblers",
        "botframework.streaming.payloads.models",
        "botframework.streaming.payload_transport",
        "botframework.streaming.transport",
        "botframework.streaming.transport.web_socket",
    ],
    install_requires=REQUIRES,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
