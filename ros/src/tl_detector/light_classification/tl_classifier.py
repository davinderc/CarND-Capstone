from styx_msgs.msg import TrafficLight
from keras.models import load_model
import h5py

class TLClassifier(object):
    def __init__(self):
        #TODO load classifier
        
        model = load_model('model.h5')
        pass

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        #TODO implement light color prediction
        #  Check what the styx_msgs/TrafficLight msg should look like to 
        #  create the correct output
        light_color = model.predict(image)
        if(light_color == 4):
            return TrafficLight.UNKNOWN
        if(light_color == 2):
            return TrafficLight.GREEN
        if(light_color == 1):
            return TrafficLight.YELLOW
        if(light_color == 0):
            return TrafficLight.RED
