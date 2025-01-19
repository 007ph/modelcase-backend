from datetime import datetime
import sys

current_date = datetime.now().strftime("%Y%m%d")

# 输入版本号
# print(version_num)
version_string = sys.argv[1:][0]

# 如果以refs/tags/ 开头，则去掉
if version_string.startswith("refs/tags/"):
    version_string = version_string[10:]

version_num = version_string[1:].split(".") + [current_date]

versionNum = (
    version_num[0] + "," + version_num[1] + "," + version_num[2] + "," + version_num[3]
)
versionString = version_num[0] + "." + version_num[1] + "." + version_num[2]

# 替换后的内容模板
vs_version_template = f"""
# UTF-8
#
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=({versionNum}),
    prodvers=({versionNum}),
    mask=0x17,
    flags=0x0,
    OS=0x4,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        '040904b0',
        [StringStruct('CompanyName', 'HEU LLC'),
        StringStruct('FileDescription', '形式化建模软件后端服务'),
        StringStruct('FileVersion', '{versionString}'),
        StringStruct('LegalCopyright', 'Copyright 2025 HEU. All rights reserved.'),
        StringStruct('OriginalFilename', 'modelcase_backend.exe'),
        StringStruct('ProductName', 'modelcase_backend'),
        StringStruct('ProductVersion', '{versionString}'),
        StringStruct('CompanyShortName', 'HEU'),
        StringStruct('ProductShortName', '形式化建模软件后端服务'),
        StringStruct('Official Build', '1')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [2052, 1200])])
  ]
)
"""

# 格式化版本号并替换模板中的占位符
vs_version_content = vs_version_template.replace(
    "versionNum",
    f"({version_num[0]}, {version_num[1]}, {version_num[2]}, {version_num[3]})",
)
vs_version_content = vs_version_content.replace("versionString", version_string)

# 保存到文件
with open("version.txt", "w", encoding="utf-8") as file:
    file.write(vs_version_content)

print("upodate version success")
