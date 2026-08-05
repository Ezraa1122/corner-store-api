class NotFoundError(Exception):
    """when things being asked for doesnt exist"""
    pass

class ProductNotFoundError(NotFoundError):
    def __init__(self, product_id: int):
        self.product_id = product_id
        super().__init__(f"Product {product_id} not found")

class InsufficientStockError(Exception):
    def __init__(self, product_id: int, requested: int, available: int):
        self.product_id = product_id
        self.requested = requested
        self.available = available
        super().__init__(
            f"Product {product_id}: requested {requested}, only {available} in stock"
        )