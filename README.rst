Projekt med Flask
=================

Kopiera filen ``.env-example`` till ``.env``. Den används till konfiguration av appen.

Starta flask med kommandot::

    poetry run flask run

När appen startat kan du besöka den på adressen http://127.0.0.1:5000.


Uppgift
-------

1. Installera paketet flask-wtf med kommandot::

    poetry add flask-wtf

2. Skapa ett formulär för inmatning av SSID och lösenord för det WiFi som 
   QR-koden ska skapas för. Fälten ska heta ``ssid`` och ``password``.
   Formuläret kan du skapa i filen ``src/first_flask_app/forms.py``.

3. Rendera formuläret i templaten för index-routen.

4. Lägg till biblioteket ``pyqrcodeng`` i projektet med kommandot::

    poetry add pyqrcodeng

5. Rendera en QR-kod som en ``<svg>``-tagg. För att åstadkomma det behöver du använda ``io.BytesIO``::

    import io
    import pyqrcodeng as pyqrcode

    qr = pyqrcode.create(data)
    buffer = io.BytesIO()
    qr.svg(buffer, xmldecl=False, omithw=True)
    svg = buffer.getvalue().decode()


Struktur i projektet
--------------------

Det är ett antal mappar och filer i projektet::

    ➜ git ls-tree -r --name-only HEAD | tree --fromfile
    .
    ├── .env-example
    ├── .flake8
    ├── .gitignore
    ├── README.rst
    ├── config.py
    ├── noxfile.py
    ├── poetry.lock
    ├── pyproject.toml
    ├── src
    │   └── first_flask_app
    │       ├── __init__.py
    │       ├── main.py
    │       ├── static
    │       │   └── style.css
    │       └── templates
    │           ├── base.html
    │           └── index.html
    ├── tests
    │   ├── __init__.py
    │   ├── conftest.py
    │   ├── test_exists.py
    │   └── test_qr.py
    └── wsgi.py


Filen ``.env-eample``
~~~~~~~~~~~~~~~~~~~~~

Ett exempel på vad som kan finnas i filen `.env`. Här hittar vi konfiguration 
av vår applikation, till exempel hemliga värden.


Filen ``.flake8``
~~~~~~~~~~~~~~~~~

Inställningar till verktyget Flake8 som lintar koden.


Filen ``.gitignore``
~~~~~~~~~~~~~~~~~~~~

Berättar för git vilka filer som den inte ska bry sig om.


Filen ```README.rst``
~~~~~~~~~~~~~~~~~~~~~

Den här filen.


Filen ``config.py``
~~~~~~~~~~~~~~~~~~~

En fil med konfiguration av applikationen.


Filen ``noxfile.py``
~~~~~~~~~~~~~~~~~~~~

Berättar för programmet ``nox`` vad den ska göra.


Filen ``poetry.lock``
~~~~~~~~~~~~~~~~~~~~~

Poetry, som installerar paket i python, använder filen för att hålla reda på
versioner av olika paket.


Filen ``pyproject.toml``
~~~~~~~~~~~~~~~~~~~~~~~~

Beskriver vårt eget paket för Python och Poetry.


Mappen ``src/``
~~~~~~~~~~~~~~~

I denna mapp hittar vi källkoden till projektet.


Filen ``src/first_flask_app/__init__.py``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Filen skapar vår applikation. Del av uppstarten och behöver sällan ändras.


Filen ``src/first_flask_app/main.py``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Filen beskriver applikationens olika sökvägar (eng. routes). Innehåller en stor
av logiken för applikationen.


Mappen ``src/first_flask_app/static/``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mappen innehåller de filer som inte Python behöver bearbeta. CSS, bildfiler, med mera.


Mappen ``src/first_flask_app/templates``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mappen innehåller våra HTML-filer som Jinja-templates.


Mappen ``tests/``
~~~~~~~~~~~~~~~~~

Mappen innehåller våra tester och lite kod som behövs för att de ska kunna köras av pytest.


Filen ``wsgi.py``
~~~~~~~~~~~~~~~~~

En fil som skapar en applikation. Behövs för att enklare starta med flask-kommandot.
