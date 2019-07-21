# Awesome-ADS-by-RICOH

Nowadays most of advertising is targeted, and you get to look at what interest you whether you are browsing the internet, on facebook, twitter and almost every social network. BUT that is not the case on the streets. When you go out you can get a wide range of advertisements that go from things you will never use to maybe something useful but expensive, and everything in between. Street advertisements are not really targeted, and lack really the statistics and impact they could be generating. And sometimes when it goes through several ads and you get one you like it changes and you get lost in a sea of ads! That is quite a shame in the age of IoT, image manipulation and Computer vision, I think we can do better and give a much nicer experience to both businesses and consumers.

<img src="https://i.ibb.co/jzVRmF6/ADStheta.png" width="1000">

Always use technology to improve the world, if you are a black hat or gray hat hacker please abstain at this point ......... or at least leave your star to make me feel less guilty XP.

# Table of contents

* [Introduction](#introduction)
* [Materials](#materials)
* [Connection Diagram](#connection-diagram)
* [Theta Setup](#theta-setup)
* [Laptop Setup](#laptop-setup)
* [Python Setup](#pyhton-setup)
* [The Final Product](#the-final-product)
* [Future Rollout](#future-rollout)
* [Our Plugin](#our-plugin)
* [References](#references)

## Introduction:

I will build an experiential advertising platform. Imagine going through the streets minding your own business. And then suddenly, you look directly into a place where an ad should be, and in a matter of seconds you find yourself looking at an incredible product, something you would like to buy or possess, or maybe an incredible offer or a service you really need right now! 

It will help by taking advantage of targeting their ads also on the Digital out of home spaces, and also measure their consumption to help understand their audience better. Publishers will have means to get the required traction of their consumers seamlessly, and monetize their existing infrastructure better. It will be an intelligent Digital-Out-Of-Home ad platform that transforms traditional digital outdoor advertising screens into targeted ad-spots.

Existing solutions for out of home ads do not do this, they base all their hypothesis on data models that seem to work, but have little evidence of this. And it is quite different of what google and others do because it requires hardware out of the user’s possession.

## Materials:

Hardware:
- Ricoh Theta V   x1.
- Laptop          x1.

Software:
- Android Studio.
- Theta Software: 
https://support.theta360.com/en/download/
- Ricoh Theta native API.
- Python.
- ADS.

## Connection Diagram:

This is the connection diagram of the system:

<img src="https://i.ibb.co/Yp23h0N/ads.png" width="800">

## Theta Setup:

<img src="https://media.wired.com/photos/5a679b59d0d73e186fbefd64/master/w_799,c_limit/Ricoh-TopArt.jpg" width="600">

The first part to be able to do this project is to put your Theta V camera in Developer mode, this is a simple but possibly a little slow process, recommend having 2 or 3 days for the engineers in charge of Ricoh Theta to unlock the developer mode of your camera

Read the following documentation by Jessie Cassman to perform this process.

https://community.theta360.guide/t/ricoh-blog-post-theta-plug-in-development-steps-for-putting-your-theta-into-developer-mode/3141

## Laptop Setup:

<img src="https://1.bp.blogspot.com/-PwaAONmMm78/V-ASbVPG39I/AAAAAAAADZY/boHNhTW5V4Y45qzx6gIweePgoO2VkIhfQCLcB/s1600/image04.png" width="600">

While they are releasing the Developer mode from Ricoh Theta, you can start downloading the latest version of Android Studio at the following link:

https://developer.android.com/studio

To have the best experience with your Ricoh Theta V camera, we recommend downloading all the software that Ricoh Theta offers (FREE).

https://support.theta360.com/en/download/

Especially for this project and to perform a control of the camera using API, it will be necessary to have installed, some specialized software to execute programs written in Python, this can be done with Terminal, CMD or an IDE such as Anaconda, in this tutorial we will use Anaconda to run the programs.

https://www.anaconda.com/distribution/

## Python Setup:

<img src="https://pydata.org/cordoba2018/media/sponsor_files/Anaconda_stacked_RGB.png" width="600">

We have to have the following libraries installed in Anaconda.

- requests 
- json
- shutil
- OpenCV 
- argparse
- pygame
- pickle 
- time

To install all the packages you have to run the following commands in Anaconda Prompt.

      conda install -c anaconda pip
      pip install pickle
      pip install pygame
      conda install -c conda-forge pytest-shutil 
      conda install -c conda-forge opencv 
      
Once we have all the installed packages, we can run the programs in the "Python Scripts" folder without errors, all files have to run from the "Python Scripts" folder due to the files that we need to running correctly, such as deep learning models to identify the gender and age of the subjects that are viewed by the camera.

It is necessary to run at least once the "Save Pickle.py" program.

After running for the first time, the other programs run without problems.

## The Final Product:

In order to run the project without problem, we need to connect the laptop to the camera via wifi.

The process to activate the AP point of the camera is the following:

1. When the camera is connected to a smartphone via a Wi-Fi network, you can use your smartphone to shoot remote photos and view photos.

2. Press the power button on the camera to turn the power on

<img src="https://support.theta360.com/uk/manual/img/p006.png" width="250">

3. Press the wireless button to turn the wireless function on

<img src="https://support.theta360.com/uk/manual/img/p009.png" width="250">

-  The wireless lamp lights in red.
      
4. Display the Wi-Fi settings of your smartphone

Select the SSID of the camera from the network list and enter the password

<img src="https://support.theta360.com/uk/manual/img/p007.png" width="250">

- The serial number printed on the base of the camera is the same as the SSID and password. 
- The SSID is "THETA" plus the numbers in the (B) section (in this case "THETA001017"). The password is the numbers in the (A) section (in this case "00001017").

Connect your Laptop to the camera.

In order for the product to work completely we need to run the following python programs in parallel in two different kernel, this is easily possible from Anaconda.

<img src="https://i.ibb.co/0qVZ951/Consoles.png" width="1000">

### Explanation of program "Theta, take, preocess and deploy data.py":

This program has the function of connecting to the Theta API.

Take a 360 photo.

Process it with DL models to take Gender and Age data:

The process to obtain age and gender is done through the following process.
- Get the faces inside the image using Haarcascades.
- Process it using DL models.

Once we have the whole process we will remove the photo from the camera so as not to fill the memory in the long run.

Once we have the counting of people of male and female gender, we keep the variable "check" in a pickle file.

The update of the "check" variable occurs every 20 seconds, the minimum that the update should last is 30 seconds, because each ad lasts approximately 30 seconds, so always the ad that is reproduced will be the most efficient for the public at all times.

### Explanation of program "OpenVideo.py":

In this program we can execute the reproduction of the announcements and it works in the following way.

If the "check" variable is equals 0, it means that most of those around the camera are men, the program will produce only ads for men.

If the "check" variable is equals 1, most of the subjects around the camera are women, the program will produce only ads for women.

If the "check" variable is equals 2, then the ads will be reproduced as 1 man and 1 woman.

This is an example how the program works in a laptop with 2 screens in a final product we display the ads in a big screen.

Each ad lasts approximately 30 seconds.

<img src="https://i.ibb.co/cXmT39n/Screenshot-2.png" width="1000">

## Important Note:

During the development process, Android Studio was used to perform all OpenCV processing within the Theta, however the examples available in the following resources did not work to make use of the functions to use "Haarcascades" or Neural Networks:

- https://github.com/theta-skunkworks
- https://github.com/theta360developers
- https://github.com/codetricity
- https://github.com/ricohapi

It was decided to make an independent plugin for the ricoh theta plugin store: https://pluginstore.theta360.com/

### Our Epic Video:

Video: Click on the image
[![Video](https://i.ibb.co/jzVRmF6/ADStheta.png)](https://youtu.be/dW3Mtp7snsI)

Sorry github does not allow embed videos.

## Future Rollout:

// Inventate algo XP

## Our Plugin:

### Download Link: Insertar link cuando este en la tienda.

<img src="http://theta360.guide/plugin-user-guide/main/img/install/store.png" width="400">

### Install:

Original Install Guide Link: http://theta360.guide/plugin-user-guide/main/install/

Connect your THETA to your computer and click on the Install button.

<img src="http://theta360.guide/plugin-user-guide/main/img/install/install.png" width="400">

The Ricoh Desktop Application will automatically start for plug-in installation.

### Configure Plug-in to Launch:

As the THETA V can save multiple plug-ins to internal storage, you need to specify the active plug-in to launch when the camera is put into plug-in mode.

There are many ways to select the active plug-in.

Developers can use the open API of the THETA to set the plug-in. This document focuses on using the official desktop app to specify the active plug-in.

### Set Active Plug-in with Desktop App:

Connect your desktop computer or laptop to the THETA with a USB cable. Under the file menu, select Plug-in management....

<img src="http://theta360.guide/plugin-user-guide/main/img/install/plug-in-manager.png" width="400">

Select the plug-in that you want to use.

<img src="http://theta360.guide/plugin-user-guide/main/img/install/plug-in-list.png" width="400">

### Idea:

Develop a plugin that could use OpenCv to process images and generate interesting filters for the camera.

Filters to be used:

- Image Equalization (color).
- Binarization of image or Threshold (Red, Green and Blue).
- Grayscale.
- Blur.
- Erosion-Dilatation.
- Negative

### How it Works:

Once activated the Plugin, we can select the desired filter using the "Mode" button, depending on the color that the Wi-Fi symbol has, it will be the effect that will be applied to the image.

- Blue: Image Equalization (color).
- Green: Image Binarization or Threshold (Red, Green and Blue).
- Cyan: Grayscale.
- Magenta: Blur.
- Yellow: Erosion-Dilatation.
- White: Negative.
- Once the filter is selected, we only have to press the Shutter button to take the image and save it, the image will be saved in a folder called "Filtered Images".

Note: when the filter is being applied the WiFi symbol will flash, until it stops blinking, do not press any other button, this process takes 1 - 4 seconds depending on the filter.

### Developing:

The filters were made with the following code lines:

- Image Equalization (color):

      fileUrl = String.format("%s/%s_equalize.jpg", Constants.PLUGIN_DIRECTORY, dateTimeStr);
      Mat rgbImage = new Mat(img.size(), img.type());
      Imgproc.cvtColor(img, img, Imgproc.COLOR_RGB2YCrCb);
      List<Mat> channels = new ArrayList<Mat>();
      Core.split(img, channels);
      Imgproc.equalizeHist(channels.get(0), channels.get(0));
      Core.merge(channels, img);
      Imgproc.cvtColor(img, img, Imgproc.COLOR_YCrCb2BGR);
      
- Binarization of image or Threshold (Red, Green and Blue):

      fileUrl = String.format("%s/%s_threshold.jpg", Constants.PLUGIN_DIRECTORY, dateTimeStr);
      Mat rgbImage = new Mat(img.size(), img.type());
      Imgproc.cvtColor(img, img, Imgproc.COLOR_RGB2YCrCb);
      Imgproc.threshold(img, img, 127.0, 255.0, Imgproc.THRESH_BINARY);
      Imgproc.cvtColor(img, img, Imgproc.COLOR_YCrCb2RGB);
      
- Grayscale:

      fileUrl = String.format("%s/%s_gray.jpg", Constants.PLUGIN_DIRECTORY, dateTimeStr);
      Imgproc.cvtColor(img, img, Imgproc.COLOR_RGB2GRAY);
      
- Blur:

      fileUrl = String.format("%s/%s_blur.jpg", Constants.PLUGIN_DIRECTORY, dateTimeStr);
      Imgproc.cvtColor(img, img, Imgproc.COLOR_RGB2BGR);
      Imgproc.blur(img, img, new Size(25,25));
      
- Erosion-Dilatation.

      fileUrl = String.format("%s/%s_erodedilate.jpg", Constants.PLUGIN_DIRECTORY, dateTimeStr);
      Imgproc.cvtColor(img, img, Imgproc.COLOR_RGB2GRAY);
      Imgproc.threshold(img, img, 0, 255, Imgproc.THRESH_BINARY_INV+Imgproc.THRESH_OTSU);
      
- Negative:
      
      fileUrl = String.format("%s/%s_negative.jpg", Constants.PLUGIN_DIRECTORY, dateTimeStr);
      Core.bitwise_not(img,img);

### Video:

Video: Click on the image
[![Demo](https://i.ibb.co/y45kSD8/Theta-Magic-Filters.png)](https://youtu.be/wUKLVBrk_Mk)

Sorry github does not allow embed videos.
