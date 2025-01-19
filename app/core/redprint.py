import pkgutil
import importlib
import sys
from flask import Flask, Blueprint

def register_redprints(app: Flask):
    """
    自动扫描 app.routes 包及其子包，加载并注册所有 Blueprint。
    子包中的路由会自动添加子包名称作为前缀。

    Args:
        app (Flask): Flask 应用实例。
    """
    package = app.config.get("BLUEPRINT_PATH", "app.routes")  # 默认扫描 app.routes 包

    try:
        # 确保包已经被导入
        if package not in sys.modules:
            importlib.import_module(package)

        package_module = sys.modules[package]
        package_path = package_module.__path__  # 获取包的路径
    except (ImportError, AttributeError) as e:
        raise RuntimeError(f"Failed to load package '{package}': {e}")

    for _, module_name, ispkg in pkgutil.walk_packages(package_path, package + "."):
        # 获取模块或包名称（例如 v1）
        prefix = module_name.split(".")[-1]

        # 如果是子包，创建蓝图并注册其路由
        if ispkg:
            blueprint = Blueprint(prefix, module_name, url_prefix=f"/{prefix}")
            try:
                # 动态导入子包
                subpackage = importlib.import_module(module_name)

                # 扫描子包中的模块
                for _, submodule_name, _ in pkgutil.walk_packages(subpackage.__path__, module_name + "."):
                    try:
                        submodule = importlib.import_module(submodule_name)
                    except ImportError as e:
                        print(f"Error importing submodule {submodule_name}: {e}")
                        continue

                    # 遍历模块中的所有属性，查找路由函数或蓝图
                    for attr_name in dir(submodule):
                        attr = getattr(submodule, attr_name)

                        # 如果是蓝图，直接注册到子包的蓝图
                        if isinstance(attr, Blueprint):
                            blueprint.register_blueprint(attr)

                        # 如果是路由函数，将其注册到当前蓝图
                        elif callable(attr) and hasattr(attr, "__module__") and attr.__module__ == submodule_name:
                            route = f"/{attr_name}"  # 默认路由路径为函数名
                            blueprint.add_url_rule(route, attr_name, attr)
                            print(f"Added route: {prefix}{route}")

                # 注册蓝图到应用
                app.register_blueprint(blueprint)
                print(f"Registered blueprint with prefix '/{prefix}': {module_name}")

            except ImportError as e:
                print(f"Error importing package {module_name}: {e}")

        # 如果是模块，直接检查并注册蓝图
        else:
            try:
                module = importlib.import_module(module_name)
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if isinstance(attr, Blueprint):
                        app.register_blueprint(attr)
                        print(f"Registered blueprint: {attr.name} from {module_name}")
            except ImportError as e:
                print(f"Error importing module {module_name}: {e}")
