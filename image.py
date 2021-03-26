import os
import cv2

class Image:
    # Get All jpg files in images folder
    @staticmethod
    def get_all_images_in_folder(foldername):
        filenames = []
        for  filename in  [x for x in os.listdir(foldername) if x.endswith(".jpg")]: 
            path = './' + foldername + '/' + filename
            filenames.append(path)
        return filenames

    # Open an Image
    @staticmethod
    def load_image(imagepath):
        image = cv2.imread(imagepath)
        return image

    # Open an Image in 512x512
    @staticmethod
    def load_image_512(imagepath):
        image = Image.load_image(imagepath)
        return  cv2.resize(image,(512, 512))

    # Get image histograms
    # @Parametre imagePath: Image path 
    @staticmethod
    def get_image_histogram(imagepath):
        image = Image.load_image_512(imagepath)
        hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        return list(hist.flatten())

    # Get image blue histogram
    # @Parametre image: Image 
    @staticmethod
    def get_image_blue_histogram(image):
        hist = cv2.calcHist([image], [0], None, [8], [0, 256])
        return list(hist)
    
    # Get image green histogram
    # @Parametre image: Image 
    @staticmethod
    def get_image_green_histogram(image):
        hist = cv2.calcHist([image], [1], None, [8], [0, 256])
        return list(hist)

    # Get image red histogram
    # @Parametre image: Image : 
    @staticmethod
    def get_image_red_histogram(image):
        hist = cv2.calcHist([image], [2], None, [8], [0, 256])
        return list(hist)
    
    # Get image full feature vector
    # @Parametre imagePath: Image path
    @staticmethod
    def get_image_full_feature_vector(imagepath):
        return  [imagepath] + Image.get_image_histogram(imagepath)