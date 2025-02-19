from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

#created new response model below which will only show the title when used

class ShowBlog(BaseModel):
    title: str
    class Config:
        from_attributes = True  # Use this instead of orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str

