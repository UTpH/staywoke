# staywoke
Hack submission for Hack(H)er413

## Methodology
We detect both eyes of the driver using facial landmark points(6 points define each eye) in real-time. The algorithm then checks 20 consecutive frames and calculates the Eye Aspect Ratio(the ratio of distances between the vertical eye landmarks and the distances between the horizontal eye landmarks). If it is less than 0.25, an alert is generated. We use Bose Soudtouch apis to play loud music on Bose speakers to alert the driver and create a display an alert as well.
We know that the return value of the eye aspect ratio will be approximately constant when the eye is open. The value will then rapid decrease towards zero during a blink.
If the eye is closed, the eye aspect ratio will remain approximately constant, but will be much smaller than the ratio when the eye is open. 
1. When the ratio is constant -> eye is open. 
2. Rapidly drops to zero, then increases again -> a blink has taken place. 
3. If the value falls but does not increase again -> the person has closed their eyes.

## Instructions to Run

- Install dependencies - openCV, scipy, imutils, dlib
- Run the following command

```python drowsiness_detection.py```
