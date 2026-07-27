# DrawDistance
 
> A distance-annotation visualization **package built for [NovaVision](https://github.com/novavision-ai)**.
 
## Overview
 
**DrawDistance** is a NovaVision component that overlays distance measurements onto an image. For each distance detection it draws a line between two keypoints and, when available, prints the measured distance (in centimeters) at the midpoint of that line. It's typically placed at the end of a pipeline to visualize the output of a distance-measurement component.
 
## Pipeline
 
- **Inputs** — `inputImage` (the frame to draw on) and `inputDetections` (distance detections, each carrying two `keyPoints` and an optional `distanceCm`).
- **Output** — `outputImage`: the same frame with distance lines and labels drawn on it.
## How It Works
 
1. Read the input frame from the shared image store.
2. For each detection with at least two keypoints, draw a line between the two points.
3. If a `distanceCm` value is present, render it as a `"<value> cm"` label at the line's midpoint.
4. Write the annotated frame back and return it as the output.
## Configuration
 
| Config | Default | Description |
|--------|---------|-------------|
| `configColor` | `#00FF00` | Hex color for the lines and labels. |
| `configThickness` | 2 | Line thickness in pixels (1–10). |
| `configFontScale` | 0.5 | Size of the distance label text (0.1–3.0). |
 
## Structure
 
```
DrawDistance.py                # Executor entry point
src/
├── models/PackageModel.py     # Pydantic schemas (inputs, output, configs)
└── utils/response.py          # Response builder
```
 
## Install
 
```bash
pip install .
```
 
Requires **Python 3.6+**, OpenCV (`opencv-python-headless`), and the NovaVision `sdk`. Designed to run inside the NovaVision runtime.
 
## License
 
[MIT](LICENSE)
