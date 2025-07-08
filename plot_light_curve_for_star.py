import lightkurve as lk
import matplotlib.pyplot as plt
import argparse

def fetch_and_plot_full_light_curve(kepler_id, target_name):
    """
    Searches for all available Kepler light curves for a given KIC ID,
    downloads and stitches them, and then plots the resulting data.
    """
    print(f"Searching for all available light curves for {target_name} (KIC {kepler_id})...")
    
    # Search for all light curve files using the Kepler ID
    search_result = lk.search_lightcurve(f'KIC {kepler_id}', author='Kepler')
    
    if not search_result:
        print(f"No data found for KIC {kepler_id}.")
        return

    print(f"Found {len(search_result)} data products. Downloading all...")
    # Download all found light curve files and stitch them into a single light curve
    lc = search_result.download_all().stitch()

    print("Processing and cleaning the full dataset...")
    # Remove NaNs and outliers. A large sigma is used to be gentle with real astrophysical signals.
    lc = lc.remove_nans().remove_outliers(sigma=20)

    # Create the plot
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(15, 5))
    
    ax.plot(lc.time.value, lc.flux.value, '.', markersize=1, color='darkslateblue', alpha=0.5)
    
    ax.set_title(f'Full Kepler Light Curve for {target_name} (KIC {kepler_id})', fontsize=16)
    ax.set_xlabel(f'Time - {lc.time.format.upper()}', fontsize=12)
    ax.set_ylabel('Normalized Flux', fontsize=12)
    ax.grid(True)
    
    # Generate a clean filename
    clean_name = "".join(x for x in target_name if x.isalnum())
    output_filename = f'light_curve_{clean_name}_{kepler_id}.png'
    plt.savefig(output_filename)
    
    print(f"\nPlot successfully saved to: {output_filename}")


if __name__ == "__main__":
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="Download and plot the full Kepler light curve for a given star.")
    parser.add_argument("kic", type=int, help="The Kepler ID (KIC) of the target star.")
    parser.add_argument("name", type=str, help="The common name of the star (e.g., 'Kepler-452'). Use quotes if the name contains spaces.")
    
    args = parser.parse_args()
    
    # Call the main function with the provided arguments
    fetch_and_plot_full_light_curve(args.kic, args.name)
