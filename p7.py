import cv2
import numpy as np

# Create a black image
image = np.zeros((500, 500, 3), dtype=np.uint8)

# Initialize triangle vertices
triangle_vertices = np.array([[250, 100], [100, 400], [400, 400]], np.int32)

# Initialize centroid
centroid = np.mean(triangle_vertices, axis=0, dtype=np.int32)

# Initial color
color = (0, 0, 255)  # Default color: Red

def draw_triangle(image, vertices, color):
    cv2.fillPoly(image, [vertices], color)

def draw_centroid(image, centroid):
    cv2.circle(image, tuple(centroid), 5, (255, 255, 255), -1)

def change_color(event, x, y, flags, param):
    global color
    if event == cv2.EVENT_LBUTTONDOWN:
        color = tuple(np.random.randint(0, 256, 3).tolist())

# Create a window and set the callback function for mouse events
cv2.namedWindow('Triangle with Centroid')
cv2.setMouseCallback('Triangle with Centroid', change_color)

while True:
    # Draw the triangle and centroid
    draw_triangle(image, triangle_vertices, color)
    draw_centroid(image, centroid)

    # Display the image
    cv2.imshow('Triangle with Centroid', image)

    # Check for keyboard events
    key = cv2.waitKey(1) & 0xFF

    # Exit when 'ESC' is pressed
    if key == 27:
        break

cv2.destroyAllWindows()
