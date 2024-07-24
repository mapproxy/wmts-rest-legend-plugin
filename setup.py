from setuptools import setup, find_packages

install_requires = [
    'MapProxy>=2.1.1'
]

readme = open('README.md', encoding="utf-8").read()

setup(
    name="wmts_rest_legend_plugin",
    python_requires='>=3.7',
    version="0.0.1",
    license="Apache 2.0",
    description="Plugin for MapProxy adding a WMTS rest service to deliver legends",
    long_description=readme,
    long_description_content_type='text/x-rst',
    author="Simon Seyock",
    author_email="seyock@terrestris.de",
    url="https://github.com/mapproxy/wmts_rest_legend_plugin",
    packages=find_packages(),
    include_package_data=True,
    package_data = {'': ['*.yaml']},
    install_requires=install_requires,

    # the following makes a plugin available to mapproxy
    entry_points={"mapproxy": ["wmts_rest_legend_plugin = wmts_rest_legend_plugin.pluginmodule"]},
    # custom PyPI classifier for mapproxy plugins
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    zip_safe = False
)
