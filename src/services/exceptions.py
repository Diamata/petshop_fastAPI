from fastapi import HTTPException, status


class PetshopException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


# ----------------------------------------- Product exceptions:

class NoProductsExistException(PetshopException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "There are no products under such requirements"


class NoProductExistsException(PetshopException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "There is no such product"


# ----------------------------------------- Brand exceptions:

class NoBrandsException(PetshopException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "There are no brands under such requirements"


class NoBrandException(PetshopException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "There is no such brand"


class NoBrandCreatedException(PetshopException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Brand was not created"


# ----------------------------------------- Categories exceptions:

class NoCategoriesException(PetshopException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "There are no categories under such requirements"


class NoCategoryException(PetshopException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "There is no such category"


class NoCategoryCreatedException(PetshopException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Category was not created"


# ----------------------------------------- Images exceptions:

class NoImagesException(PetshopException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "There are no images under such requirements"


class NoImageException(PetshopException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "There is no such image"


class NoImageCreatedException(PetshopException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Image was not created"
