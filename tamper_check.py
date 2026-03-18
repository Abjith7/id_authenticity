import cv2
import numpy as np

def detect_tampering(image_path):

    img = cv2.imread(image_path)

    temp = "temp.jpg"

    cv2.imwrite(temp, img, [cv2.IMWRITE_JPEG_QUALITY, 90])

    recompressed = cv2.imread(temp)

    diff = cv2.absdiff(img, recompressed)

    score = np.mean(diff)

    if score > 10:
        return "Possible image tampering detected"

    return "No obvious tampering"