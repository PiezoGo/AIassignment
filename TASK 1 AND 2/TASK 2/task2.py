# pip install python-constraint pillow matplotlib

from constraint import Problem
from PIL import Image
import matplotlib.pyplot as plt

# Load and display the image
img = Image.open("australiamap.png")

plt.figure(figsize=(10, 8))
plt.imshow(img)
plt.axis('off')
plt.title("Map of Australia", fontsize=13)
plt.tight_layout()
plt.show()

# pip install python-constraint pillow matplotlib

from constraint import Problem
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ─── (a) Load the Australia map image ─────────────────────────────────────────
img = Image.open("australiamap.png")

# ─── (b) Constraint Satisfaction Problem ──────────────────────────────────────
problem = Problem()

regions = ['WA', 'NT', 'SA', 'QLD', 'NSW', 'VIC', 'TAS']
colors  = ['Blue', 'Red', 'Green']

for region in regions:
    problem.addVariable(region, colors)

# Real adjacencies from the map
adjacencies = [
    ('WA',  'NT'),
    ('WA',  'SA'),
    ('NT',  'SA'),
    ('NT',  'QLD'),
    ('SA',  'QLD'),
    ('SA',  'NSW'),
    ('SA',  'VIC'),
    ('QLD', 'NSW'),
    ('NSW', 'VIC'),
    # TAS is an island — no land adjacencies
]

for r1, r2 in adjacencies:
    problem.addConstraint(lambda a, b: a != b, (r1, r2))

solution = problem.getSolution()

print("CSP Colouring Solution:")
print("-" * 30)
for region, color in solution.items():
    print(f"  {region:5s} → {color}")

# ─── (c) Display the map image with colour labels overlaid ────────────────────
color_map = {
    'Blue':  '#4A90D9',
    'Red':   '#E05C5C',
    'Green': '#5DAA5D',
}

# Approximate label positions on the image (x, y as fractions of image size)
label_positions = {
    'WA':  (0.22, 0.50),
    'NT':  (0.45, 0.32),
    'SA':  (0.47, 0.62),
    'QLD': (0.70, 0.35),
    'NSW': (0.75, 0.62),
    'VIC': (0.72, 0.78),
    'TAS': (0.72, 0.93),
}

fig, ax = plt.subplots(figsize=(10, 8))
ax.imshow(img)
ax.axis('off')

for region, (fx, fy) in label_positions.items():
    w, h = img.size
    x, y = fx * w, fy * h
    c = solution[region]
    ax.annotate(
        f"{region}\n({c})",
        xy=(x, y),
        fontsize=11,
        fontweight='bold',
        color='white',
        ha='center', va='center',
        bbox=dict(
            boxstyle='round,pad=0.4',
            facecolor=color_map[c],
            edgecolor='white',
            linewidth=1.5,
            alpha=0.88
        )
    )

# Legend
legend_patches = [
    mpatches.Patch(color=color_map[c], label=c)
    for c in ['Blue', 'Red', 'Green']
]
ax.legend(handles=legend_patches, loc='lower left',
          fontsize=11, framealpha=0.85, title='CSP Colours')

ax.set_title("Australia — Map Colouring (Constraint Satisfaction)", fontsize=13, pad=12)
plt.tight_layout()
plt.savefig("australia_coloured.png", dpi=150, bbox_inches='tight')
plt.show()

print("\nSaved as australia_coloured.png")