import yaml


# flutter_launcher_icons:
#   android: "launcher_icon"
#   image_path: "assets/migu.jpg"
#   min_sdk_android: 21 # android min sdk min:16, default 21

default_icons_spec = {
    'flutter_launcher_icons': {
        'android': 'launcher_icon',
        'image_path': 'assets/migu.jpg',
        'min_sdk_android': 21
    }
}


# change the value of image_path in flutter_launcher_icons.yaml
def change_icon_img_path(img_path):
    # pubspec = None

    # with open('flutter_launcher_icons.yaml', 'r', encoding='utf-8') as f:
        # pubspec = yaml.load(f)
    # if not pubspec:
    pubspec = default_icons_spec
    if pubspec.get('flutter_launcher_icons'):
        pubspec['flutter_launcher_icons']['image_path'] = img_path
    else:
        pubspec = default_icons_spec
        pubspec['flutter_launcher_icons']['image_path'] = img_path

    with open('flutter_launcher_icons.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(pubspec, f)
        f.flush()
        
    
    import time
    time.sleep(1)


# package_rename_config:
#   android:
#     app_name: # (String) The display name of the android app
#     package_name: # (String) The package name of the android app
#     override_old_package: # (Optional) (String) Use this to delete the old folder structure of MainActivity or to use the existing code with the new package name
#     lang: # (Optional) (String) The android development language {kotlin(default) or java}


def change_name(name,package_name):
    # package_rename_config.yaml
    default_package_rename_config = {
        'package_rename_config': {
            'android': {
                'app_name': name,
                'package_name': package_name
                }
            }
        }
    package_rename_config = default_package_rename_config
    with open('package_rename_config.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(package_rename_config, f)
        f.flush()
    import time
    time.sleep(1)
        