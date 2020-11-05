
def test_form_exists(client):
    rv = client.get('/')
    assert '<form action="" method="POST">'.encode() in rv.data


def test_post_to_index(client):
    rv = client.post('/', data=dict(
        ssid="FreeWifi",
        password="supersecret"
    ))
    assert rv.status_code == 200


def test_index_calls_pyqrcode(mocker, client):
    patch = mocker.patch('first_flask_app.main.pyqrcode')
    client.post('/', data=dict(
        ssid="FreeWiFi",
        password="supersecret"
    ))

    patch.create.assert_called_once_with('WIFI:T:WPA;S:FreeWiFi;P:supersecret;;')
