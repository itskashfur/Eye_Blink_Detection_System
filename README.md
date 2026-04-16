<h1 align="center">Real-Time Eye Blink Detection using Facial Landmarks</h1>
<h2>Abstract</h2>
<p>
A real-time algorithm to detect eye blinks in a video sequence from a standard camera is proposed.
Recent landmark detectors trained on in-the-wild datasets exhibit strong robustness against head orientation,
illumination changes, and facial expressions.
</p>
<p>
The algorithm estimates facial landmark positions and extracts a scalar quantity called the
<strong>Eye Aspect Ratio (EAR)</strong>, which characterizes eye opening in each frame.
A linear SVM classifier detects blinks as a temporal pattern of EAR values.
The proposed method achieves state-of-the-art performance on standard datasets.
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/9a57141c-50d3-4611-90a4-ae7d0ab7e1b8" width="600">
</p>
<p align="center"><em>
Figure 1: Open and closed eyes with automatically detected landmarks.
The EAR signal across frames showing a blink.
</em></p>

<hr>

<h2>1. Introduction</h2>

<p>
Eye blink detection plays a crucial role in applications such as:
</p>

<ul>
  <li>Driver drowsiness monitoring</li>
  <li>Dry-eye prevention systems</li>
  <li>Human-computer interaction for disabled users</li>
  <li>Anti-spoofing in face recognition systems</li>
</ul>

<p>
Existing methods are categorized into:
</p>

<ul>
  <li><strong>Active systems</strong> — use special hardware (infrared cameras, wearable sensors)</li>
  <li><strong>Passive systems</strong> — rely on a standard camera</li>
</ul>

<p>
Traditional passive methods depend heavily on lighting conditions and head orientation.
Modern landmark detectors trained on large in-the-wild datasets offer greater robustness and real-time performance.
</p>

<hr>

<h2>2. Proposed Method</h2>

<p>
An eye blink consists of rapid closing and reopening of the eye,
typically lasting between <strong>100–400 ms</strong>.
</p>

<h3>2.1 Feature Extraction – Eye Aspect Ratio (EAR)</h3>

<p>
For each frame:
</p>

<ul>
  <li>Facial landmarks are detected</li>
  <li>Eye landmarks are extracted</li>
  <li>EAR is computed as a ratio of vertical eye distances to horizontal eye width</li>
</ul>

<p>
EAR properties:
</p>

<ul>
  <li>Approximately constant when eye is open</li>
  <li>Approaches zero when eye is closed</li>
  <li>Invariant to uniform scaling</li>
  <li>Invariant to in-plane rotation</li>
</ul>

<p>
Since blinking is usually synchronous in both eyes,
EAR values from both eyes are averaged.
</p>

<h3>2.2 Classification Using Temporal Window</h3>

<p>
A low EAR value alone does not always indicate a blink.
Therefore, a temporal window approach is used.
</p>

<p>
For 30 FPS video:
</p>

<ul>
  <li>6 frames before and after the current frame are considered</li>
  <li>A 13-dimensional feature vector is constructed</li>
  <li>A linear SVM classifier is trained on annotated blink data</li>
</ul>

<p>
Classification is performed in a sliding-window manner across the video sequence.
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/77504133-e1bd-4ebe-bca9-695eb1965fc1" width="600">
</p>

<p align="center"><em>
Figure 2: EAR signal, thresholding results, SVM predictions, and ground-truth labels.
</em></p>

<hr>

<h2>3. Experiments</h2>

<h3>3.1 Landmark Detection Accuracy</h3>

<p>
The algorithm was evaluated using the <strong>300-VW dataset</strong>,
which contains 50 in-the-wild annotated videos.
</p>

<p>
Two real-time landmark detectors were tested:
</p>

<ul>
  <li><strong>Chehra</strong></li>
  <li><strong>Intraface</strong></li>
</ul>

<p>
Accuracy was measured using average relative landmark localization error,
normalized by the inter-ocular distance (IOD).
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/b56bac77-79e3-4894-9063-684975a61d77" width="600">
</p>

<p align="center"><em>
Figure 3: Landmark detection comparison on original and downscaled images.
</em></p>

<p>
Results indicate:
</p>

<ul>
  <li>Chehra achieves very low localization error in standard conditions</li>
  <li>Intraface is more robust on small face images</li>
  <li>Intraface performs better for eye-specific landmarks</li>
</ul>

<hr>

<h2>Conclusion</h2>

<p>
The proposed real-time eye blink detection framework integrates:
</p>

<ul>
  <li>Robust facial landmark detection</li>
  <li>EAR-based feature extraction</li>
  <li>Linear SVM classification</li>
</ul>

<p>
The system achieves high accuracy while maintaining real-time performance,
making it suitable for vigilance monitoring and human-computer interaction applications.
</p>

<hr>

<p align="center"><strong>End of Document</strong></p>
