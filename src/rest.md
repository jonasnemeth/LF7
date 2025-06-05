# REST

## Beispiel APIs

### Nominatim

> [API-Dokumentation](https://nominatim.org/release-docs/develop/api/Search/)

„Free-form query“ mit `q=`
* [https://nominatim.openstreetmap.org/search?format=json&q=dresden](https://nominatim.openstreetmap.org/search?format=json&q=dresden)

„Structured query“ mit `city=` und optional `countrycodes=`
* [https://nominatim.openstreetmap.org/search?format=json&city=dresden&countrycodes=de](https://nominatim.openstreetmap.org/search?format=json&city=dresden&countrycodes=de)

Mit `format=xml`
* [https://nominatim.openstreetmap.org/search?format=xml&city=dresden&countrycodes=de](https://nominatim.openstreetmap.org/search?format=xml&city=dresden&countrycodes=de)

Ohne `format=`
* [https://nominatim.openstreetmap.org/search?city=dresden&countrycodes=de](https://nominatim.openstreetmap.org/search?city=dresden&countrycodes=de)


### [Swagger Petstore](https://petstore.swagger.io/)


### Dokumentation

Benötigte Informationen über API-Endpunkte:
* URL (Protokoll, Host, Port, **Pfad**)
* **HTTP-Methode**
* Query **Parameter**
* Request Body
* Request Header (z.B. Authorization)
* Responese Body
  * **MimeType** (z.B. application/json)
  * Encoding (z.B. UTF-8)
  * **Schema** (z.B. [JSON-Schema](https://json-schema.org/), DTD)

> Empfehlung: [**OpenAPI** Specification / **Swagger**](https://swagger.io/specification/) zur automatischen Dokumentation verwenden


## Beispiel Code

* [Node-RED](nodered.md)
* Python: [./examples/rest/python/](./examples/rest/python/)

## Sicherheit

[OWASP Top 10 Web Application Security Risks](https://owasp.org/www-project-top-ten/)

Relevante [IT-Grundschutz-Bausteine](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium/IT_Grundschutz_Kompendium_Edition2023.pdf?__blob=publicationFile&v=4#download=1):

* CON.2 Datenschutz
* CON.8 Software-Entwicklung
* CON.10 Entwicklung von Webanwendungen
* APP.3.1 Webanwendungen und Webservices
* APP.3.2 Webserver

### Beispiel

**APP.3.1.A21 Sichere HTTP-Konfiguration bei Webanwendungen**

> Zum Schutz vor Clickjacking, Cross-Site-Scripting und anderen Angriffen SOLLTE der IT-Betrieb geeignete [HTTPResponse-Header](https://de.wikipedia.org/wiki/Liste_der_HTTP-Headerfelder) setzen. Dazu SOLLTEN mindestens die folgenden HTTP-Header verwendet werden:
> * [Content-Security-Policy](https://de.wikipedia.org/wiki/Content_Security_Policy),
> * [Strict-Transport-Security](https://de.wikipedia.org/wiki/HTTP_Strict_Transport_Security),
> * [Content-Type](https://de.wikipedia.org/wiki/Internet_Media_Type),
> * [X-Content-Type-Options](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html#x-content-type-options) sowie
> * [Cache-Control](https://de.wikipedia.org/wiki/Browser-Cache#Sicherheitsaspekte)

Weitere Infos bei [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html)
