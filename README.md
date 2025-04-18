# Simple Client-Server Text Processor


### Creator: Ali Mohamed

---

## Overview

This project is a basic Client-Server application built using Python's `socket` library.  
It allows a client to send a message to the server, and depending on the command prefix, the server processes the text and sends back a response.

---

## Features

- Sort text in **ascending** or **descending** order.
- Convert text to **uppercase**.
- **Echo** the original text if no valid command is given.
- Simple and easy to use over a local network.

---

## Supported Commands

| Command | Description                       |
|:--------|:----------------------------------|
| A       | Sorts the text in descending order |
| C       | Sorts the text in ascending order  |
| D       | Converts the text to uppercase     |
| Other   | Echoes back the original message   |

---

## Files Included

- `client.py` — Connects to the server, sends user input, and displays responses.
- `server.py` — Listens for client connections, processes commands, and sends back results.

---

## Requirements

- Python 3.x

> No external libraries are required; everything runs using the Python standard library.

---

## How to Run

1. Open a terminal and **start the server**:
    ```
    python server.py
    ```

2. Open another terminal and **start the client**:
    ```
    python client.py
    ```

3. **Send a message** starting with a command character (like `Ahello` or `Dworld`).

4. **To exit**, just press Enter without typing a message in the client terminal.

---

## Example

**Client input:**
```
Cpython
```

**Server response:**
```
hnopty
```

---

## License

This project is licensed under the MIT License — see the LICENSE file for details.

---
