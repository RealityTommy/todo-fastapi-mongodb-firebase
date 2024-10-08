from pydantic import BaseModel

# Define the TodoModel
class TodoModel(BaseModel):
    name: str
    description: str
    completed: bool
    firebase_uid: str

    # Add an example to the JSON schema
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Name",
                "description": "Description",
                "completed": False,
                "firebase_uid": ""
            }
        }