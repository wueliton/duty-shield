from Service.SoDService import SoDService
from Utils.BaseModel import BaseModel


class UsersModel(BaseModel):
    def __init__(self, sod_service: SoDService):
        super().__init__(sod_service, 'users')