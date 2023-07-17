from cv2 import namedWindow,WINDOW_NORMAL,imread,imshow,waitKey,destroyAllWindows
import os
import multiprocessing as mp
def show_images(feeling):
    folder_path = 'emotions/'+feeling
    image_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            image_files.append(filename)
    image_files.sort()
    namedWindow('Animation', WINDOW_NORMAL)
    current_image = 0
    while True:
        image_path = os.path.join(folder_path, image_files[current_image])
        image = imread(image_path)
        imshow('Animation', image)
        key = waitKey(40)
        if key == ord('q'):
            break
        current_image = (current_image + 1) % len(image_files)
    destroyAllWindows()
if __name__ == '__main__':

    show_images_process = mp.Process(target=show_images('blink2'))
    show_images_process.start()
    show_images_process.join()
