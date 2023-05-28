from Utils.BaseController import BaseController


class PutProfileController(BaseController):
    def validate_system(self, cod: str):
        return self._model.validate_system(cod)

    def validate_profile(self, profile_name: str):
        return self._model.validate_profile(profile_name)


