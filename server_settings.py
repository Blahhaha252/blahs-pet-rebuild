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
            if 'prefix' in data:
                serverprefix = data['prefix']
            else:
                with open("config.yml", 'r') as file:
                    data = yaml.safe_load(file)
                serverprefix = data['bot']['prefix']
            return serverprefix

    def watched_list(self):
        pass
    def watch_list_add(self, item):
        try:
            self.yaml_master(type='addl', path=self.base_path, key='watched', value1=item)
        except MYamlER as e:
            print(e)

#yaml master, will be used soon when its finished to help with making the other classes and other uses shorter (needs to be updated to be smaller)
#types chck (check), addp (addpair), addl (add list), rpair (remove pair), rlist (remove list), chng (change, used for booleans mainly)
    def yaml_master(self, type, path, key=None, value1=None, value2=None):
        dir, filename = os.path.split(path)
        serverid = dir.split("/")[1]
        if not os.path.exists(dir):
            os.makedirs(dir)

        if key is None:
            raise ValueError("Key cannot be None.")

        if not os.path.exists(path):
            with open(path, 'w') as file:
                file.write(f"serverid: {serverid}")

        self.yaml_master_edit(type, path, key, value1, value2)
    def yaml_master_edit(self, type, path, key=None, value1=None, value2=None):
        if type == "chck":
            if key is None:
                return os.path.exists(path)
            else:
                with open(path, 'r') as file:
                    data = yaml.safe_load(file)
                if key in data:
                    if value1 is None and value2 is None:
                        return True
                    elif value1 is not None and value2 is None:
                        return value1 in data[key]
                    elif value1 is not None and value2 is not None:
                        return value1 in data[key]
                        raise MYamlER(f"2 values were provided, using the first one ({value1}) not {value2}, type={type}")
                    elif value1 is None and value2 is not None:
                        raise MYamlER(f"value1 is null, but value2 isnt, value2 is ment for changing not type={type}")
                else:
                    return False
                    raise MYamlER(f"Key was not found in data type={type}")
        elif type == "addp":
            if key is None:
                raise MYamlER(f"key was not provided, and a key is needed type={type}")
            else:
                with open(path, 'r') as file:
                    data = yaml.safe_load(file)
                if key in data:
                    raise MYamlER(f"Key= {key} Exists in this file!, please use type chng or rpair")
                else:
                    if value1 is None and value2 is None:
                        data[key] = None
                        with open(path, 'w') as file:
                            yaml.safe_dump(data, file, sort_keys=False)
                    elif value1 is not None and value2 is None:
                        data[key] = value1
                        with open(path, 'w') as file:
                            yaml.safe_dump(data, file, sort_keys=False)
                    elif value1 is not None and value2 is not None:
                        data[key] = value1
                        with open(path, 'w') as file:
                            yaml.safe_dump(data, file, sort_keys=False)
                        raise MYamlER(f"2 values were provided, using the first one ({value1}) not {value2}, type={type}")
                    elif value1 is None and value2 is not None:
                        raise MYamlER(f"value1 is null, but value2 isnt, value2 is ment for changing not type={type}")
        elif type == "addl":
            if key is None:
                raise MYamlER(f"key was not provided, and a key is needed type={type}")
            else:
                with open(path, 'r') as file:
                    data = yaml.safe_load(file)
                if key in data:
                    if (value1 is None and value2 is None) or (value1 is None and value2 is not None):
                        raise MYamlER(f"Cant add 2 of the same list keys!, or value1 is null and value 2 is not null, info:{type, value1, value2}")
                    elif (value1 is not None and value2 is None) or (value1 is not None and value2 is not None):
                        if value1 in data[key]:
                            raise MYamlER(f"List item already exists in list type={type}")
                        data[key].append(value1)
                        with open(path, 'w') as file:
                            yaml.safe_dump(data, file, sort_keys=False)
                        if value2 is not None:
                            raise MYamlER(f"value1 is null, but value2 isnt, value2 is ment for changing not type={type}")
                else:
                    if (value1 is None and value2 is None) or (value1 is None and value2 is not None):
                        if value2 is not None:
                            raise MYamlER(f"value1 is null, but value2 isnt, value2 is ment for changing not type={type}")
                        data[key] = []
                        with open(path, 'w') as file:
                            yaml.safe_dump(data, file, sort_keys=False)
                    elif (value1 is not None and value2 is None) or (value1 is not None and value2 is not None):
                        data[key] = [value1]
                        with open(path, 'w') as file:
                            yaml.safe_dump(data, file, sort_keys=False)
                        if value2 is not None:
                            raise MYamlER(f"2 values were provided, using the first one ({value1}) not {value2}, type={type}")
        elif type == 'rpair':
            if key is None:
                raise MYamlER(f"key was not provided, and a key is needed type={type}")
            else:
                with open(path, 'r') as file:
                    data = yaml.safe_load(file)
                if key not in data:
                    raise MYamlER(f"Key was not found!, key={key}, type={type}")
                else:
                    if value1 is None:
                        if value2 is not None:
                            raise MYamlER(f"value1 is null, but value2 isnt, value2 is ment for changing not type={type}")
                        else:
                            del data[key]
                            with open(path, 'w') as file:
                                yaml.safe_dump(data, file, sort_keys=False)
                    elif value1 is not None:
                        if value1 in data[key]:
                            data[key] = None
                            with open(path, 'w') as file:
                                yaml.safe_dump(data, file, sort_keys=False)
                        else:
                            raise MYamlER(f"{value1} is not in {key} type={type}")
                        if value2 is not None:
                            raise MYamlER(f"2 values were provided, using the first one ({value1}) not {value2}, type={type}") 
        elif type == 'rlist':
            if key is None:
                raise MYamlER(f"key was not provided, and a key is needed type={type}")
            else:
                with open(path, 'r') as file:
                    data = yaml.safe_load(file)
                if key not in data:
                    raise MYamlER(f"key was not provided, and a key is needed type={type}")
                else:
                    if value1 is None:
                        if value2 is not None:
                            raise MYamlER(f"value1 is null, but value2 isnt, value2 is ment for changing not type={type}")
                        else:
                            del data[key]
                            with open(path, 'w') as file:
                                yaml.safe_dump(data, file, sort_keys=False)
                    elif value1 is not None:
                        if value1 not in data[key]:
                            raise MYamlER(f"Key was not found!, key={key}, type={type}")
                        else:
                            data[key].remove(value1)
                            with open(path, 'w') as file:
                                yaml.safe_dump(data, file, sort_keys=False)
                            if value2 is not None:
                                raise MYamlER(f"2 values were provided, using the first one ({value1}) not {value2}, type={type}")
        elif type == 'chng':
            if key is None:
                raise MYamlER(f"key was not provided, and a key is needed type={type}")
            else:
                with open(path, 'r') as file:
                    data = yaml.safe_load(file)   
                if value1 is None and value2 is None:
                    if key in data:
                        if isinstance(data[key], bool):
                            data[key] = not data[key]
                            with open(path, 'w') as file:
                                yaml.safe_dump(data, file, sort_keys=False)
                        else:
                            raise MYamlER(f"Cant switch key sense it doesnt have a boolean value! type={type}")
                elif value1 is not None and value2 is None:
                    raise MYamlER(f"Cant swap 2 values if only 1 is provided type={type}")
                elif value1 is not None and value2 is not None:
                    if key in data:
                        if value1 in data[key]:
                            data[key] = value2
                            with open(path, 'w') as file:
                                yaml.safe_dump(data, file, sort_keys=False)
                        else:
                            raise MYamlER(f"value1 was not found in key, value1 = {value1}, type={type}")
                elif value1 is None and value2 is not None:
                    raise MYamlER(f"Cant swap out value1 with value2 if value1 is None! type={type}")
        else:
            raise MYamlER(f"No type was provided, please provide a type")