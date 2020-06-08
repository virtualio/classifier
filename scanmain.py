
# import the necessary packages
import numpy as np
import cv2
import urllib.request
import os


class crawler:

    crawling_links = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    number_of_images = 20
    file_name = "Humans"




    def __init__(self):
        print("Number of urls to crawl: " + str(self.number_of_images))



    def open_dir(self):
        if not os.path.exists(self.file_name + "/selected"):
            os.makedirs(self.file_name + "/selected")
        if not os.path.exists(self.file_name + "/not_selected"):
            os.makedirs(self.file_name + "/not_selected")


    def get_urls(self):

        crawling_list_html = urllib.request.urlopen(self.crawling_links).read()
        return crawling_list_html.decode()


    def collect_iamges(self, crawling_list_urls):

        pic_num = 0

        for url in crawling_list_urls.split('\n'):

            try:
                urllib.request.urlretrieve(url, self.file_name + '/' + str(pic_num+1) + '.jpg')                
                #img = cv2.imread(self.file_name + '/'+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
                # should be larger than samples / pos pic (so we can place our image on it)
                #resized_image = cv2.resize(img, (100, 100))
                #cv2.imwrite(self.file_name + '/'+str(pic_num)+".jpg",resized_image)
                
                pic_num += 1
                if pic_num > self.number_of_images:
                    print("pictures saved: "+str(pic_num))
                    break

            except Exception as e:
                pass  






crawler1 = crawler()

crawler1.open_dir()
#crawling_list_urls = crawler1.get_urls()
#crawler1.collect_iamges(crawling_list_urls)

print ("END")











