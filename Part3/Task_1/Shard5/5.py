def load_config(filename):
    try:
        module_name = 'config_module'
        with open(filename, 'r') as file:
            script = file.read()
            compiled_script = compile(script, filename, 'exec')
            module = type(module_name, (object,), {})()
            exec(compiled_script, module.__dict__)
        return module
    except Exception as e:
        print(f"Ошибка загрузки конфигурации: {e}")
        return None
    
load_config("S:\Education\Питон 4 сем\pract from GitHub\Part3\Task_1\Shard5\config.txt")