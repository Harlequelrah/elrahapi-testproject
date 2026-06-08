from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware

# from myapp.router import myapp_router
from song.schemas import SongCreateModel
from song.cruds import song_crud, session_manager
from fastapi import FastAPI, Depends

app = FastAPI(root_path="/api")


@app.get("/")
async def hello():
    return {"message": "hello"}


@app.post("/prompt")
async def prompt(prompt: str, session=Depends(session_manager.get_sync_db)):
    prompt_split = prompt.lower().strip().split(" ")
    if "create" in prompt:
        if "name" in prompt_split and "duration" in prompt_split:
            song_obj = {}
            song_obj["name"] = prompt_split[prompt_split.index("name") + 1]
            song_obj["duration"] = int(prompt_split[prompt_split.index("duration") + 1])
            song_create = song_crud.CreatePydanticModel(**song_obj)
            print(type(song_create), song_create.model_dump())
            # if isinstance(song_create, song_crud.CreatePydanticModel):
            return await song_crud.create(session=session, create_obj=song_create)
    if any([w in prompt_split for w in ["give", "return"]]):
        if any([w in prompt_split for w in ["id", "song"]]):
            song_id = int(prompt_split[prompt_split.index("id") + 1])
        return await song_crud.read_one(session=session, pk=song_id)


# app.include_router(myapp_router)
app.add_middleware(
    ErrorHandlingMiddleware,
)
