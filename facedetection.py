import dlib
from skimage import io

def faces (link):
    img = io.imread(link)
    detector = dlib.get_frontal_face_detector()
    dets = detector(img,1)
    return(len(dets))
