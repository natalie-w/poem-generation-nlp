# poem-generation-nlp

Reference from https://medium.com/@ngwaifoong92/beginners-guide-to-retrain-gpt-2-117m-to-generate-custom-text-content-8bb5363d8b7f and https://towardsdatascience.com/object-detection-with-10-lines-of-code-d6cb4d86f606.

Poem dataset from https://github.com/researchmm/img2poem/tree/master/data.

# Image Step:
Open a terminal
Install tensorflow pip3 install tensorflow
Install OpenCV pip3 install opencv-pytho
Install Keras pip3 install keras
Install ImageAI pip3 install imageai --upgrade
Download the RetinaNet model file that will be used for object detection via this "link".
Go to image directory and put in a picture in JPG format. Rename the image file as image.jpg.
Run python detection.py to see the objects in the picture.

# Poetry Step:
Open a terminal
Run python src/interactive_conditional_samples.py --temperature 1 --top_k 40 --model_name poem
Get the output from the previous step and type it in when you see Model prompt.
Read it out loud and have fun!
