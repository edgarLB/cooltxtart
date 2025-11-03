import mediapipe as mp
import cv2


def make_mask(img):
    mp_selfie_segmentation = mp.solutions.selfie_segmentation
    with mp_selfie_segmentation.SelfieSegmentation() as selfie_segmentation:
        results = selfie_segmentation.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        mask = results.segmentation_mask

        return mask