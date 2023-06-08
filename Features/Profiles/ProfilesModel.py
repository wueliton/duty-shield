from Service.SoDService import SoDService
from Utils.BaseModel import BaseModel


class ProfilesModel(BaseModel):
    def __init__(self, sod_service: SoDService):
        super().__init__(sod_service, 'profiles')
