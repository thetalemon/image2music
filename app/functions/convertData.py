#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import cv2
import numpy as np
import os
from io import BytesIO
from PIL import Image
from scipy.io import wavfile

def base64toCV2(img):
    code = base64.b64decode(img.split(',')[1])
    image_decoded = Image.open(BytesIO(code))

    img_array = np.asarray(image_decoded)

    return img_array

def CV2toBase64(img):
    convertedCV2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    CV2PIL = Image.fromarray(convertedCV2)

    modified_bin = BytesIO()
    CV2PIL.save(modified_bin, format="PNG")
    img_str = base64.b64encode(modified_bin.getvalue()).decode("utf-8")
    add_headers = "data:image/png;base64," + img_str

    return add_headers

def PMtoBase64(pm):
    audio_data = pm.fluidsynth()
    music_max = np.max(np.abs(audio_data))
    muisc_array = (audio_data/music_max).astype(np.float32)
    wav_file_name = 'test.wav'
    wavfile.write(wav_file_name,44100, muisc_array)

    f = open(wav_file_name,'rb')
    buffer = f.read()
    f.close()
    os.remove(wav_file_name)
    music = base64.b64encode(buffer).decode("utf-8")
    add_muisc = "data:audio/wav;base64," + music

    return add_muisc
