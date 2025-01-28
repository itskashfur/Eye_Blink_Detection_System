Real-Time Eye Blink Detection using Facial Landmarks
 
* Abstract.
  A real-time algorithm to detect eye blinks in a video sequence from a standard camera is proposed. Recent landmark detectors, trained on in-the wild datasets exhibit excellent robustness against ahead orientation with respect to a camera, varying illumination and facial expressions. We show that the landmarks are detected precisely enough to reliably estimate the level of the eye opening. The proposed algorithm therefore estimates the landmark positions, extracts a single scalar quantity– eye aspect ratio (EAR)– characterizing the eye opening in each frame. Finally, an SVM classifier detects eye blinks as a pattern of EAR values in a short temporal window. The simple algorithm outperforms the state-of-the-art results on two standard datasets
  
![495123_1_En_77_Fig2_HTML](https://github.com/user-attachments/assets/9a57141c-50d3-4611-90a4-ae7d0ab7e1b8)
Figure 1: Open and closed eyes with landmarks pi automatically detected by [1]. The eye aspect ratio EAR in Eq. (1) plotted for several frames of a video sequence. A single blink is present.

* 1. Introduction
   Detecting eye blinks is important for instance in systems that monitor a human operator vigilance,e.g. driver drowsiness [5, 13], in systems that warn a computer user staring at the screen without blink
ing for a long time to prevent the dry eye and the computer vision syndromes [17, 7, 8], in human computer interfaces that ease communication for disabled people [15], or for anti-spoofing protection in face recognition systems [11].Existing methods are either active or passive. Active methods are reliable but use special hardware,often expensive and intrusive, e.g. infrared cameras and illuminators [2], wearable devices, glasses with a special close-up cameras observing the eyes [10].While the passive systems rely on a standard remote camera only.
  Many methods have been proposed to automatically detect eye blinks in a video sequence. Several methods are based on a motion estimation in the eye region. Typically, the face and eyes are detected by a Viola-Jones type detector. Next, motion in the eye area is estimated from optical flow, by sparse tracking [7, 8],
or by frame-to-frame intensity differencing and adaptive thresholding. Finally, a decision is made whether the eyes are or are not covered by eyelids [9, 15]. A different approach is to infer the state of the eye opening from a single image, as e.g. by correlation matching with open and closed eye tem plates [4], a heuristic horizontal or vertical image intensity projection over the eye region [5, 6], a para metric model fitting to find the eyelids [18], or active shape models [14].
  A major drawback of the previous approaches is that they usually implicitly impose too strong requirements on the setup, in the sense of a relative face-camera pose (head orientation), image resolution, illumination, motion dynamics,etc. Especially the heuristic methods that use raw image intensity are likely to be very sensitive despite their real-time performance.
  
  However nowadays, robust real-time facial landmark detectors that capture most of the characteristic points on a human face image, including eye corners and eyelids, are available, see Fig. 1. Mostof the state-of-the-art landmark detectors formulate a regression problem, where a mapping from an image into landmark positions [16] or into other landmark parametrization [1] is learned. These modern landmark detectors are trained on “in-the-wild datasets” and they are thus robust to varying illumination, various facial expressions, and moderatenon-frontal head rotations. An average error of the landmark localization of a state-of-the-art detector is usually below five percent of the inter-ocular distance. Recent methods run even significantly super real-time [12].
  Therefore, we propose a simple but efficient algorithm to detect eye blinks by using a recent facial landmark detector. A single scalar quantity that reflects a level of the eye opening is derived from the landmarks. Finally, having a per-frame sequence of the eye opening estimates, the eye blinks are found by an SVM classifier that is trained on examples of blinking and non-blinking patterns.
  Facial segmentation model presented in [14] is similar to the proposed method. However, their system is based on active shape models with reported processing time of about 5 seconds per frame for the segmentation, and the eye opening signal is normalized by statistics estimated by observing a longer sequence. The system is thus usable for offline processing only. The proposed algorithm runs real-time, since the extra costs of the eye opening from land marks and the linear SVM are negligible.
 
 The contributions of the paper are:
   1. Ability of two state-of-the-art landmark detectors [1, 16] to reliably distinguish between the open and closed eye states is quantitatively demonstrated on a challenging in-the wild dataset and for various face image resolutions.
   2. Anovel real-time eye blink detection algorithm which integrates a landmark detector and a classifier is proposed. The evaluation is done on two standard datasets [11, 8] achieving state-of-the art results.
  The rest of the paper is structured as follows: The algorithm is detailed in Sec. 2, experimental validation and evaluation is presented in Sec. 3. Finally,Sec. 4 concludes the paper.
 ![2-Figure2-1](https://github.com/user-attachments/assets/77504133-e1bd-4ebe-bca9-695eb1965fc1)
Figure 2: Example of detected blinks. The plots of the eye aspect ratio EAR in Eq. (1), results of the EAR thresholding (threshold set to 0.2), the blinks detected by EAR SVM and the ground-truth labels over the video sequence. Input image with detected landmarks (depicted frame is marked by a red line).
 
* 2. Proposed method
  The eye blink is a fast closing and reopening of a human eye. Each individual has a little bit different pattern of blinks. The pattern differs in the speed of closing and opening, a degree of squeezing the eye and in a blink duration. The eye blink lasts approximately 100-400 ms.



![WhatsApp Image 2024-08-15 at 17 10 09](https://github.com/user-attachments/assets/fee9c54e-8873-4e4e-b220-625d6a9053df)
![WhatsApp Image 2024-08-15 at 17 10 09 (1)](https://github.com/user-attachments/assets/8be13259-ca70-4677-a609-aca246b461c4)
![WhatsApp Image 2024-08-15 at 17 10 08](https://github.com/user-attachments/assets/076de5ef-e1d3-45e9-9a3d-7f89e31247ea)
![WhatsApp Image 2024-08-15 at 17 10 08 (2)](https://github.com/user-attachments/assets/a2b18c1a-09d9-4764-82b6-d7cba77da7b8)
![WhatsApp Image 2024-08-15 at 17 10 08 (1)](https://github.com/user-attachments/assets/6edd6a53-d452-4390-bc62-24ede3ae51d1)
![blk1](https://github.com/user-attachments/assets/df3174f4-5897-4b1b-a46e-a98cea9c1658)
![blk](https://github.com/user-attachments/assets/103bf4db-2ed6-41da-acdb-1b85a6f86549)
![WhatsApp Image 2024-08-15 at 17 10 11](https://github.com/user-attachments/assets/3ac83f1b-3aea-424f-8519-5f99d3335bf3)
