# ============================================================
# Program  : Edge Detection using OpenCV (Canny)
# Author    : Ishwari Vijaykumar Surve
# Target:
# Detect the edges of a real image using OpenCV Canny
# Needs     : sample.png in the same folder
# ============================================================

import cv2

print("=" * 60)
print("   Deep Learning : CNN Edge Detection")
print("   Program 28 : Edge Detection using OpenCV (Canny)")
print("=" * 60)
print("Press any key in an image window to close all windows.")

# Load image
img = cv2.imread("sample.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Show Original Image
cv2.imshow("Original Image", img)

# Show Grayscale Image
cv2.imshow("Grayscale Image", gray)

# Show Edge Detected Image
cv2.imshow("Edges", edges)

# Wait until key press
cv2.waitKey(0)
cv2.destroyAllWindows()
