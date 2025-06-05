# [HTTP](https://de.wikipedia.org/wiki/Hypertext_Transfer_Protocol)

* Server + Clients
* Übertragung von Daten/Dateien
* Für jede Übertragung wird eine neue TCP-Verbindung auf- und abgebaut

## Layer

**5-7**

* baut auf TCP/IP (Layer 4/3) auf
* wenn SSL/TLS genutzt wird, ist es wie ein zusätzlicher Layer zwischen 4 und 5

## Ports

* **80** Standardport HTTP://
* 443 HTTPS://

## Methoden (Verben)

* **GET**
* **POST**
* PUT
* DELETE
* …

## Statuscodes

* **200** OK
* **301** Redirect
* **404** Not Found
* 503 Service Unavailable
* 418 I'm a Teapot

## HTTP-Response

> HTTP 1.1 200 OK       ## Protokoll-Version + Statuscode
>
> Content-Type: text/html
>
> …                     ## Weitere Header (key+value)
>
>                       ## Leerzeile
>
> \<html\>                ## Content
>
> …
>
> \</html\>
