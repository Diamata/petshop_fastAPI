from fastapi import APIRouter, status

from src.images.schemas import ImageSchema

router = APIRouter(prefix="/images", tags=["Images"])


# @router.get("")
# async def get_all_images() -> list[ImageSchema]:
#     pass
#
#
# @router.get("/{image_id}")
# async def get_image_by_id(image_id: int) -> ImageSchema:
#     pass
#
#
# @router.post("", status_code=status.HTTP_201_CREATED)
# async def create_image(url: str, product_id: int) -> ImageSchema:
#     pass
#
#
# # TODO: put & patch with dependency from what is required:
# @router.post("/{image_id}", status_code=status.HTTP_200_OK)
# async def update_image(image_id: int) -> ImageSchema:
#     pass
#
#
# @router.delete("/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_image(image_id: int) -> None:
#     pass
