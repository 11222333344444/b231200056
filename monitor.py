
---

## 2) **monitor.py**

```python
import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        event_type = event.event_type  # created, deleted, modified, moved
        is_directory = event.is_directory
        filepath = event.src_path

        # Değişiklik bilgilerini JSON formatında oluştur
        change_data = {
            "event_type": event_type,
            "is_directory": is_directory,
            "filepath": filepath,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        # JSON verisini dosyaya yaz
        with open("/home/yakup/bsm/logs/changes.json", "a") as f:
            json.dump(change_data, f)
            f.write("\n")

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path="/home/yakup/bsm/test", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
