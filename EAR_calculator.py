from scipy.spatial import distance as dist
def eye_aspect_ratio(eye):
	a = dist.euclidean(eye[1], eye[5])
	b = dist.euclidean(eye[2], eye[4])
	c = dist.euclidean(eye[0], eye[3])

	ear = (a + b) / (2.0 * c)
	return ear

def mouth_aspect_ratio(mouth): 
	a = dist.euclidean(mouth[13], mouth[19])
	b = dist.euclidean(mouth[14], mouth[18])
	c = dist.euclidean(mouth[15], mouth[17])

	mar = (a + b + c) / 3.0
	return mar