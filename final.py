from cv2 import namedWindow, WINDOW_NORMAL, imread, imshow, waitKey, destroyAllWindows
import os
import multiprocessing as mp
import psutil

def show_images(feeling):
    folder_path = 'emotions/' + feeling
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

def monitor_resources():
    while True:
        cpu_percentage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory()
        total_memory = memory_usage.total
        available_memory = memory_usage.available
        used_memory = memory_usage.used
        memory_percentage = memory_usage.percent

        print(f"CPU Usage: {cpu_percentage}%")
        print(f"Total Memory: {total_memory} bytes")
        print(f"Available Memory: {available_memory} bytes")
        print(f"Used Memory: {used_memory} bytes")
        print(f"Memory Percentage: {memory_percentage}%")
        print("------------------------")

if __name__ == '__main__':
    feeling1 = 'blink2'

    show_images_process = mp.Process(target=show_images, args=(feeling1,))
    monitor_resources_process = mp.Process(target=monitor_resources)

    show_images_process.start()
    monitor_resources_process.start()

    show_images_process.join()
    monitor_resources_process.join()
