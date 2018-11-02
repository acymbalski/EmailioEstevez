import smtplib
import json

class Emailio():

    to_addresses = []
    from_address = "default@nobody.com"
    from_password = ""
    
    host_url = "smtp.gmail.com"
    host_port = 587
    
    header = ""
    message = ""

    def __init__(self, cfg_filename=""):
        if self.load_config(cfg_filename):
            smtp_status = self.start_smtp()
        else:
            print("No configuration file provided.")
        
    def load_config(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.from_address = data["gmail_username"]
            self.from_password = data["gmail_password"]
            return True
        except:
            return False
    
    def add_address(self, new_address):
        self.to_addresses.append(new_address)
    
    def start_smtp(self):
        try:
            self.smtp_server = smtplib.SMTP(self.host_url, self.host_port)
            self.smtp_server.ehlo()
            self.smtp_server.starttls()
            self.smtp_server.ehlo
            self.smtp_server.login(self.from_address, self.from_password)
        except:
            print("Error establishing connection.")
            return False
        return True
        
    def set_subject(self, subject):
        # sent to multiple addresses? we're working with a list, so...
        self.header = 'To:' + ','.join(self.to_addresses) + '\n' + 'From: ' + self.from_address + '\n' + 'Subject:{}'.format(subject) + ' \n'
        
    def set_message(self, msg):
        self.message = msg
        
    def set_message_with_template(self, template_filename, data):
        message_str = ""
        with open(template_filename, 'r') as f:
            for line in f.readlines():
                try:
                    message_str += line.format(*data)
                except IndexError:
                    print("Invalid number of data points supplied to the template. Ignoring this line's formatting...")
                    message_str += line
                
        self.message = message_str
        
    def send(self):
        try:
            self.smtp_server.sendmail(self.from_address, self.to_addresses, self.header + self.message)
        except:
            print("Error sending message.")
            
    def close(self):
        self.smtp_server.close()
