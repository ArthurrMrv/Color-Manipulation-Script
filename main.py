# #2D2F73

from PIL import Image
import matplotlib.pyplot as plt
from tqdm import tqdm
import sys

def rgb_to_hex(rgb):
    """Convert an RGB tuple to a hex color string."""
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def hex_to_rgb(hex_color):
    """Convert a hex color string to an RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def colors_in_img(image_path):
    """
    Change specific colors in an image based on a provided hex color map.

    Args:
        image_path (str): Path to the input image file.
        hex_color_map (dict): Dictionary mapping original hex colors to new hex colors.
                              Example: {"#FF0000": "#00FF00"} changes all red pixels to green.
        output_path (str): Path to save the modified image.
    """
    
    ans = set()
    
    # Load the image and convert it to RGB
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    
    # Get image dimensions
    width, height = img.size
    
    
    
    # Loop through each pixel in the image
    for x in range(width):
        for y in range(height):
            # Convert the current pixel's color to hex
            current_hex_color = rgb_to_hex(pixels[x, y])
            
            ans.add(current_hex_color)
    
    return list(ans)


# Set up the plot
def plot_cols(colors, save_path):
    # Calculate figure height based on number of colors
    fig_height = max(5, 0.8 * len(colors))  # Ensure minimum size for readability
    fig, ax = plt.subplots(figsize=(8, fig_height))
    ax.axis('off')  # Hide axes

    # Plot each color in the grid with its hex code
    for i, color in enumerate(colors):
        y_pos = -i  # Stack colors vertically
        ax.add_patch(plt.Rectangle((0, y_pos), 0.3, 0.8, color=color))  # Color square
        ax.text(0.35, y_pos + 0.3, color, fontsize=12, verticalalignment='center')  # Hex code label

    # Adjust limits based on number of colors
    ax.set_xlim(0, 1)
    ax.set_ylim(-len(colors), 1)
    plt.savefig(save_path)
    
import matplotlib.colors as mcolors

def lighten_color(hex_color, factor=0.4):
    """
    Lightens a hex color by blending it with white.
    The factor should be between 0 and 1, where higher values produce lighter colors.
    """
    # Convert hex to RGB
    rgb = mcolors.hex2color(hex_color)
    
    # Lighten each component by blending with white
    lighter_rgb = [(1 - (1 - comp) * (1 - factor)) for comp in rgb]
    
    # Convert back to hex
    return mcolors.to_hex(lighter_rgb)

def convert_image_px(input_path, output_path, hex_color_map):
    """
    Change specific colors in an image based on a provided hex color map.

    Args:
        image_path (str): Path to the input image file.
        hex_color_map (dict): Dictionary mapping original hex colors to new hex colors.
                              Example: {"#FF0000": "#00FF00"} changes all red pixels to green.
        output_path (str): Path to save the modified image.
    """
    # Load the image and convert it to RGB
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()
    
    # Get image dimensions
    width, height = img.size
    bar = tqdm(total=width*height)
    # Loop through each pixel in the image
    for x in range(width):
        for y in range(height):
            # Convert the current pixel's color to hex
            current_hex_color = rgb_to_hex(pixels[x, y])
            bar.update(1)
            # If the current pixel's color is in hex_color_map, replace it
            if current_hex_color in hex_color_map:
                #print(f"Replacing color {current_hex_color} with {hex_color_map[current_hex_color]}")
                # Convert the replacement color back to RGB
                new_rgb_color = hex_to_rgb(hex_color_map[current_hex_color])
                pixels[x, y] = new_rgb_color
    
    # Save the modified image
    img.save(output_path)
    print(f"Modified image saved as {output_path}")

if __name__ == "__main__":
    
    image_path, output_path = sys.argv[1], sys.argv[2]
    
    # get factor from args given with --factor
    factor = 0.4  # Default factor value
    for arg in sys.argv:
        if arg.startswith("--factor="):
            factor = float(arg.split("=")[1])
    
    colors = colors_in_img(image_path)
    lighten_colors = list(map(lambda x: lighten_color(x, factor), colors))
    #colors = list(map(lighten_color, colors))
    #plot_cols(colors, "color_palette Thales logo.png")
    
    hex_map = dict(zip(colors, lighten_colors))
    convert_image_px(image_path, output_path, hex_map)