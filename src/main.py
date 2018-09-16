import face_recognition
import cv2
import time

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

"""
# Load a sample picture and learn how to recognize it.q
obama_image = face_recognition.load_image_file("C:/Users/francis/PycharmProjects/face-recognition/lib/obama/58015949-079c-492e-9041-c5d499fad45f-Election_2018_Ohio_Obama-GNAMT9AVN.1.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("C:/Users/francis/PycharmProjects/face-recognition/lib/biden/joe-biden-official-portrait_1600jpg.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

francis_image = face_recognition.load_image_file("C:/Users/francis/PycharmProjects/face-recognition/lib/francis.jpg")
francis_encoding = face_recognition.face_encodings(francis_image)[0]


"""
# Create arrays of known face encodings and their names
known_face_encodings = [
    # obama_face_encoding,
    # biden_face_encoding,
    # francis_encoding
]
known_face_names = [
    "Barack Obama",
    "Joe Biden",
    "Francis"
]

# In frames
WAIT_BETWEEN_MATCHES = 30*5

# For not processing the same person multiple times in a short period of time
time_delay = {x: 0 for x in known_face_names}


# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


def post_request(name, picture_time):
    print(name, picture_time)
    pass


while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Every frame update the frame delay if needed
    time_delay = {x: y-1 if y > 0 else 0 for x, y in time_delay.items()}

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

                # Ignore this guy if a delay is happening
                if time_delay[name] != 0:
                    name = "Unknown"
                else:
                    time_delay[name] = WAIT_BETWEEN_MATCHES
                    post_request(name, time.gmtime())

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        if name != 'Unknown':
            post_request(name, time.time())


    # Display the resulting image
    cv2.imshow('Video', frame)


    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
