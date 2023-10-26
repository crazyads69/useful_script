def convert_hex_to_format(input_hex):
    # Split the input hex string into a list of bytes
    hex_values = input_hex.split()
    # Initialize variables
    result = ""  # The result string
    current_byte = ""  # The current byte being processed
    start_index = 1
    end_index = 1
    # Loop through the list of bytes and process each byte
    i = 0
    while i < len(hex_values):
        # Get the current hex value
        hex_value = hex_values[i]
        # Check if the hex value is valid (2 characters)
        if len(hex_value) != 2:
            i += 1
            continue  # Skip invalid hex values

        char = chr(
            int(hex_value, 16)
        )  # Convert the current byte hex to ASCII character
        if start_index == end_index:
            # Handle the case when the byte's start index is equal to the end index
            if char.isalnum() or char.isspace():
                # If it's alphanumeric or a space, update the current byte and end index
                current_byte = hex_value + " "
                end_index += 1
            else:
                # If it's a special character, print it and update both indices
                result += f"Byte {end_index}: {hex_value} = {char}\n"
                start_index = end_index = end_index + 1
            i += 1
        elif char == " ":
            # Handle spaces
            if current_byte:
                # Print the previous character in the required format
                byte_string = " ".join(current_byte.strip().split())
                try:
                    byte_ascii = bytes.fromhex(byte_string.replace(" ", "")).decode(
                        "utf-8", errors="replace"
                    )
                except UnicodeDecodeError:
                    byte_ascii = "�"  # Replace non-decodable bytes with �
                result += f"Byte {start_index} đến {end_index-1}: {byte_string} = {byte_ascii}\n"
            # Print the space character
            result += f"Byte {end_index}: {hex_value} = dấu cách [space]\n"
            # Update the start and end index
            start_index = end_index = end_index + 1
            i += 1
            current_byte = ""
        elif char.isalnum():
            # If the character is alphanumeric, add it to the current byte and update the end index
            current_byte += hex_value + " "
            end_index += 1
            i += 1
        elif (
            hex_value == "0d" and i + 1 < len(hex_values) and hex_values[i + 1] == "0a"
        ):
            # Handle line breaks (CR LF)
            if current_byte:
                byte_string = " ".join(current_byte.strip().split())
                try:
                    byte_ascii = bytes.fromhex(byte_string.replace(" ", "")).decode(
                        "utf-8", errors="replace"
                    )
                except UnicodeDecodeError:
                    byte_ascii = "�"  # Replace non-decodable bytes with �
                result += f"Byte {start_index} đến {end_index-1}: {byte_string} = {byte_ascii}\n"
            result += f"Byte {end_index} đến {end_index + 1}: 0d 0a = dấu ngắt dòng [CR][LF]\n"
            start_index = end_index = end_index + 2
            i += 2
            current_byte = ""
        else:
            # Handle special characters
            if current_byte:
                byte_string = " ".join(current_byte.strip().split())
                try:
                    byte_ascii = bytes.fromhex(byte_string.replace(" ", "")).decode(
                        "utf-8", errors="replace"
                    )
                except UnicodeDecodeError:
                    byte_ascii = "�"  # Replace non-decodable bytes with �
                result += f"Byte {start_index} đến {end_index-1}: {byte_string} = {byte_ascii}\n"
            result += f"Byte {end_index}: {hex_value} = {char}\n"
            start_index = end_index = end_index + 1
            i += 1
            current_byte = ""
    # Print any remaining character, if any
    if current_byte:
        byte_string = " ".join(current_byte.strip().split())
        try:
            byte_ascii = bytes.fromhex(byte_string.replace(" ", "")).decode(
                "utf-8", errors="replace"
            )
        except UnicodeDecodeError:
            byte_ascii = "�"  # Replace non-decodable bytes with �
        result += (
            f"Byte {start_index} đến {end_index-1}: {byte_string} = {byte_ascii}\n"
        )

    return result


# Input a hex string
input_hex = input("Input a hex string (with spaces): ")
formatted_output = convert_hex_to_format(input_hex)
print(formatted_output)
