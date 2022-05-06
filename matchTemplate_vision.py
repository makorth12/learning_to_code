import cv2 as cv
import numpy as np


class MatchTemplate_Vision:

    # properties
    needle_img = None
    needle_w = 0
    needle_h = 0
    method = None

    # constructor
    def __init__(self, needle_img_path, method=cv.TM_CCORR_NORMED):
        self.needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)

        # Save the dimensions of the needle image
        self.needle_w = self.needle_img.shape[1]
        self.needle_h = self.needle_img.shape[0]

        # There are 6 methods to choose from:
        # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
        self.method = method

    def find(self, haystack_img, threshold=0.5, debug_mode=None, im_show_window_name=None):
        # run the OpenCV algorithm
        result = cv.matchTemplate(haystack_img, self.needle_img, self.method)
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.needle_w, self.needle_h]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            rectangles.append(rect)
        # Apply group rectangles
        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

        points = []
        if len(rectangles):
            line_color = (0, 255, 0)
            line_type = cv.LINE_4

            # Loop over all the rectangles
            for (x, y, w, h) in rectangles:

                # Determine the center position
                center_x = x + int(w/2)
                center_y = y + int(h/2)
                # Save the points
                points.append((center_x, center_y))

                if debug_mode == 'rectangles':
                    # Determine the box position
                    top_left = (x, y)
                    bottom_right = (x + w, y + h)
                    # Draw the box
                    cv.rectangle(haystack_img, top_left, bottom_right, color=line_color, 
                                lineType=line_type, thickness=2)

        ############ DISPLAYS MATCHES #############
        if debug_mode:
            cv.imshow(im_show_window_name, haystack_img)

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()

        return points
                         

 