from datetime import datetime


def generate_log(data):
    """
    Creates a timestamped log file and writes each entry from the data list.
    """

    # Validate input
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    # Generate filename
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write log entries to file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Print confirmation message
    print(f"Log written to {filename}")

    return filename