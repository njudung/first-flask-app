
def test_form_exists(client):
    rv = client.get('/')
    assert '<form action="" method="POST">'.encode() in rv.data


def test_post_to_index(client):
    rv = client.post('/', data=dict(
        ssid="FreeWifi",
        password="supersecret"
    ))
    assert rv.status_code == 200


def test_index_generates_qr(client):
    rv = client.post('/', data=dict(
        ssid="FreeWiFi",
        password="supersecret"
    ))
    assert '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 45 45" class="pyqrcode"><path stroke="#000" class="pyqrline" d="M4 4.5h7m1 0h5m3 0h4m1 0h1m2 0h1m3 0h1m1 0h7m-37 1h1m5 0h1m1 0h1m1 0h4m2 0h4m1 0h2m1 0h2m1 0h2m1 0h1m5 0h1m-37 1h1m1 0h3m1 0h1m1 0h1m1 0h3m1 0h2m1 0h2m1 0h1m1 0h1m1 0h1m3 0h1m1 0h1m1 0h3m1 0h1m-37 1h1m1 0h3m1 0h1m3 0h3m2 0h6m1 0h1m2 0h4m1 0h1m1 0h3m1 0h1m-37 1h1m1 0h3m1 0h1m3 0h2m2 0h1m1 0h1m1 0h1m1 0h1m1 0h1m3 0h3m1 0h1m1 0h3m1 0h1m-37 1h1m5 0h1m1 0h1m2 0h1m2 0h1m1 0h2m1 0h3m2 0h1m2 0h1m2 0h1m5 0h1m-37 1h7m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h7m-29 1h3m1 0h2m1 0h2m1 0h1m7 0h1m-25 1h3m1 0h1m1 0h1m1 0h6m2 0h5m1 0h1m4 0h3m2 0h3m-35 1h3m2 0h3m1 0h1m1 0h2m2 0h1m1 0h2m2 0h1m2 0h3m1 0h1m4 0h2m-36 1h1m4 0h2m3 0h4m1 0h1m1 0h1m5 0h3m4 0h2m2 0h2m-37 1h1m3 0h2m1 0h2m1 0h1m1 0h3m1 0h1m1 0h1m2 0h2m1 0h1m1 0h1m1 0h3m1 0h1m2 0h1m-36 1h2m2 0h7m2 0h1m1 0h2m3 0h4m2 0h1m1 0h1m1 0h3m1 0h1m-35 1h2m2 0h2m2 0h3m2 0h1m2 0h1m1 0h4m3 0h2m1 0h2m1 0h1m3 0h2m-37 1h2m2 0h5m3 0h1m2 0h1m1 0h2m2 0h1m2 0h1m2 0h2m1 0h3m1 0h3m-35 1h2m1 0h1m1 0h1m2 0h2m1 0h1m1 0h7m2 0h1m1 0h3m6 0h1m-36 1h7m2 0h3m1 0h2m5 0h2m1 0h1m2 0h8m-33 1h2m1 0h1m4 0h2m3 0h2m2 0h1m4 0h1m3 0h2m2 0h1m1 0h1m1 0h2m-37 1h1m1 0h1m1 0h1m1 0h3m1 0h4m2 0h1m3 0h1m2 0h3m1 0h4m1 0h1m1 0h3m-37 1h1m2 0h1m1 0h1m1 0h1m5 0h1m1 0h2m2 0h1m1 0h1m1 0h1m2 0h6m1 0h1m1 0h2m-36 1h2m2 0h7m1 0h4m1 0h1m1 0h2m1 0h8m3 0h3m-37 1h1m2 0h3m5 0h1m1 0h1m4 0h1m4 0h3m3 0h1m1 0h1m1 0h1m-34 1h1m1 0h1m3 0h1m1 0h3m4 0h5m3 0h1m1 0h3m1 0h1m2 0h2m1 0h2m-37 1h3m1 0h2m4 0h1m1 0h3m2 0h4m1 0h1m2 0h1m1 0h2m2 0h1m1 0h1m-34 1h2m1 0h2m1 0h1m2 0h1m1 0h1m3 0h1m1 0h1m1 0h2m2 0h2m1 0h4m1 0h2m1 0h1m1 0h1m-37 1h6m2 0h1m10 0h2m1 0h1m4 0h1m2 0h1m4 0h1m-36 1h1m2 0h2m1 0h2m1 0h1m3 0h1m1 0h2m3 0h1m2 0h2m2 0h2m2 0h3m2 0h1m-37 1h1m2 0h1m3 0h4m4 0h1m1 0h7m3 0h1m4 0h2m1 0h2m-37 1h1m1 0h1m2 0h6m3 0h1m1 0h2m1 0h2m1 0h2m2 0h7m1 0h1m-27 1h2m1 0h1m3 0h1m1 0h1m1 0h3m1 0h1m3 0h2m3 0h4m-36 1h7m2 0h6m1 0h5m4 0h2m1 0h1m1 0h1m1 0h1m3 0h1m-37 1h1m5 0h1m2 0h1m1 0h2m5 0h7m3 0h1m3 0h1m2 0h2m-37 1h1m1 0h3m1 0h1m1 0h3m1 0h3m1 0h1m3 0h2m3 0h9m2 0h1m-37 1h1m1 0h3m1 0h1m1 0h1m1 0h1m1 0h2m2 0h2m3 0h2m1 0h1m2 0h1m1 0h6m-35 1h1m1 0h3m1 0h1m1 0h1m1 0h1m3 0h2m3 0h3m4 0h2m1 0h3m1 0h2m1 0h1m-37 1h1m5 0h1m2 0h1m2 0h5m3 0h2m2 0h1m1 0h5m1 0h1m3 0h1m-37 1h7m3 0h2m1 0h4m2 0h1m1 0h1m2 0h3m2 0h2m1 0h2m1 0h2"></path></svg>'.encode() in rv.data  # noqa: E501
