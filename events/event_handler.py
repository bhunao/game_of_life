from models.base_models import ObjectModel
from .event import Event, EventProperties


class EventHandler:
    @classmethod
    def handle_event(cls, event: Event):
        print(f'handling event: {event.name}')

        # brain event
        if event.name == "brain":
            player = self.get_objects_by_name("player")[0]
            food = self.get_objects_by_name("food")[0]
            event.action(player, food, self.display.screen.get_size())
            return

        target_names = event.properties.target_objects
        target_objects = []
        config = {}


        if not target_names:
            objcts = event.action(self.display, game_event, config)
            self.display.render_objets(objcts)
            if event.name == "game of life":
                pass
            return

        for target_name in target_names:
            target_objects.extend(self.get_objects_by_name(target_name))

        for target in target_objects:
            event.action(self.display, game_event, target, config)

    @classmethod
    def handle_events(cls, *events: Event):
        for event in events:
            if event.addittional_properties:
                raise NotImplementedError("EventHandler.handle_events() does not support addittional_properties yet.")

            cls.handle_event(event)

