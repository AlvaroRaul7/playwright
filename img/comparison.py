from pathlib import Path
import os
from playwright.sync_api import sync_playwright
from image_similarity_measures.quality_metrics import rmse, ssim, sre
import cv2
import numpy as np



def Compare_Images(Link,Locator):

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)

        # To save cookies to a file first extract them from the browser context:
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        page.goto(Link)
        image_bytes = page.screenshot(
            full_page=True,   # this will try to scroll to capture full page
            path='screenshot.png',  # this will save the screenshot directly to a file
        #clip={"x": 0, "y": 0, "width": 100, "height": 100},  # this will clip the screenshot to a specific region
        )
        # or we can save it manually
        Path("screenshot.png").write_bytes(image_bytes)
    
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)

        # To save cookies to a file first extract them from the browser context:
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        page.goto(Link)
        image_bytes1 = page.locator(Locator).screenshot( path= 'screenshotElement.png' )
        Path("screenshotElement.png").write_bytes(image_bytes1)
    
    original = cv2.imread("screenshot.png")
    duplicate = cv2.imread("screenshotElement.png")
    scale_percent = 100
    width = int(original.shape[1] * scale_percent / 100)
    height = int(original.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_image = cv2.resize(duplicate, dim, interpolation = cv2.INTER_AREA)
    # Use RMSE to compare the images
    rmse_result = rmse(original, resized_image)
    print(rmse_result)
    
    return rmse_result


        

        
