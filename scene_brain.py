from visit_manager import NumberOfVisits
import json
import arrangement
import art
import realism


class SceneController(NumberOfVisits):

    def __init__(self, filename):
        super().__init__()
        self.name = filename
        self.go_again = True
        self.scene = self.get_scene()

    def __str__(self):
        """Function for polymorphism"""

        return self.scene

    def get_scene(self):
        """Return the scene to be shown"""

        with open(file=self.name, mode="r") as json_file:
            self.scene = json.load(json_file)["scene"]

        self.go_again = False

        return self.scene

    def show_scene(self):
        if self.scene == "Lsystem":
            arrangement.main()

        elif self.scene == "Environmental Art Graph":
            art.art()

        elif self.scene == "Outdoor Scene":
            realism.main()


if __name__ == "__main__":
    scene_controller = SceneController("scene.json")
    scene_controller.show_scene()
