import dlib
from skimage import io

def faces (link):
    img = io.imread(link)
    detector = dlib.get_frontal_face_detector()
    # Run the face detector, upsampling the image 1 time to find smaller faces.
    dets = detector(img,1)
    return(len(dets))
