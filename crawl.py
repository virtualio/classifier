
# import the necessary packages
import numpy as np
import cv2
import urllib.request
import os
import time


# TODO: use generator in crawling for efficiency


##
#   @description: Crawler class have two modes: ['human','cat']
#   the class crawl in number of images from a list from the net.
#   download it to lcal machine, detect faces and sort it.
#   @author Star Dust
#   @Date: January 1, 2027
## 
class crawler:


    number_of_images= 100
    # default 
    file_name       = "Humans"
    crawling_links  = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152' #humans is default
    # load face cascade
    front_face      = None


    def __init__(self, mode):
        if mode == 'cat':
            self.crawling_links = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02121808'
            self.file_name      = "Cats"
            self.front_face      = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
        else:
            self.front_face      = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

        print("Number of urls to crawl: " + str(self.number_of_images))
        print ("++++++++++++++++++++++++++")
        print("START")
    


    def open_dir(self):
        if not os.path.exists(self.file_name + "/selected"):
            os.makedirs(self.file_name + "/selected")
        if not os.path.exists(self.file_name + "/not_selected"):
            os.makedirs(self.file_name + "/not_selected")


    def get_urls(self):
        crawling_list_html = urllib.request.urlopen(self.crawling_links).read()
        return crawling_list_html.decode()


    def collect_images(self, crawling_list_urls):

        pic_num = 0

        for url in crawling_list_urls.split('\n'):

            try:
                urllib.request.urlretrieve(url, self.file_name + '/' + str(pic_num+1) + '.jpg')                
                 
                pic_num += 1
                if pic_num > self.number_of_images:
                    print("collected images: " + str(pic_num))
                    return

            except Exception as e:
                pass  

    
    def classify(self):
        i = 0        # number of images detected
        j = 0        # number of faces

        # read all images in dir
        for img_name in os.listdir(self.file_name):
            img = cv2.imread(self.file_name + '/' + img_name, cv2.IMREAD_COLOR)
            
            if img is not None:
                gray_img    = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                face_objects= self.front_face.detectMultiScale(gray_img, 1.3, 5)
                is_selected = False

                # for all faces in a pictures
                for (x, y, w, h) in face_objects:
                    is_selected = True
                    cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)
                    j += 1

                if is_selected:
                    cv2.imwrite(self.file_name + "/selected/" + "img" + str(i) + ".jpg", img)
                    i += 1

        print("number founded faces: " + str(j))
        print("number pictures with faces: " + str(i))



#cat/human mode
crawler1 = crawler('cat')

crawler1.open_dir()
crawling_list_urls = crawler1.get_urls()
crawler1.collect_images(crawling_list_urls)
crawler1.classify()

print ("END")











