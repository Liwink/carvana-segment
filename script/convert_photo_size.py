#!/usr/bin/env python
# encoding: utf-8

import os
from tqdm import tqdm
from PIL import Image

SOURCE_DIR = '../../images/train/'
TARGET_DIR = '../../images/train128x128/train/'
SIZE = 128, 128


def convert(filename):
    im = Image.open(SOURCE_DIR + filename)
    im.thumbnail(SIZE, Image.ANTIALIAS)
    im.save(TARGET_DIR + filename, 'JPEG')


def photo_filenames():
    return [i for i in os.listdir(SOURCE_DIR) if i.endswith('.jpg')]


def main():
    filenames = photo_filenames()

    for f in tqdm(filenames):
        convert(f)


if __name__ == '__main__':
    main()
