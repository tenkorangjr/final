from scene_input import AskScene
from scene_brain import SceneController
import realism


def main(run=True):
    """Run program"""

    if not run:
        return

    program = AskScene()
    program.create_pop_up()

    control = SceneController("scene.json")
    control.show_scene()

    # Recursive call
    main(run=control.go_again)


if __name__ == "__main__":
    main()
