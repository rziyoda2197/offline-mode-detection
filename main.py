import requests

class OfflineModeDetector:
    def __init__(self, timeout=5):
        self.timeout = timeout

    def is_offline(self):
        try:
            requests.head('https://www.google.com', timeout=self.timeout)
            return False
        except requests.ConnectionError:
            return True

def main():
    detector = OfflineModeDetector()
    if detector.is_offline():
        print("Offline mode detected")
    else:
        print("Online mode detected")

if __name__ == "__main__":
    main()
```

```python
import socket

class OfflineModeDetector:
    def __init__(self, timeout=5):
        self.timeout = timeout

    def is_offline(self):
        try:
            socket.create_connection(('www.google.com', 80), timeout=self.timeout)
            return False
        except OSError:
            return True

def main():
    detector = OfflineModeDetector()
    if detector.is_offline():
        print("Offline mode detected")
    else:
        print("Online mode detected")

if __name__ == "__main__":
    main()
```

```python
import requests

class OfflineModeDetector:
    def __init__(self, timeout=5):
        self.timeout = timeout

    def is_offline(self):
        try:
            requests.get('https://www.google.com', timeout=self.timeout)
            return False
        except requests.ConnectionError:
            return True

def main():
    detector = OfflineModeDetector()
    if detector.is_offline():
        print("Offline mode detected")
    else:
        print("Online mode detected")

if __name__ == "__main__":
    main()
