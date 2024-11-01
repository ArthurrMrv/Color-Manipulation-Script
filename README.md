# Color Manipulation Script

This Python script allows users to modify specific colors in an image based on a provided hex color mapping. The script also includes functionality to lighten colors and visualize them in a plot.

## Features

- Convert RGB colors to hex format and vice versa.
- Extract unique colors from an image.
- Lighten colors by blending with white.
- Change specific colors in an image based on a hex color map.
- Visualize colors in a simple plot.

## Requirements

To run this script, you need to have Python installed along with the following libraries:

- Pillow
- Matplotlib
- tqdm

You can install these dependencies using pip:

```bash
pip install Pillow matplotlib tqdm
```

## Usage

To run the script, use the command line. The script takes the following arguments:

```
python script_name.py <input_image_path> <output_image_path> [--factor=<lightening_factor>]
```

- `<input_image_path>`: Path to the input image file.
- `<output_image_path>`: Path where the modified image will be saved.
- `--factor=<lightening_factor>` (optional): A float value between 0 and 1 that determines how much to lighten the colors. The default factor is `0.4`.

### Example

```bash
python main.py input_image.png output_image.png --factor=0.5
```

## Functions

### `rgb_to_hex(rgb)`

Converts an RGB tuple to a hex color string.

### `hex_to_rgb(hex_color)`

Converts a hex color string to an RGB tuple.

### `colors_in_img(image_path)`

Extracts unique colors from the specified image.

### `plot_cols(colors, save_path)`

Plots the given colors and saves the plot as an image.

### `lighten_color(hex_color, factor=0.4)`

Lightens a hex color by blending it with white.

### `convert_image_px(input_path, output_path, hex_color_map)`

Changes specific colors in an image based on a provided hex color map.

## Example Workflow

1. **Extract Colors**: Use `colors_in_img(image_path)` to extract unique colors from the image.
2. **Lighten Colors**: Apply `lighten_color(hex_color, factor)` to lighten the extracted colors.
3. **Create a Hex Color Map**: Map original colors to their lightened versions.
4. **Modify Image**: Use `convert_image_px(input_path, output_path, hex_color_map)` to modify the image colors according to the hex color map.
5. **Plot Colors**: Use `plot_cols(colors, save_path)` to visualize the colors.

## Notes

- Ensure that the input image is in a supported format (e.g., PNG, JPEG).
- The script uses a progress bar to indicate processing progress when modifying the image.

## Examples

Before:
![Before](Centralesupelec logo.jpeg)

After (factor = 0.6):
![After](Centralesupelec logo Changed.jpeg)




