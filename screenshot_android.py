#!/usr/bin/env python

import argparse
import subprocess
from time import sleep

# http://developer.android.com/intl/ru/tools/devices/managing-avds-cmdline.html
# yep, set up an AVD and run it via command line.

screenshot_cmd = 'adb shell screencap -p | perl -pe \'s/\\x0D\\x0A/\\x0A/g\''
open_cmd = ('adb shell am start -a android.intent.action.VIEW -c '
            'android.intent.category.DEFAULT -d {domain} -n {browser}')
kill_cmd = 'adb shell am force-stop {browser}'


def run(browser):
    '''
    For each domain in urls.txt, open it in the browser and take a screenshot,
    saving it as num.txt. That will allow for easy programmatic embedding in
    something like a spreadsheet (hopefully).
    '''
    browser_dict_start = {
        # found this chrome dev apk here:
        # http://www.apkmirror.com/apk/google-inc/chrome-dev/chrome-dev-51-0-2700-2-release/chrome-dev-51-0-2700-2-3-android-apk-download/
        'chrome-dev': 'com.chrome.dev/com.google.android.apps.chrome.Main',
        'chrome': 'com.android.chrome/com.google.android.apps.chrome.Main',
        'fennec': 'org.mozilla.fennec/.App',
        'firefox': 'org.mozilla.firefox/.App',
        'UCMobile': 'com.UCMobile.intl/com.UCMobile.main.UCMobile'
    }

    browser_dict_stop = {
        'chrome-dev': 'com.chrome.dev',
        'chrome': 'com.android.chrome',
        'fennec': 'org.mozilla.fennec',
        'firefox': 'org.mozilla.firefox',
        'UCMobile': 'com.UCMobile.intl'
    }

    with open('urls.txt', 'r') as f:
        for num, domain in enumerate(f, start=1):
            domain = domain.rstrip('\n')
            subprocess.call([open_cmd.format(domain=domain,
                             browser=browser_dict_start[browser])], shell=True)
            sleep(60)
            # take a screenshot and save it as 'firefox/domainname.png', etc.
            subprocess.call([
                screenshot_cmd + ' > screenshots/' + browser + '/' +
                domain + '.png'], shell=True)
            # kill the app
            subprocess.call([kill_cmd.format(
                browser=browser_dict_stop[browser])], shell=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--browser', default='firefox',
                        choices=['chrome-dev', 'firefox', 'chrome', 'fennec', 'UCMobile'],
                        help='Choose which browser to run.')
    args = parser.parse_args()

    if args.browser:
        run(args.browser)

