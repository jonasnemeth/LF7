# badbank
example of how (not) to use REST + SQL


## ./example

* REST + OpenAPI
  * using [fastapi](https://fastapi.tiangolo.com/)

* [sqlite3](https://docs.python.org/3/library/sqlite3.html)


## ./basic\_auth

* [HTTP Basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication)
  * using [fastapi.security.HTTPBasic](https://fastapi.tiangolo.com/advanced/security/http-basic-auth/)

* [passlib.hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html) with [salt](https://en.wikipedia.org/wiki/Salt_(cryptography)) + [pepper](https://en.wikipedia.org/wiki/Pepper_(cryptography))

* enforce https


## ./injection

* examples of sql-injections
