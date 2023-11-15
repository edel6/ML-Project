from torchvision.datasets.utils import download_url
import tarfile

download_url("https://s3.amazonaws.com/fast-ai-imageclas/imagenette2-320.tgz", '.')

with tarfile.open('./imagenette2-320.tgz', 'r:gz') as tar:
    tar.extractall(path='./data')