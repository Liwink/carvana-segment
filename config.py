from sys import platform

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