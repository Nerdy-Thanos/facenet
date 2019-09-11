# facenet
Face detection and recognition

This uses Keras and tensorflow(backend) to create a compilation of layers of a sequential neural network and save it as a model.

Install the required dependencies by running the (pip3 install -r requirements_cpu.txt) for a system without a GPU
For a system with GPU, run the (pip3 install -r requirements_gpu.txt
Make sure a compatible version of CUDA and cuDNN are installed on top of tensorflow.

Run the Generating_training_data.py to generate your training data. make sure to enable your webcam or camera.

Your training directory should be in the following format
----facenet
    |___people
        |__PERSON NAME
  

This will enable the camera to record a video and capture frames. HAARCASCADE is used to detect facial features and a face cut is 
saved in the directory.

Capture required images by tweaking the "pic_no" in the script.

run the trainer.py script to create and train a Keras model. 

On Subsequent runs, load the saved model by addint the option face_model = load_model('MODEL_NAME') 
instead of creating a new model everytime.

Tweak the learning rate and batch size to ensure minimum loss. Change the number of epochs as required

Run the recognizer.py script to detect and recognize faces.

Change the "a" and "people" dictionary for everyone person added in the people directory
