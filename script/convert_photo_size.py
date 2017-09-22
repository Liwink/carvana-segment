#!/usr/bin/env python
# encoding: utf-8

import os
from tqdm import tqdm
from PIL import Image

SOURCE_DIR = '../../images/train/'
TARGET_DIR = '../../images/train128x128/train/'
# SOURCE_DIR = '../../images/train_masks/'
# TARGET_DIR = '../../annotations/train128x128/train/'
SIZE = 192, 128


def convert(filename):
    im = Image.open(SOURCE_DIR + filename)
    im.thumbnail(SIZE, Image.ANTIALIAS)
    # im.save(TARGET_DIR + filename, 'JPEG')
    if filename.endswith('gif'):
        filename = filename[:-3] + 'jpg'
        im = im.convert('RGB')
    im.save(TARGET_DIR + filename)


def photo_filenames():
    return [i for i in os.listdir(SOURCE_DIR) if i.endswith('.jpg') or i.endswith('.gif')]


def main():
    filenames = photo_filenames()

    for f in tqdm(filenames):
        convert(f)


if __name__ == '__main__':
    main()
