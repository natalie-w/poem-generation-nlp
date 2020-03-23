{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "#%pip install tensorflow\n",
    "#%pip install opencv-python\n",
    "#%pip install keras\n",
    "#%pip install imageai --upgrade"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:From //anaconda3/lib/python3.7/site-packages/tensorflow/python/ops/resource_variable_ops.py:435: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.\n",
      "Instructions for updating:\n",
      "Colocations handled automatically by placer.\n",
      "tracking <tf.Variable 'Variable:0' shape=(9, 4) dtype=float32> anchors\n",
      "tracking <tf.Variable 'Variable_1:0' shape=(9, 4) dtype=float32> anchors\n",
      "tracking <tf.Variable 'Variable_2:0' shape=(9, 4) dtype=float32> anchors\n",
      "tracking <tf.Variable 'Variable_3:0' shape=(9, 4) dtype=float32> anchors\n",
      "tracking <tf.Variable 'Variable_4:0' shape=(9, 4) dtype=float32> anchors\n",
      "truck  :  58.30690264701843\n",
      "car  :  69.10769939422607\n",
      "car  :  61.42861843109131\n",
      "car  :  72.09374904632568\n",
      "car  :  93.20825338363647\n",
      "car  :  56.84356689453125\n",
      "car  :  90.43924808502197\n",
      "truck  :  50.30401349067688\n",
      "car  :  51.080310344696045\n",
      "car  :  57.31037259101868\n",
      "car  :  55.43476939201355\n",
      "car  :  72.57300615310669\n",
      "car  :  90.1898741722107\n",
      "car  :  65.9139633178711\n",
      "truck  :  64.46212530136108\n",
      "car  :  63.0946159362793\n",
      "car  :  72.85314798355103\n",
      "car  :  92.99613237380981\n"
     ]
    }
   ],
   "source": [
    "from imageai.Detection import ObjectDetection\n",
    "import os\n",
    "\n",
    "execution_path = os.getcwd()\n",
    "\n",
    "detector = ObjectDetection()\n",
    "detector.setModelTypeAsRetinaNet()\n",
    "detector.setModelPath( os.path.join(execution_path , \"resnet50_coco_best_v2.0.1.h5\"))\n",
    "detector.loadModel()\n",
    "detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , \"image.jpg\"), output_image_path=os.path.join(execution_path , \"imagenew.jpg\"))\n",
    "\n",
    "for eachObject in detections:\n",
    "    print(eachObject[\"name\"] , \" : \" , eachObject[\"percentage_probability\"] )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
