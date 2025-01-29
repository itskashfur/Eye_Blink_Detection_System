Real-Time Eye Blink Detection using Facial Landmarks
 
* Abstract.
  A real-time algorithm to detect eye blinks in a video sequence from a standard camera is proposed. Recent landmark detectors, trained on in-the wild datasets exhibit excellent robustness against ahead orientation with respect to a camera, varying illumination and facial expressions. We show that the landmarks are detected precisely enough to reliably estimate the level of the eye opening. The proposed algorithm therefore estimates the landmark positions, extracts a single scalar quantity– eye aspect ratio (EAR)– characterizing the eye opening in each frame. Finally, an SVM classifier detects eye blinks as a pattern of EAR values in a short temporal window. The simple algorithm outperforms the state-of-the-art results on two standard datasets
  
![495123_1_En_77_Fig2_HTML](https://github.com/user-attachments/assets/9a57141c-50d3-4611-90a4-ae7d0ab7e1b8)
Figure 1: Open and closed eyes with landmarks pi automatically detected by [1]. The eye aspect ratio EAR in Eq. (1) plotted for several frames of a video sequence. A single blink is present.

1. Introduction
   -----------
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
 
2. Proposed method
   --------------
  The eye blink is a fast closing and reopening of a human eye. Each individual has a little bit different pattern of blinks. The pattern differs in the speed of closing and opening, a degree of squeezing the eye and in a blink duration. The eye blink lasts approximately 100-400 ms.
  We propose to exploit state-of-the-art facial landmark detectors to localize the eyes and eyelid contours. From the landmarks detected in the image,we derive the eye aspect ratio (EAR) that is used as an estimate of the eye opening state. Since the per frame EAR may not necessarily recognize the eye blinks correctly, a classifier that takes a larger temporal window of a frame into account is trained.
 2.1. Description of features
 For every video frame, the eye landmarks are detected. The eye aspect ratio (EAR) between height and width of the eye is computed.
 
 where,p1,....,p6 are the 2D landmark locations, de-picted in Fig. 1.
 The EAR is mostly constant when an eye is open and is getting close to zero while closing an eye. It is partially person and head pose insensitive. Aspect ratio of the open eye has asmallvariance among individuals and it is fully invariant to a uniform scaling of the image and in-plane rotation of the face. Since eye blinking is performed by both eyes synchronously,the EAR of both eyes is averaged. An example of an EAR signal over the video sequence is shown in Fig. 1, 2, 7.
 Asimilar feature to measure the eye opening wassuggested in [9], but it was derived from the eye segmentation in a binary image.
 2.2. Classification
 It generally does not hold that low value of the EAR means that a person is blinking. A low value of the EAR may occur when a subject closes his/her eyes intentionally for a longer time or performs a facial expression, yawning, etc., or the EAR captures a short random fluctuation of the landmarks.
 Therefore, we propose a classifier that takes a larger temporal window of a frame as an input. For the 30fps videos, we experimentally found that 6 frames can have a significant impact on a blink detection for a frame where an eye is the most closed when blinking. Thus, for each frame, a 13-dimensional feature is gathered by concatenating the EARs of its +-6 neighboring frames.
 This is implemented by a linear SVM classifier(called EAR SVM) trained from manually annotated sequences. Positive examples are collected as  ground-truth blinks, while the negatives are those that are sampled from parts of the videos where no blink occurs, with 5 frames spacing and 7 frames margin from the ground-truth blinks. While testing, a classifier is executed in a scanning-window fashion. A13-dimensional feature is computed and classified by EAR SVM for each frame except the beginning and ending of a video sequence.

3. Experiments
   -----------
 Two types of experiments were carried out: The experiments that measure accuracy of the landmark detectors, see Sec. 3.1, and the experiments that evaluate performance of the whole eye blink detection algorithm, see Sec 3.2.
   3.1. Accuracy of landmark detectors
   To evaluate accuracy of tested landmark detectors,weused the 300-VW dataset [19]. It is a dataset containing 50 videos where each frame has associated a precise annotation of facial landmarks. The videos are “in-the-wild”, mostly recorded from a TV.
 The purpose of the following tests is to demonstrate that recent landmark detectors are particularly robust and precise in detecting eyes, i.e. the eye corners and contour of the eyelids. Therefore we prepared a dataset, a subset of the 300-VW, containing sample images with both open and closed eyes. More precisely, having the ground-truth landmark annotation, we sorted the frames for each subject by the eye aspect ratio (EAR in Eq. (1)) and took 10 frames of the highest ratio (eyes wide open), 10 frames of the lowest ratio (mostly eyes tightly shut) and 10 frames sampled randomly. Thus we collected 1500 images.Moreover, all the images were later subsampled (successively 10 times by factor 0.75) in order to evaluate accuracy of tested detectors on small face images.
 Two state-of-the-art landmark detectors were tested: Chehra [1] and Intraface [16]. Both run in real-time1. Samples from the dataset are shown in Fig. 3. Notice that faces are not always frontal to the camera, the expression is not always neutral, people are often emotionally speaking or smiling, etc.Sometimes people wear glasses, hair may occasionally partially occlude one of the eyes. Both detectors perform generally well, but the Intraface is more robust to very small face images, sometimes at impressive extent as shown in Fig. 3.
![28-Figure5 1-1](https://github.com/user-attachments/assets/b56bac77-79e3-4894-9063-684975a61d77)
Figure 3: Example images from the 300-VW dataset with landmarks obtained by Chehra [1] and Intraface [16]. Original images (left) with inter-ocular distance (IOD) equal to 63 (top) and 53 (bottom) pixels. Images subsampled (right) to IOD equal to 6.3(top) and 17 (bottom).
 Quantitatively, the accuracy of the landmark detection for a face image is measured by the average relative landmark localization error, defined as usually
 where xi is the ground-truth location of landmark i in the image, xi is an estimated landmark location by a detector, N is a number of landmarks and normalization factor is the inter-ocular distance (IOD), i.e.Euclidean distance between eye centers in the image.
 First, a standard cumulative histogram of the aver age relative landmark localization error was calculated, see Fig. 4, for a complete set of 49 landmarks and also for a subset of 12landmarksoftheeyesonly,since these landmarks are used in the proposed eye blink detector. The results are calculated for all the original images that have average IOD around 80 px,and also for all “small” face images (including sub Sampled ones) having IOD 50 px. For all landmarks, Chehra has more occurrences of very small errors (up to 5 percent of the IOD), but Intraface is more robust having more occurrences of errors below 10 percent of the IOD. For eye landmarks only, the Intraface is always more precise than Chehra. As already mentioned, the Intraface is much more robust to small images than Chehra. This behaviour is further observed in the following experiment.








![WhatsApp Image 2024-08-15 at 17 10 09](https://github.com/user-attachments/assets/fee9c54e-8873-4e4e-b220-625d6a9053df)
![WhatsApp Image 2024-08-15 at 17 10 09 (1)](https://github.com/user-attachments/assets/8be13259-ca70-4677-a609-aca246b461c4)
![WhatsApp Image 2024-08-15 at 17 10 08](https://github.com/user-attachments/assets/076de5ef-e1d3-45e9-9a3d-7f89e31247ea)
![WhatsApp Image 2024-08-15 at 17 10 08 (2)](https://github.com/user-attachments/assets/a2b18c1a-09d9-4764-82b6-d7cba77da7b8)
![WhatsApp Image 2024-08-15 at 17 10 08 (1)](https://github.com/user-attachments/assets/6edd6a53-d452-4390-bc62-24ede3ae51d1)
![blk1](https://github.com/user-attachments/assets/df3174f4-5897-4b1b-a46e-a98cea9c1658)
![blk](https://github.com/user-attachments/assets/103bf4db-2ed6-41da-acdb-1b85a6f86549)
![WhatsApp Image 2024-08-15 at 17 10 11](https://github.com/user-attachments/assets/3ac83f1b-3aea-424f-8519-5f99d3335bf3)
