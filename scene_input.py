from tkinter import *
import tkinter
import json


class AskScene:

    def __init__(self) -> None:
        """Initialiser for scene selector"""

        self.scenes = None
        self.window = None
        self.label = None
        self.scene_var = None
        self.select_level = None
        self.button = None
        self.done = None

    def create_pop_up(self):
        """Function to create the pop up"""

        self.window = Tk()
        self.window.title("NumGuess Game")
        self.window.minsize(width=250, height=60)
        self.window.config(pady=10, padx=10)

        window_height = 80
        window_width = 300

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))

        self.window.geometry(
            f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate - 150}")

        # Label for pop-up
        self.label = Label(self.window, text="Select Scene: ")
        self.label.grid(row=0, column=0)

        # Level selection
        self.scenes = ["Environmental Art Graph", "Lsystem", "Outdoor Scene"]
        self.scene_var = StringVar(self.window)
        self.scene_var.set(self.scenes[0])
        self.select_scene = OptionMenu(
            self.window, self.scene_var, *self.scenes)
        self.select_scene.grid(row=0, column=1, padx=10)

        self.button = Button(self.window, text="Let's Go",
                             command=self.scene_selected)
        self.button.grid(row=1, column=1, columnspan=2, pady=10)

        self.window.mainloop()

    def scene_selected(self):
        """Store the scene selected in scene.json"""

        try:
            # Write the item selected in the scene.json file
            self.scene = self.scene_var.get()
            scene_dict = {
                "scene": self.scene
            }
            with open(file="scene.json", mode="w") as scene_file:
                json.dump(scene_dict, scene_file, indent=4)
        # Alert the user that no item has been selected
        except tkinter.TclError:
            tkinter.messagebox.showwarning(message="Select a Scene")
            return False
        else:
            # Close the window after taking input
            self.window.destroy()
            self.window.update()


if __name__ == "__main__":
    pop = AskScene()
    pop.create_pop_up()
