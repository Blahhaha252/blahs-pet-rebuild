import os
import yaml
class nullVar(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)
class serversettings:
    
    def __init__(self, serverid=None, watched=None):
        self.serverid = serverid
        self.watched = []
        self.base_path = f"servers/{self.serverid}/config.yml"
    def prefix(self):
        if not os.path.exists(self.base_path):
            with open("config.yml", 'r') as file:
                data = yaml.safe_load(file)
            serverprefix = data['bot']['prefix']
            return serverprefix
        else:
            with open(self.base_path, 'r') as file:
                data = yaml.safe_load(file)
            serverprefix = data['prefix']
            return serverprefix
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
            if not os.path.exists(f"servers/{self.serverid}"):
                os.makedirs(f"servers/{self.serverid}")
                data = {'prefix': self.prefix(), 'watched': [item]}
                with open(self.base_path, 'w') as file:
                    yaml.safe_dump(data, file, sort_keys=False)
            else:
                data = {'prefix': self.prefix(), 'watched': [item]}
                with open(self.base_path(), 'w') as file:
                    yaml.safe_dump(data, file, sort_keys=False)
        else:
            with open(self.base_path, 'r') as file:
                data = yaml.safe_load(file)
            if 'watched' not in data:
                data['watched'] = []
            else:
                data['watched'].append(item)
            with open(self.base_path, 'w') as file:
                yaml.safe_dump(data, file, sort_keys=False)
    def watch_list_remove(self, item):
        if not os.path.exists(self.base_path):
            raise nullVar(f"{item} does not exist or the server file hasnt been created")
        else:
            with open(self.base_path, 'r') as file:
                data = yaml.safe_load(file)
            if 'watched' in data:
                if item in data['watched']:
                    data['watched'].remove(item)
                    with open(self.base_path, 'w') as file:
                        yaml.safe_dump(data, file, sort_keys=False)
                else:
                    raise nullVar(f"{item} does not exist or the server file hasnt been created")
            else:
                raise nullVar(f"{item} does not exist or the server file hasnt been created")