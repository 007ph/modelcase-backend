def parse_args(args):
    args = args[1:]  # 获取命令行参数（不包含脚本名）
    kwargs = {}
    for arg in args:
        # 解析命令行参数,必须以是--开头
        if "=" in arg and arg.startswith("--"):
            key, value = arg.split("=", 1)
            if value.isdigit():  # 如果是数字，转换为 int
                value = int(value)  # type: ignore
            kwargs[key.lstrip("--")] = value
        else:
            raise TypeError(f"Invalid argument: {arg}")
    return kwargs
