import tensorflow
import keras

class SequentialModel:

    def __init__(self, input_size: tuple = (0, 0), output_size: tuple = (0, 0)):

        # Model
        self.model = keras.Sequential()
        self.input_size = input_size
        self.output_size = output_size

    # This checks if the model settings are valid before it is formed
    # Right now this only checks the input and output sizes
    def __check__(self):

        if self.input_size == (0, 0):
            return False

        elif self.output_size == (0, 0):
            return False

        else:
            return True

    # This will construct the model
    def form(self):

        self.model.add(keras.layers.Conv2D(32, kernel_size=(3, 3), activation="relu", input_shape=self.input_size))
        self.model.add(keras.layers.Conv2D(64, kernel_size=(3, 3), activation="relu"))
        self.model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
        self.model.add(keras.layers.Conv2D(64, kernel_size=(3, 3), activation="relu"))
        self.model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
        self.model.add(keras.layers.Conv2D(64, kernel_size=(3, 3), activation="relu"))
        self.model.add(keras.layers.Dense(128, activation="relu"))
        self.model.add(keras.layers.Dense(self.output_size, activation="softmax"))

        return

    # I'mma return the model for now caues I don't know what do with it here
    def GetModel(self):
        return self.model