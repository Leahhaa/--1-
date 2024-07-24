import os
import argparse
import time
import requests
import concurrent.futures
from multiprocessing import Pool
from aiohttp import ClientSession
import asyncio


def download_image(url):
    start_time = time.time()
    response = requests.get(url)
    image_name = os.path.basename(url)
    with open(image_name, 'wb') as f:
        f.write(response.content)
    end_time = time.time()
    print(f"Downloaded {image_name} in {end_time - start_time:.2f} seconds")


def download_images_threading(urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, urls)


def download_images_multiprocessing(urls):
    with Pool() as pool:
        pool.map(download_image, urls)


async def download_image_async(url, session):
    start_time = time.time()
    async with session.get(url) as response:
        content = await response.read()
        image_name = os.path.basename(url)
        with open(image_name, 'wb') as f:
            f.write(content)
    end_time = time.time()
    print(f"Downloaded {image_name} in {end_time - start_time:.2f} seconds")


async def download_images_async(urls):
    async with ClientSession() as session:
        tasks = [download_image_async(url, session) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download images from URLs")
    parser.add_argument('urls', metavar='URL', type=str, nargs='+', help='URLs of images to download')
    parser.add_argument('--method', choices=['threading', 'multiprocessing', 'async'], default='threading',
                        help='Method to use for downloading images')

    args = parser.parse_args()
    urls = args.urls

    start_time = time.time()

    if args.method == 'threading':
        download_images_threading(urls)
    elif args.method == 'multiprocessing':
        download_images_multiprocessing(urls)
    elif args.method == 'async':
        asyncio.run(download_images_async(urls))

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

'''
Для запуска программы из консоли:
  python fourth_homework.py  https://example.com/image1.jpg --method threading или 
  python fourth_homework.py  https://example.com/image2.jpg --method multiprocessing или
  python fourth_homework.py  https://example.com/image3.jpg --method async
'''
