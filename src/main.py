import uvicorn
from fastapi import FastAPI

from src.products.router import router as router_products
from src.brands.router import router as router_brands
from src.images.router import router as router_images
from src.categories.router import router as router_categories
from src.characteristics.router import router as router_characteristics

app = FastAPI()

app.include_router(router_products)
app.include_router(router_brands)
app.include_router(router_images)
app.include_router(router_categories)
app.include_router(router_characteristics)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
