def test_create_product(client):
    response = client.post("/products/", json={
        "name": "Muffin",
        "price": 3.0,
        "stock": 5
    })

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Muffin"
    assert data["id"] is not None

def test_list_products(client):
    client.post("/products/", json={"name": "Coffee", "price": 4.5, "stock": 10})

    response = client.get("/products/")

    assert response.status_code == 200
    assert len(response.json()) == 1

def test_get_nonexistent_product_returns_404(client):
    response = client.get("/products/9999")

    assert response.status_code == 404