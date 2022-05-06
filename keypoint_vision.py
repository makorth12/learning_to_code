import cv2 as cv
import numpy as np


class Keypoint_Vision:
    # properties
    needle_img = None
    needle_w = 0
    needle_h = 0

    # constructor
    def __init__(self, needle_img_path):
        self.needle_img = needle_img_path

        # Save the dimensions of the needle image
        self.needle_w = self.needle_img.shape[1]
        self.needle_h = self.needle_img.shape[0]
                              
    def draw_crosshairs(self, haystack_img, points):
        # these colors are actually BGR
        marker_color = (255, 255, 255)
        marker_type = cv.MARKER_CROSS

        for (center_x, center_y) in points:
            # draw the center point
            cv.drawMarker(haystack_img, (center_x, center_y), marker_color, marker_type)

        return haystack_img

    def match_keypoints(self, haystack_screenshot, name, counter, min_match_count, patch_size=32):

        orb = cv.ORB_create(edgeThreshold=0, patchSize=patch_size)
        keypoints_needle, descriptors_needle = orb.detectAndCompute(self.needle_img, None)
        orb2 = cv.ORB_create(edgeThreshold=0, patchSize=patch_size, nfeatures=2000)
        keypoints_haystack, descriptors_haystack = orb2.detectAndCompute(haystack_screenshot, None)

        FLANN_INDEX_LSH = 6
        index_params = dict(algorithm=FLANN_INDEX_LSH, table_number=6, key_size=12, multi_probe_level=1)
        search_params = dict(checks=50)

        try:
            flann = cv.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(descriptors_needle, descriptors_haystack, k=2)
        except cv.error:
                return None, None, [], []
            
        # store all the good matches as per Lowe's ratio test.
        good = []
        points = []

        for pair in matches:
            if len(pair) == 2:
                if pair[0].distance < 0.7*pair[1].distance:
                    good.append(pair[0])

        log = (str("Search Count: ") + str(counter) + str(" - ") + str("Searching for: ") + str(name) + ' - ' + '%03d keypoints matched - %03d' % (len(good), len(keypoints_needle)))
        print(log)

        if len(good) > min_match_count:
            
            for match in good:
                points.append(keypoints_haystack[match.trainIdx].pt)
        
        return keypoints_needle, keypoints_haystack, good, points, log

    def centeroid(self, point_list):
        point_list = np.asarray(point_list, dtype=np.int32)
        length = point_list.shape[0]
        sum_x = np.sum(point_list[:, 0])
        sum_y = np.sum(point_list[:, 1])
        return [np.floor_divide(sum_x, length), np.floor_divide(sum_y, length)]