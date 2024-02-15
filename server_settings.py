import os
import yaml
class serversettings:
    
    def __init__(self, prefix=None, serverid=None, watched=None):
        self.prefix = prefix
        self.serverid = serverid
        self.watched = []
        self.base_path = f"servers/{self.serverid}/config.yml"
    def prefix(self):
        if not os.path.exists(self.base_path):
            return '!'
        else:
            with open(self.base_path, 'r') as file:
                data = yaml.safe_load(file)
            prefix = data['prefix']
            return prefix
    def watched_list(self):
        if not os.path.exists(self.base_path):
            return None
        elif os.path.exists(self.base_path):
            with open(self.base_path, 'r') as file:
                data = yaml.safe_load(file)
            watched = data.get('watched', [])
            return watched
    def watch_list_add(self, item):
        if not os.path.exists(self.base_path):
            if not os.path.exists(f"servers/{self.serverid}")
                os.makedirs(f"servers/{self.sererid}")
                with open(self.base_path, 'w') as file:
                data = {'prefix': self.prefix, 'watched': [item]}