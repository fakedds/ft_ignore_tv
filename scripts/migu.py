import subprocess


def main():
    # subprocess.run(['flu', 'migu.py'], cwd='scripts')
    subprocess.run(['dart', 'pub', 'get'], shell=True)
    from util import change_icon_img_path, change_name
    change_icon_img_path('assets/migu.jpg')
    change_name('咪咕快游', 'cn.emagsoftware.gamehall')
    # subprocess.run(cmd, shell=True)
    subprocess.run(['dart', 'pub', 'run', 'flutter_launcher_icons:main'], shell=True)
    #  dart run package_rename
    subprocess.run(['dart', 'run', 'package_rename'], shell=True)
    subprocess.run(['flutter', 'clean'], shell=True)


    subprocess.run(['flutter', 'build', 'apk', '--release'], shell=True)
    cmd = 'mv build/app/outputs/apk/release/app-release.apk build/app/outputs/apk/release/migu_fake.apk'


if __name__ == '__main__':
    main()