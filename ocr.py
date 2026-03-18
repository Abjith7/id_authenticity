import easyocr
import cv2

reader = easyocr.Reader(['en'])

def extract_text(image_path):

    # read image
    img = cv2.imread(image_path)

    # upscale image (helps OCR detect small characters)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # remove noise
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # increase contrast
    thresh = cv2.adaptiveThreshold(
        blur,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # save debug image so you can see what OCR reads
    cv2.imwrite("debug_preprocessed.jpg", thresh)

    # run OCR
    result = reader.readtext(thresh)

    # extract text
    text = " ".join([r[1] for r in result])

    return text