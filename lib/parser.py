#!/usr/bin/env python3
import zipfile
import json


def get_app_name(zip_file_list):
    """Return app name

    :param zip_file_list: All file included in the IPA file
    """
    for element in zip_file_list:
        if element.count("/") == 2:
            if "Info.plist" in element:
                element = element.replace("Payload/", "").replace("/Info.plist", "")

                return element


def parse_ipa(ipa_path):
    """Parse IOS to identify the Framework used

    :param ipa_path: Full path to the IPA
    """

    result = {}
    parser = open("settings.json", "r").read()
    fram_dict = json.loads(parser)

    zipf = zipfile.ZipFile(ipa_path)
    zip_file_list = zipf.namelist()

    for frame_info in fram_dict:
        file, framework = frame_info["file"], frame_info["framework"]
        file = "Payload/%s/%s" % (get_app_name(zip_file_list), file)

        if file in zip_file_list:
            if framework in result:
                current = result[framework]
                result[framework] = current + 1

            else:
                result[framework] = 1

    return result


def get_result(ipa_path):
    """Get best result

    :param ipa_path: Full path to the IPA
    """
    ipa_parsed = parse_ipa(ipa_path)

    if ipa_parsed:
        new_d = dict(sorted(ipa_parsed.items(), key=lambda t: t[0], reverse=True))
        print("[!] %s seems to be the best answer" % next(iter(new_d)))

    else:
        print("[!] No framework detected")
