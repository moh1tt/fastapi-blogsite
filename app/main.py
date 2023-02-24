from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from Blogs import models
from Blogs.database import engine
from pathlib import Path
from Blogs.routers import blog,user,authentication,portfolio

models.Base.metadata.create_all(engine)

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "app/Blogs/static"),
    name="static",
)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(portfolio.router)




 

# if __name__ == '__main__':
#     uvicorn.run("Blogs.main:app", port=5000, reload=True, access_log=False)