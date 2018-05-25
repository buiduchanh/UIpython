import os
import cv2
import tensorflow as tf

from nets import inception
from preprocessing import inception_preprocessing

# MODEL_PATH = '/home/buiduchanh/WorkSpace/demo_jestson/model/frozen_acr_front_view.pb'
MODEL_PATH = '/home/nvidia/hanh_demo/model/frozen_acr_front_view.pb'
MODEL_NAMES = {0: ['Audi', 'A3 Sportback'], 1: ['Audi', 'A4 Avant'], 2: ['BMW', '1 Series'], 3: ['BMW', '3 Series'],
               4: ['Daihatsu', 'Hijet Cargo'], 5: ['Daihatsu', 'Mira ES'], 6: ['Daihatsu', 'Mira Gino'],
               7: ['Daihatsu', 'Tanto'], 8: ['Honda', 'Fit'], 9: ['Honda', 'Fried'], 10: ['Honda', 'Life'],
               11: ['Honda', 'N-BOX'], 12: ['Honda', 'N-WGN'], 13: ['Honda', 'Odyssey'], 14: ['Honda', 'Shuttle'],
               15: ['Honda', 'Step Wagon'], 16: ['Honda', 'Wesel'], 17: ['Lexus', 'Lexus CT'],
               18: ['Lexus', 'Lexus GS'], 19: ['Lexus', 'Lexus IS'], 20: ['Mazda', 'Axela'], 21: ['Mazda', 'Demio'],
               22: ['Mercedes Benz', 'C Class'], 23: ['Mercedes Benz', 'E Class'], 24: ['Mercedes Benz', 'S Class'],
               25: ['Mini', 'Mini'], 26: ['Nissan', 'Dayz'], 27: ['Nissan', 'Dayz Roox'], 28: ['Nissan', 'Fairlady Z'],
               29: ['Nissan', 'Juke'], 30: ['Nissan', 'Note'], 31: ['Nissan', 'OTTI'], 32: ['Nissan', 'Serena'],
               33: ['Nissan', 'Skyline'], 34: ['Nissan', 'X-Trail'], 35: ['Porsche', '911'], 36: ['Porsche', 'Cayenne'],
               37: ['Subaru', 'Forester'], 38: ['Subaru', 'Impreza'], 39: ['Subaru', 'Impreza Hatchback'],
               40: ['Subaru', 'Impreza STI'], 41: ['Subaru', 'Impreza Sport'], 42: ['Subaru', 'Impreza Sport Wagon'],
               43: ['Subaru', 'Impreza XV'], 44: ['Subaru', 'Levorg'], 45: ['Suzuki', 'ALTO Lapin'],
               46: ['Suzuki', 'Every'], 47: ['Suzuki', 'Every Wagon'], 48: ['Suzuki', 'Ignis'],
               49: ['Suzuki', 'MR Wagon'], 50: ['Suzuki', 'Solio'], 51: ['Toyota', 'Alphard'],
               52: ['Toyota', 'Alphard Hybrid'], 53: ['Toyota', 'Aqua'], 54: ['Toyota', 'Corolla'],
               55: ['Toyota', 'Corolla Axio'], 56: ['Toyota', 'Corolla Fielder'], 57: ['Toyota', 'Corolla Lumion'],
               58: ['Toyota', 'Crown'], 59: ['Toyota', 'Crown Athlete'], 60: ['Toyota', 'Crown Estate'],
               61: ['Toyota', 'Crown Majesta'], 62: ['Toyota', 'Crown Royal'], 63: ['Toyota', 'Crown Sedan'],
               64: ['Toyota', 'Esquire'], 65: ['Toyota', 'Estima'], 66: ['Toyota', 'Harrier'],
               67: ['Toyota', 'Land Cruiser 100'], 68: ['Toyota', 'Land Cruiser 60'], 69: ['Toyota', 'Land Cruiser 70'],
               70: ['Toyota', 'Land Cruiser 80'], 71: ['Toyota', 'Land Cruiser Cygnus'],
               72: ['Toyota', 'Land Cruiser Prado'], 73: ['Toyota', 'Noah'], 74: ['Toyota', 'Passo'],
               75: ['Toyota', 'Prius'], 76: ['Toyota', 'Sienta'], 77: ['Toyota', 'Vellfire'], 78: ['Toyota', 'Vitz'],
               79: ['Toyota', 'Voxy'], 80: ['Toyota', 'Wish'], 81: ['Toyota', 'bB'], 82: ['Volkswagen', 'Golf'],
               83: ['Volkswagen', 'New Beetle']}
IMAGE_SIZE = 299


class Recognizor:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Recognizor.__instance == None:
            print("Initialize ... ")
            Recognizor()
        return Recognizor.__instance

    def __init__(self):
        if Recognizor.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Recognizor.__instance = self

        with tf.gfile.GFile(MODEL_PATH, "rb") as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())

        with tf.Graph().as_default() as graph:
            tf.import_graph_def(graph_def, name="prefix")

            self.x = graph.get_tensor_by_name('prefix/input:0')
            self.y = graph.get_tensor_by_name('prefix/InceptionV4/Logits/Predictions:0')
            self.sess = tf.Session(graph=graph)

    def get_model(self, image):
        with tf.Session():
            processed_images = []
            image = tf.convert_to_tensor(image)
            processed_image = inception_preprocessing.preprocess_image(image, IMAGE_SIZE, IMAGE_SIZE,
                                                                       is_training=False).eval()
            processed_images.append(processed_image)

            probs = self.sess.run(self.y, feed_dict={self.x: processed_images})
            sorted_inds = [j[0] for j in sorted(enumerate(-probs[0]), key=lambda x: x[1])]
            results = []
            for k in range(3):
                index = sorted_inds[k]
                name = MODEL_NAMES[index]
                prob = round(probs[0][index], 3)
                print("prob", prob)

                results.append('{}-{}:{}%'.format(name[0], name[1], round(prob * 100, 2)))

            print("result", results)

        return results

# if __name__ == '__main__':
# image = cv2.imread('/home/buiduchanh/WorkSpace/demo_jestson/test/T0_018/to_016_020593222.jpg')
# image = cv2.imread('/home/buiduchanh/WorkSpace/demo_jestson/test/T0_018/TO_016_0205932.jpg')
# result  = get_model(image)
# print("result",result)
