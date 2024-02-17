import os
import yaml
class nullVar(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)
class MYamlER(Exception):
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
#yaml master, will be used soon when its finished to help with making the other classes and other uses shorter (needs to be updated to be smaller)
#types chck (check), addp (addpair), addl (add list), rpair (remove pair), rlist (remove list), chng (change, used for booleans mainly)
    def yaml_master(self, type, path, key=None, value1=None, value2=None):
        if not os.path.exists(self.base_path):
            if not os.path.exists(f"servers/{self.serverid}"):
                os.makedirs(f"servers/{self.serverid}")
                # do logic to compare shit
            else:
                pass
        else:
            pass
        def yaml_master_edit(self, type, path, key=None, value1=None, value2=None):
            if type == "chck":
                if key is None:
                    if os.path.exists(path):
                        return True
                    else:
                        return False
                else:
                    if value1 is None and value2 is None:
                        with open(path, 'r') as file:
                            data = yaml.safe_load(file)
                        if key in data:
                            return True
                        else:
                            return False
                    elif value1 is not None and value2 is None:
                        with open(path, 'r') as file:
                            data = yaml.safe_load(file)
                        if key in data:
                            if value1 in data[key]:
                                return True
                            else:
                                return False
                        else:
                            raise MYamlER(f"Cant check value1 because key doesnt exist in file type={type}")
                    elif value1 is not None and value2 is not None:
                        with open(path, 'r') as file:
                            data = yaml.safe_load(file)
                        if key in data:
                            if value1 in data[key]:
                                return True
                                raise MYamlER(f"2 values were provided, using the first one ({value1}) not {value2}, type={type}")
                            else:
                                return False
                                raise MYamlER(f"2 values were provided, using the first one ({value1}) not {value2}, type={type}")
                        else:
                            raise MYamlER(f"Cant check value1 because key doesnt exist in file type={type}")
                            raise MYamlER(f"2 values were provided, using the first one ({value1}) not {value2}, type={type}")
                    elif value1 is None and value2 is not None:
                        raise MYamlER(f"value1 is null, but value2 isnt, value2 is ment for changing not type={type}")
            elif type == "addp":
                if key is None:
                    raise MYamlER(f"key was not provided, and a key is needed type={type}")
                else:
                    if value1 is None and value2 is None:
                        with open(path, 'r') as file:
                            data = yaml.safe_load(file)
                        data[key] = None
                        with open(path, 'w') as file:
                            yaml.safe_dump(data, file, sort_keys=False)
                    elif value1 is not None and value2 is None:
                        with open(path, 'r') as file:
                            data = yaml.safe_load(file)
                        data[key] = value1
                        with open(path, 'w') as file:
                            yaml.safe_dump(data, file, sort_keys=False)
                    elif value1 is not None and value2 is not None:
                        with open(path, 'r') as file:
                            data = yaml.safe_load(file)
                        data[key] = value1
                        with open(path, 'w') as file:
                            yaml.safe_dump(data, file, sort_keys=False)
                        raise MYamlER(f"2 values were provided, using the first one ({value1}) not {value2}, type={type}")
                    elif value1 is None and value2 is not None:
                        raise MYamlER(f"value1 is null, but value2 isnt, value2 is ment for changing not type={type}")
            elif value == "addl":
                if key is None:
                    raise MYamlER(f"key was not provided, and a key is needed type={type}")
                else:
                    if value1 is None and value2 is None:
                        with open(path, 'r') as file:
                            data = yaml.safe_load(file)
                        data[key] = []
                        with open(path, 'w') as file:
                            yaml.safe_dump(data, file, sort_keys=False)
                    elif value1 is not None and value2 is none:
                        with open(path, 'r') as file:
                            data = yaml.safe_load(file)
                        if key in data:
                            data[key].append(value1)
                            with open(path, 'w') as file:
                                yaml.safe_dump(data, file, sort_keys=False)
                        else:
                            raise MYamlER(f"Key doesnt exist! type={type}")
                    elif value1 is not None and value2 is not None:
                        with open(path, 'r') as file:
                            data = yaml.safe_load(file)
                        data[key].append(value1)
                        with open(path, 'w') as file:
                            yaml.safe_dump(data, file, sort_keys=False)
                        raise MYamlER(f"2 values were provided, using the first one ({value1}) not {value2}, type={type}")
                    elif value1 is None and value2 is not None:
                        raise MYamlER(f"value1 is null, but value2 isnt, value2 is ment for changing not type={type}")
            elif type == 'rpair':
                if key is None:
                    raise MYamlER(f"key was not provided, and a key is needed type={type}")
                else:
                    if value1 is None and value2 is None:
                        with open(path, 'r') as file:
                            data = yaml.safe_load(file)
                        if key in data:
                            del data[key]
                            with open(path, 'w') as file:
                                yaml.safe_dump(data, file, sort_keys=False)
                        else:
                            raise MYamlER(f"Key doesnt exist! type={type}")
                        
                    elif value1 is not None and value2 is None:
                        with open(path, 'r') as file:
                            data = yaml.safe_load(file)
                        if key in data:
                            if value1 in data[key]:
                                data[key] = None
                                with open(path, 'w') as file:
                                    yaml.safe_dump(data, file, sort_keys=False)
                            else:
                                raise MYamlER(f"value doesnt exist! type={type}")
                        else:
                            raise MYamlER(f"Key doesnt exist! type={type}")
                    elif value1 is not None and value2 is not None:
                        with open(path, 'r') as file:
                            data = yaml.safe_load(file)
                        if key in data:
                            if value1 in data[key]:
                                data[key] = None
                                with open(path, 'w') as file:
                                    yaml.safe_dump(data, file, sort_keys=False)
                                raise MYamlER(f"2 values were provided, using the first one ({value1}) not {value2}, type={type}")
                            else:
                                raise MYamlER(f"value doesnt exist! type={type}")
                        else:
                            raise MYamlER(f"Key doesnt exist! type={type}")
                    elif value1 is None and value2 is not None:
                        raise MYamlER(f"value1 is null, but value2 isnt, value2 is ment for changing not type={type}")
            elif type == 'rlist':
                if key is None:
                    raise MYamlER(f"key was not provided, and a key is needed type={type}")
                else:
                    if value1 is None and value2 is None:
                        with open(path, 'r') as file:
                            data = yaml.safe_load(file)
                        if key in data:
                            del data[key]
                            with open(path, 'w') as file:
                                yaml.safe_dump(data, file, sort_keys=False)
                        else:
                            raise MYamlER(f"Key doesnt exist! type={type}")
                    elif value1 is not None and value2 is None:
                        with open(path, 'r') as file:
                            data = yaml.safe_load(file)
                        if key in data:
                            if value1 in data[key]:
                                data[key].remove(value1)
                                with open(path, 'w') as file:
                                    yaml.safe_dump(data, file, sort_keys=False)
                            else:
                                raise MYamlER(f"value doesnt exist! type={type}")
                        else:
                            raise MYamlER(f"Key doesnt exist! type={type}")
                    elif value1 is not None and value2 is not None:
                        pass
                    elif value1 is None and value2 is not None:
                        raise MYamlER(f"value1 is null, but value2 isnt, value2 is ment for changing not type={type}")
            elif type == 'chng':
                if key is None:
                    raise MYamlER(f"key was not provided, and a key is needed type={type}")
                else:
                    if value1 is None and value2 is None:
                        pass
                    elif value1 is not None and value2 is None:
                        pass
                    elif value1 is not None and value2 is not None:
                        pass
            else:
                raise MYamlER(f"No type was provided, please provide a type")