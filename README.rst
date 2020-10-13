Projekt med Flask
=================

Kopiera filen ``.env-example`` till ``.env``. Den används till konfiguration av appen.

Starta flask med kommandot::

    poetry run flask run

När appen startat kan du besöka den på adressen http://127.0.0.1:5000.

Uppgift
-------

1. Skapa ett formulär för inmatning av SSID och lösenord för det WiFi som 
   QR-koden ska skapas för. Fälten ska heta `ssid` och `password`.

2. Rendera formuläret på index-routen.

3. Lägg till biblioteket `pyqrcodeng` i projektet med kommandot::

    poetry add pyqrcodeng

4. Rendera en QR-kod som en `<svg>`-tagg. För att åstadkomma det behöver du använda `io.BytesIO`::

    qr = pyqrcode.create(data)
    buffer = io.BytesIO()
    qr.svg(buffer, xmldecl=False, omithw=True)
    svg = buffer.getvalue().decode()
