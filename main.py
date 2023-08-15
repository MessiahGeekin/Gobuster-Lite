import os
import requests

list_wordlist = []

def validate_wordlist_path(path):
    if os.path.exists(path) and os.path.isfile(path) and path.endswith(".txt"):
        return True
    else:
        return False


def reading_wordlist(wordlist_path):
    encodings = ["utf-8", "latin-1", "cp1252"]
    for encoding in encodings:
        try:
            with open(wordlist_path, "r", encoding=encoding) as file:
                for words in file:
                    list_wordlist.append(words.strip())
            return list_wordlist
        except UnicodeDecodeError:
            print(f"Cannot decode using {encoding}")


def validate_target_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            print(f"Error: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False


def target_url(url, wordlist):
    for word in wordlist:
        full_url = f"{url}/{word}"
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"Found: {full_url}")

def main():
    wordlist_path = input("Enter wordlist path: ")
    if not validate_wordlist_path(wordlist_path):
        print("Invalid wordlist path.")
        return

    list_wordlist = reading_wordlist(wordlist_path)

    target_url_str = input("Enter target URL: ")
    if not validate_target_url(target_url_str):
        print("Invalid target URL.")
        return

    target_url(target_url_str, list_wordlist)

if __name__ == "__main__":
    main()
