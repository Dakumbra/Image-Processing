# Samuel Weems
# Project
# CMPS 4553/5353 Summer 2018
# July 03, 2018

# Image Processing techniques learned:
#       Image pixel coordinate system
#       Combining images together
#       Alpha channel transparency
#       Resizing images and image aspect ratios
#       Downsampling filter

import face_recognition
from PIL import Image, ImageFont, ImageDraw
import PIL
import requests
import os

##############################################################################
############################ Crown Function ##################################
##############################################################################

# Given a file with a face in it and a crown file this function locates faces
# adjusts the size of crown(s) appropriately and applies them to each face
#   Note: Easily can add other images to face based on facelandmarks

def crown(crown_file, face_file):
    
    current_face_image = face_file           # Face Image
    crown_image = Image.open(crown_file)     # Crown Image

# Find location of faces and face landmarks in image
#
# Note: Format of each face in face_locations array: (top, right, bottom, left)
# Note: Face Landmarks Keys: chin, left_eyebrow, right_eyebrow, nose_bridge, 
#                            nose_tip, left_eye, right_eye, top_lip, bottom_lip
#                            EXAMPLE: face_landmarks_list[0]['left_eyebrow']
#
#  Draw Squares over faces for visualization: 
#    dr = ImageDraw.Draw(new_image)
#    dr.rectangle(((left,top), (right,bottom)), fill = "black", outline ="blue")

    face_image = face_recognition.load_image_file(current_face_image)
    face_locations = face_recognition.face_locations(face_image)
    face_landmarks_list = face_recognition.face_landmarks(face_image)

# Crown Data

    num_crowns = len(face_locations)
    crown_width, crown_height = crown_image.size
    crown_size_ratio = crown_width/crown_height

    background = Image.open(current_face_image) # Set face image as background image

    for i in range(num_crowns): #Loop creating crown for each face
        top, right, bottom, left = face_locations[i]
        height_adjustment = int((bottom-top)/2)
        horizontal_adjustment = int((right - left)/10)

    # Create Crown(s) and resize
        new_crown_width = right-left
        new_crown_height = new_crown_width / crown_size_ratio
        new_crown_image = crown_image.resize([new_crown_width, int(new_crown_height)], PIL.Image.ANTIALIAS)
            # Note: PIL.Image.ANTIALIAS applies a high-quality downsampling filter

    # Apply crowns to faces
        background.paste(new_crown_image, (left+horizontal_adjustment,top-height_adjustment), new_crown_image)
    
    background.show()   # Display result

##############################################################################
############################ Main Program ####################################
##############################################################################

# Calls function with hard-coded Images (add interface if desired) 

johnson = 'Tina.jpg'
simpson = 'simpson.jpg'
CS_women = 'WomenOFCMPS.jpg'
girls = 'temp.jpg'

crown_file = 'temp.png'

crown(crown_file, johnson)    # function calls
crown(crown_file, simpson) 
crown(crown_file, girls) 
crown(crown_file, CS_women) 












