import os
import webbrowser

def open_app(app_name):
    if "notepad" in app_name:
        os.system("notepad")
    elif "chrome" in app_name:
        os.system("start chrome")
    elif "discord" in app_name:
        os.system("discord")
    elif "youtube" in app_name:
        webbrowser.open("https://www.youtube.com/")
    elif "facebook" in app_name:
        webbrowser.open("https://www.facebook.com/")
    elif "instagram" in app_name:
        webbrowser.open("https://www.instagram.com/")
    elif "gmail" in app_name:
        webbrowser.open("https://mail.google.com/")
    elif "portfolio" in app_name:
        webbrowser.open("https://www.aadityaprasadbhatt.com.np")
    elif "github" in app_name:
        webbrowser.open("https://github.com/ADart12")
    elif "linkedin" in app_name:
        webbrowser.open("https://www.linkedin.com/in/adart976/")
    elif "twitter" in app_name:
        webbrowser.open("https://x.com/Aaditya_Bhatt51")
    else:
        return False
    return True


def open_file(file_path):
    try:
        os.startfile(file_path)
        return True
    except Exception as e:
        print("Error opening file: {e}")
        return False
def open_folder(folder_path):
    try:
        os.startfile(folder_path)
        return True
    except Exception as e:
        print("Error opening folder: {e}")
        return False

def webSearch(translQuery):
    try:
        webbrowser.open(f"https://www.google.com/search?q={translQuery}")
        return True
    except Exception as e:
        print(f"Error performing web search: {e}")
        return False

def execute(translQuery):
    if "open" in translQuery:
        # Check if the query contains any of the specified app names
        if any(app in translQuery for app in (
        "notepad", "chrome", "discord", "youtube", "facebook", "instagram", "twitter", "gmail", "portfolio", "github",
        "linkedin")):
            return open_app(translQuery)
        # Check if the query contains the word "file"
        elif "file" in translQuery:
            # Extract the file path from the query
            file_path = translQuery.split("file")[-1].strip()
            return open_file(file_path)
        # Check if the query contains the word "folder"
        elif "folder" in translQuery:
            # Extract the folder path from the query
            folder_path = translQuery.split("folder")[-1].strip()
            return open_folder(folder_path)
    elif "search" in translQuery:
        search_query = translQuery.split("search")[-1].strip()
        return webSearch(search_query)
    return False
