from sys import platform

"""
`images` and `masks` dir
images: CARVANA_DIR + '/images/%s/%s.jpg'%(folder,name)
masks:  CARVANA_DIR + '/annotations/%s/%s_mask.jpg'%(folder,name)
"""

if platform == 'darwin':
    TRAIN_OUT_DIR = '/Users/lcp/projects/carvana/results/single/UNet1024-01c'
    VALID_OUT_DIR = '/Users/lcp/projects/carvana/results/single/UNet1024-peduo-label-01c'
    CARVANA_DIR = '/Users/lcp/projects/carvana'
    USING_CUDA = False
elif platform == 'linux' or platform == 'linux2':
    USING_CUDA = True
    raise Exception('Clarify the Config of Linux.')
else:
    raise Exception('Clarify the Config.')