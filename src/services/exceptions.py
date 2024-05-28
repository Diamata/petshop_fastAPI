from fastapi import HTTPException, status


class PetshopException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


# ----------------------------------------- Product exceptions

class NoProductsExistException(PetshopException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "There are no products under such requirements"


class NoProductExistsException(PetshopException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "There is no such product"


# ----------------------------------------- Brand exceptions

class NoBrandsException(PetshopException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "There are no brands under such requirements"


class NoBrandException(PetshopException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "There is no such brand"
