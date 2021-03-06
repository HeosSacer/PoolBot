from setuptools import setup

setup(
    name='PoolBot',
    version='0.1',
    packages=['src', 'src.utils', 'venv.lib.python3.5.site-packages.grpc', 'venv.lib.python3.5.site-packages.grpc.beta',
              'venv.lib.python3.5.site-packages.grpc._cython', 'venv.lib.python3.5.site-packages.grpc._cython._cygrpc',
              'venv.lib.python3.5.site-packages.grpc.framework',
              'venv.lib.python3.5.site-packages.grpc.framework.common',
              'venv.lib.python3.5.site-packages.grpc.framework.foundation',
              'venv.lib.python3.5.site-packages.grpc.framework.interfaces',
              'venv.lib.python3.5.site-packages.grpc.framework.interfaces.base',
              'venv.lib.python3.5.site-packages.grpc.framework.interfaces.face',
              'venv.lib.python3.5.site-packages.grpc.experimental', 'venv.lib.python3.5.site-packages.idna',
              'venv.lib.python3.5.site-packages.async', 'venv.lib.python3.5.site-packages.async.test',
              'venv.lib.python3.5.site-packages.click', 'venv.lib.python3.5.site-packages.flask',
              'venv.lib.python3.5.site-packages.flask.ext', 'venv.lib.python3.5.site-packages.google.protobuf',
              'venv.lib.python3.5.site-packages.google.protobuf.util',
              'venv.lib.python3.5.site-packages.google.protobuf.pyext',
              'venv.lib.python3.5.site-packages.google.protobuf.compiler',
              'venv.lib.python3.5.site-packages.google.protobuf.internal',
              'venv.lib.python3.5.site-packages.google.protobuf.internal.import_test_package',
              'venv.lib.python3.5.site-packages.jinja2', 'venv.lib.python3.5.site-packages.aiohttp',
              'venv.lib.python3.5.site-packages.asyncio', 'venv.lib.python3.5.site-packages.certifi',
              'venv.lib.python3.5.site-packages.chardet', 'venv.lib.python3.5.site-packages.chardet.cli',
              'venv.lib.python3.5.site-packages.discord', 'venv.lib.python3.5.site-packages.discord.ext',
              'venv.lib.python3.5.site-packages.discord.ext.ipc',
              'venv.lib.python3.5.site-packages.discord.ext.commands', 'venv.lib.python3.5.site-packages.urllib3',
              'venv.lib.python3.5.site-packages.urllib3.util', 'venv.lib.python3.5.site-packages.urllib3.contrib',
              'venv.lib.python3.5.site-packages.urllib3.contrib._securetransport',
              'venv.lib.python3.5.site-packages.urllib3.packages',
              'venv.lib.python3.5.site-packages.urllib3.packages.backports',
              'venv.lib.python3.5.site-packages.urllib3.packages.ssl_match_hostname',
              'venv.lib.python3.5.site-packages.requests', 'venv.lib.python3.5.site-packages.werkzeug',
              'venv.lib.python3.5.site-packages.werkzeug.debug', 'venv.lib.python3.5.site-packages.werkzeug.contrib',
              'venv.lib.python3.5.site-packages.backports.configparser', 'venv.lib.python3.5.site-packages.multidict',
              'venv.lib.python3.5.site-packages.markupsafe', 'venv.lib.python3.5.site-packages.sqlalchemy',
              'venv.lib.python3.5.site-packages.sqlalchemy.ext',
              'venv.lib.python3.5.site-packages.sqlalchemy.ext.declarative',
              'venv.lib.python3.5.site-packages.sqlalchemy.orm', 'venv.lib.python3.5.site-packages.sqlalchemy.sql',
              'venv.lib.python3.5.site-packages.sqlalchemy.util', 'venv.lib.python3.5.site-packages.sqlalchemy.event',
              'venv.lib.python3.5.site-packages.sqlalchemy.engine',
              'venv.lib.python3.5.site-packages.sqlalchemy.testing',
              'venv.lib.python3.5.site-packages.sqlalchemy.testing.suite',
              'venv.lib.python3.5.site-packages.sqlalchemy.testing.plugin',
              'venv.lib.python3.5.site-packages.sqlalchemy.dialects',
              'venv.lib.python3.5.site-packages.sqlalchemy.dialects.mssql',
              'venv.lib.python3.5.site-packages.sqlalchemy.dialects.mysql',
              'venv.lib.python3.5.site-packages.sqlalchemy.dialects.oracle',
              'venv.lib.python3.5.site-packages.sqlalchemy.dialects.sqlite',
              'venv.lib.python3.5.site-packages.sqlalchemy.dialects.sybase',
              'venv.lib.python3.5.site-packages.sqlalchemy.dialects.firebird',
              'venv.lib.python3.5.site-packages.sqlalchemy.dialects.postgresql',
              'venv.lib.python3.5.site-packages.sqlalchemy.databases',
              'venv.lib.python3.5.site-packages.sqlalchemy.connectors', 'venv.lib.python3.5.site-packages.websockets',
              'venv.lib.python3.5.site-packages.websockets.py35', 'venv.lib.python3.5.site-packages.autocorrect',
              'venv.lib.python3.5.site-packages.async_timeout', 'venv.lib.python3.5.site-packages.sqlite3database',
              'venv.lib.python3.5.site-packages.sqlite3database.helper',
              'venv.lib.python3.5.site-packages.flask_sqlalchemy',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip.req',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip.vcs',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip.utils',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip.compat',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip.models',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.distlib',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.distlib._backport',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.colorama',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.html5lib',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.html5lib._trie',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.html5lib.filters',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.html5lib.treewalkers',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.html5lib.treeadapters',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.html5lib.treebuilders',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.lockfile',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.progress',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.requests',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.requests.packages',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.requests.packages.chardet',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.requests.packages.urllib3',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.requests.packages.urllib3.util',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.requests.packages.urllib3.contrib',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.requests.packages.urllib3.packages',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.packaging',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.cachecontrol',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.cachecontrol.caches',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.webencodings',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip._vendor.pkg_resources',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip.commands',
              'venv.lib.python3.5.site-packages.pip-9.0.1-py3.5.egg.pip.operations'],
    url='https://github.com/HeosSacer/PoolBot',
    license='',
    author='HeosSacer',
    author_email='ee2marine@gmail.com',
    description=''
)
