#!/usr/bin/env python
#
# Bootstrap script
# ===========================================

import glob
import os


# Path to this file
SELF_PATH = os.path.dirname(os.path.abspath(__file__))

EXPLICIT_SYMLINKS = {
    'ghostty/config': '~/Library/Application Support/com.mitchellh.ghostty/config',
}


def create_symlinks():
    'Create the symlinks on user home'
    always_overwrite = False

    for origin, destine in symlink_targets():

        if os.path.lexists(destine):
            if os.path.islink(destine) and os.readlink(destine) == origin:
                continue

            # Ask the user if overwrite the file
            if not always_overwrite:
                answer = confirm_overwrite(destine)
                always_overwrite = answer == 'a'
            else:
                answer = 'a'

            # Remove the file if the user answered yes
            if always_overwrite or answer in ('y', 'a'):
                os.remove(destine)

            # Keep the file if the user answered no
            if answer == 'n':
                continue

        # Create the symlink
        os.makedirs(os.path.dirname(destine), exist_ok=True)
        os.symlink(origin, destine)


def symlink_targets():
    'Return generic and explicit symlink origin/destination pairs'
    for symlink in glob.glob('*/*.symlink'):
        origin = os.path.join(SELF_PATH, symlink)
        filename = '.' + os.path.splitext(os.path.basename(symlink))[0]
        destine = os.path.expanduser(os.path.join('~', filename))
        yield origin, destine

    for source, target in EXPLICIT_SYMLINKS.items():
        origin = os.path.join(SELF_PATH, source)
        destine = os.path.expanduser(target)
        yield origin, destine


def confirm_overwrite(path):
    'Ask the user to overwrite a file'
    while True:
        answer = input('%s exists, overwrite it? (a/y/n) ' %
                           os.path.basename(path))

        if answer in ('y', 'n', 'a'):
            break

    return answer


if __name__ == '__main__':
    os.chdir(SELF_PATH)
    create_symlinks()
