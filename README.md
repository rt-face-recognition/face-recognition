# InstaFace

A [HackTheNorth 2018](https://hackthenorth.com/) project! More information [here](https://devpost.com/software/instaface)


![gallery](https://user-images.githubusercontent.com/8631008/45700692-33b89700-bb3b-11e8-97a6-8ae6456280c2.jpg)


# Description

A hackaton project inspired by problems in the health field.

This app allows for easy recognition of faces using OpenCV. This essentially identitifies faces in a video feed and actively matches it to people in a contacts list. This is then sent to a Fitbit which notifies the wearer of the person's identity.


# Resources used
We used OpenCV, python, flask and heroku to build it and deployt it; The Fit-Bit Studio and Javascript was used for the watch integration.

# Files and stucture
`main.py` represents the main video acquiring program, based on a [project](https://github.com/ageitgey/face_recognition) developed by the canadian army.

The `index.js` and ` 	indexCompanion.js` files are to be imported into Fit-Bit studio for functioning of the app. Ideally, use the `Face-Recognition-export.zip` file instead since it defines graphical settings needed for correct running of the Javascript code.

All the rest is mostly Flask based and for deploy with Heroku.

