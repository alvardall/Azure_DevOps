import os
import testData.data as data
import logging

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, data.fileName)


def write_to_file(text, mode='a'):
    try:
        with open(file_path, mode, encoding='utf-8') as file:
            file.write(text + "\n")
        logging.info(f"Message written to {file_path}: {text}")
    except Exception as e:
        logging.error(f"Failed to write to file {file_path}: {e}")


def cleanup():
    try:
        answer = input("\nDo you want to delete 'live_coding_text.txt' and 'execut.log'? (y/n): ").strip().lower()
        if answer == "y":
            if os.path.exists(file_path):
                os.remove(file_path)
                print("File 'live_coding_text.txt' deleted successfully.")
                logging.info("File 'live_coding_text.txt' deleted successfully.")
            else:
                print("File 'live_coding_text.txt' not found.")
                logging.warning("File 'live_coding_text.txt' not found during cleanup.")
            
            logging.shutdown()

            log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "execut.log")
            if os.path.exists(log_path):
                os.remove(log_path)
                print("File 'execut.log' deleted successfully.")
            else:
                print("File 'execut.log' not found.")
        else:
            print("Files not deleted.")
            logging.info("File deletion canceled by user.")
    except Exception as e:
        print(f"An error occurred during cleanup: {e}")
        logging.error(f"An error occurred during cleanup: {e}")