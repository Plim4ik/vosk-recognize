from datetime import datetime
import transcribe
import file_manager
import os

def main():
    start_time = datetime.now()
    print(f"Начало работы: {start_time}")

    # Создание папки для скачивания файлов, если она не существует
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    links = file_manager.read_links()
    for link in links:
        filename = file_manager.download_and_convert_audio(link)
        transcribe_time, text = transcribe.transcribe_audio(filename)
        file_manager.write_result(link, transcribe_time, text)

    end_time = datetime.now()
    print(f"Конец работы: {end_time}")

if __name__ == "__main__":
    main()
