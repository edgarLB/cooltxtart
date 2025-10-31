import mediapipe as mp
import cv2
import numpy as np


# filePath = '../temp/IMG_6604.jpeg'
# img = cv2.imread(filePath)
# img = cv2.resize(img, (150,150))
# print(img.shape)
#
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
def make_mask(img):
    mp_selfie_segmentation = mp.solutions.selfie_segmentation
    with mp_selfie_segmentation.SelfieSegmentation() as selfie_segmentation:
        results = selfie_segmentation.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        mask = results.segmentation_mask

        return mask


    # --- test ---
        # condition = mask > 0.6

        # background1 = np.zeros_like(img, dtype=np.uint8)
        # output = np.where(condition[..., None], img, background1)

        # cv2.imwrite('../temp/output1.png', output)
        # cv2.imshow('Removed Background', output)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()