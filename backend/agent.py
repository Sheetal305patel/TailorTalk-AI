from backend.drive_tool import search_drive


def generate_drive_query(user_input):
    user_input = user_input.lower()

    # PDF files
    if "pdf" in user_input:
        return "mimeType='application/pdf'"

    # Images
    elif "image" in user_input or "photo" in user_input:
        return "mimeType contains 'image/'"

    # Spreadsheet
    elif "sheet" in user_input or "excel" in user_input:
        return "mimeType contains 'spreadsheet'"

    # Default search
    else:
        words = user_input.split()

        for word in words:
            if len(word) > 3:
                return f"name contains '{word}'"

    return "trashed=false"


def process_query(user_input):

    drive_query = generate_drive_query(user_input)

    print("Generated Query:", drive_query)

    files = search_drive(drive_query)

    if not files:
        return "No matching files found."

    response = ""

    for file in files:

        response += f"📄 {file['name']}\n"
        response += f"🔗 {file['webViewLink']}\n\n"

    return response