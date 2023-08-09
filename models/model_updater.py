from .base_models import ObjectModel, Sprite


class ModelUpdater:
    @classmethod
    def move_model(cls, objct: ObjectModel):
        objct.x += objct.velocity_x
        objct.y += objct.velocity_y

    @classmethod
    def update_model(cls, object_model: ObjectModel):
        cls.move_model(object_model)

    @classmethod
    def update_models(cls, *object_model: ObjectModel):
        for objct in object_model:
            if objct.update:
                cls.update_model(objct)

