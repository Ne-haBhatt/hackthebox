from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
from random import randint

#class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
class_names = [True, True, False, False, False, False, False, False, True, True]

img_path = "dog.png"


class SigmaNet: #class was given
    def __init__(self):
        self.name = 'sigmanet'
        self.model_filename = 'sigmanet.h5'
        try:
            self._model = load_model(self.model_filename)
            print('Successfully loaded', self.name)
        except (ImportError, ValueError, OSError):
            print('Failed to load', self.name)

    def color_process(self, imgs):
        if imgs.ndim<4:
            imgs = np.array([imgs])
        imgs = imgs.astype('float32')
        mean = [125.307, 122.95, 113.865]
        std = [62.9932, 62.0887, 66.7048]
        for img in imgs:
            for i in range(3):
                img[:, :, i] = (img[:, :, i] - mean[i])/std[i]
        return imgs

    def predict(self, img):
        processed = self.color_process(img)
        return self._model.predict(processed)[0]

    def predict_one(self, img):
        confidence = self.predict(img)[0]
        predicted_class = np.argmax(confidence)
        return class_names[predicted_class]

    def predict_one_calced(self,weights): # method added
        predicted_class = np.argmax(weights)
        return class_names[predicted_class]



def ran_pixel():
    x = randint(0, 31)
    y = randint(0, 31)
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return x, y, r, g, b


def evolve(x,y,r,g,b):
    n = randint(0,99)
    if n<56:
        if n<32:
            if n<16:
                if n<8:
                    x = max(0, x-randint(1,4))
                else:
                    x = min(31, x+randint(1,4))
            else:
                if n<24:
                    y = max(0, y-randint(1,4))
                else:
                    y = min(31, y+randint(1,4))
        else:
            if n<48:
                if n<40:
                    r = max(0, r-randint(1,6))
                else:
                    r = min(255, r+randint(1,6))
            else:
                g = max(0, g-randint(1,6))
    else:
        if n<84:
            if n<72:
                if n<64:
                    g = min(255, g+randint(1,6))
                else:
                    b = max(0, b-randint(1,6))
            else:
                if n<80:
                    b = min(255, b+randint(1,6))
                else:
                    x = randint(0,31)
        else:
            if n<92:
                if n<88:
                    y = randint(0,31)
                else:
                    r = randint(0,255)
            else:
                if n<96:
                    g = randint(0,255)
                else:
                    b = randint(0,255)
    return x,y,r,g,b

img = Image.open(img_path).convert("RGB")
sigma = SigmaNet()
gen = 0
fmly = [[ran_pixel() for __ in range(5)] for _ in range(10)]
clean_data = np.array(img)
rank = [(3.1,4) for i in range(100)]

while True:
    desc = [[evolve(*laser) for laser in cld] for cld in fmly for _ in range(10)]

    for i, d in enumerate(desc):
        data = clean_data.copy()
        for x,y,r,g,b in d:
            data[y, x] = [r,g,b]

        ret = sigma.predict(data)
        cls = sigma.predict_one_calced(ret)

        if cls:
            print("Our dog turned into a vehicle!")
            print(d)

            img = Image.fromarray(data)
            img.show()
            exit(0)
            
        rank[i] = (ret[0]+ret[1]+ret[8]+ret[9],i)
        if gen%128 == 0:
            print(gen)
        gen += 1

        
    rank.sort(reverse=True)
    
    fmly[0] = desc[rank[0][1]]
    fmly[1] = desc[rank[1][1]]
    fmly[2] = desc[rank[2][1]]
    fmly[3] = desc[rank[3][1]]
    fmly[4] = desc[rank[4][1]]

    fmly[5] = desc[rank[randint(5,25)][1]]
    fmly[6] = desc[rank[randint(5,25)][1]]
    fmly[7] = desc[rank[randint(5,25)][1]]
    fmly[8] = desc[rank[randint(26,50)][1]]
    fmly[9] = desc[rank[randint(26,50)][1]]
