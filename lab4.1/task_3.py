import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')

body = patches.Ellipse((0.5, 0.4), 0.6, 0.4, facecolor='#DEB887', edgecolor='black', linewidth=2)
ax.add_patch(body)

head = patches.Circle((0.5, 0.7), 0.2, facecolor='#DEB887', edgecolor='black', linewidth=2)
ax.add_patch(head)

left_ear = patches.Polygon([[0.35, 0.85], [0.3, 1.0], [0.45, 0.9]], facecolor='#8B4513', edgecolor='black', linewidth=2)
right_ear = patches.Polygon([[0.65, 0.85], [0.7, 1.0], [0.55, 0.9]], facecolor='#8B4513', edgecolor='black', linewidth=2)
ax.add_patch(left_ear)
ax.add_patch(right_ear)

muzzle = patches.Ellipse((0.5, 0.65), 0.15, 0.1, facecolor='white', edgecolor='black', linewidth=1)
ax.add_patch(muzzle)

nose = patches.Ellipse((0.5, 0.64), 0.05, 0.03, facecolor='black')
ax.add_patch(nose)

left_eye = patches.Circle((0.45, 0.73), 0.03, facecolor='black')
right_eye = patches.Circle((0.55, 0.73), 0.03, facecolor='black')
ax.add_patch(left_eye)
ax.add_patch(right_eye)

left_highlight = patches.Circle((0.448, 0.735), 0.008, facecolor='white')
right_highlight = patches.Circle((0.548, 0.735), 0.008, facecolor='white')
ax.add_patch(left_highlight)
ax.add_patch(right_highlight)

ax.plot([0.48, 0.52], [0.6, 0.6], 'k-', linewidth=2)

left_paw = patches.Ellipse((0.4, 0.2), 0.08, 0.05, facecolor='#DEB887', edgecolor='black', linewidth=1)
right_paw = patches.Ellipse((0.6, 0.2), 0.08, 0.05, facecolor='#DEB887', edgecolor='black', linewidth=1)
ax.add_patch(left_paw)
ax.add_patch(right_paw)

tail = patches.Ellipse((0.8, 0.5), 0.15, 0.05, angle=30, facecolor='#DEB887', edgecolor='black', linewidth=2)
ax.add_patch(tail)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.show()