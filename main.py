from psd_tools import PSDImage
import os

def extract_psd_info(psd_file_name):
    psd_file_path = os.path.join(os.path.dirname(__file__), psd_file_name)
    psd = PSDImage.open(psd_file_path)

    # Print the layers present in the PSD file
    print("Layers:")
    for layer in psd.descendants():
        print(layer.name)

        # Display the dimensions of each layer
        print(f"  Dimensions: {layer.width}x{layer.height}")

        # Extract and print any text content present in the PSD file
        if hasattr(layer, 'text_data') and layer.text_data is not None:
            print(f"  Text Content: {layer.text_data.text}")

if __name__ == "__main__":
    psd_file_name = 'vector-shapes.psd'  
    extract_psd_info(psd_file_name)
