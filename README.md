# Chrome Dino Game Automation 🦖

This project automates the Chrome Dinosaur (T-Rex) game using Python. The script detects obstacles by analyzing screen pixels and automatically presses the space bar to make the dinosaur jump. This project was built as part of a learning assignment to understand screen automation and basic computer vision concepts.

## Technologies Used
- Python  
- Pillow (PIL) – screen capture and image processing  
- PyAutoGUI – keyboard automation  
- NumPy – pixel analysis  

## How It Works
The script captures a small region of the screen in front of the dinosaur, converts it to grayscale, and counts dark pixels representing obstacles. When an obstacle is detected, it simulates a space bar press to make the dinosaur jump. A cooldown mechanism is used to prevent repeated jumps.

## How to Run
1. Install dependencies:
```bash
pip install pyautogui pillow numpy
```

2. Open the game:
- Visit: https://elgoog.im/t-rex/
- Press **F11** for fullscreen
- Ensure browser zoom is **100%**

3. Run the script:
```bash
python dino_bot.py
```

4. Switch back to the browser within 5 seconds and watch the bot play.

## Configuration
The detection region may need adjustment depending on screen resolution:
```python
SCAN_REGION = (560, 350, 610, 400)
```
You can also tune the pixel threshold and jump cooldown values inside the script for better performance.

## Limitations
This solution uses pixel-based detection, which is sensitive to screen resolution, browser zoom level, and theme (light or dark mode). It is intended for learning purposes and is not a fully robust AI-based solution.

## Learning Outcome
- Screen automation using Python  
- Image processing with Pillow  
- Real-time decision-making using pixel data  
- Understanding limitations of basic computer vision techniques  

## Author
Created as part of a Python automation learning assignment.
