# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "tiny_petstore"
VERSION = "2.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Tiny Pet Store",
    author_email="hirose31@gmail.com",
    url="",
    keywords=["Swagger", "Tiny Pet Store"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['tiny_petstore=tiny_petstore.__main__:main']},
    long_description="""\
    This is a yet another example pet store API server using [Connexion](https://github.com/zalando/connexion) .  - [Repository](https://github.com/hirose31/connexion-tiny-petstore)  # search resource expression  ## examples  &#x60;&#x60;&#x60;jsonc // WHERE name &#x3D; &#39;foo&#39; AND age &gt; 20 {     \&quot;name\&quot;: \&quot;foo\&quot;,     \&quot;age\&quot;: {\&quot;&gt;\&quot;: 20} } &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60;jsonc // WHERE addresses.email like \&quot;%@example.org\&quot; {     \&quot;addresses.email\&quot;: {\&quot;like\&quot;: \&quot;%@example.org\&quot;} } &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60;jsonc // WHERE age &gt;&#x3D; 6 AND age &lt;&#x3D; 12 {     \&quot;age\&quot;: [\&quot;and\&quot;, {\&quot;&gt;&#x3D;\&quot;: 6}, {\&quot;&lt;&#x3D;\&quot;: 12}] } &#x60;&#x60;&#x60;  ## rules  &#x60;&#x60;&#x60; // FILTER {     ATTR: EXPR,     ATTR: EXPR,     ... } &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60; // ATTR column_name joined_table.column_name &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60; // EXPR // comparison expr { OP: VALUE } { OP: [VALUE, VALUE, ...] } VALUE # shorthand for { \&quot;&#x3D;&#x3D;\&quot;: VALUE }  // boolean expr [\&quot;or\&quot;, EXPR, EXPR, ...] [\&quot;and\&quot;, EXPR, EXPR, ...] &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60; // OP &#x3D;&#x3D; !&#x3D; in !in &gt; &gt;&#x3D; &lt; &lt;&#x3D; like !like &#x60;&#x60;&#x60; 
    """
)

