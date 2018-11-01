# Emailio Estevez
Simple email sender class for Python, currently only good for sending from gmail accounts.

## Setup
Create an account configuration .json file that follows the included example.
At the moment there's no password obfuscation so be wary of that.

## Sample Usage
```
from emailer import Emailer

e = Emailer("email_cfg.json")
e.add_address("sample_target@domain.com")
e.set_header("Subject")
e.set_message("This is the plaintext message.")
e.send()
e.close()
```
