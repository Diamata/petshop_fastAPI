from fastapi import HTTPException, status


class PetshopException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class NoProductsExistsException(PetshopException):
    status_code = status.HTTP_409_CONFLICT
    detail = "There are no products under such requirements"
