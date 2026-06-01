#!/usr/bin/env python3
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
    linked = skipped = 0

    for origin, destination in symlink_targets():
        short = pretty_path(destination)

        if os.path.lexists(destination):
            if os.path.islink(destination) and os.readlink(destination) == origin:
                print('skipped %s (already linked)' % short)
                skipped += 1
                continue

            # Ask the user if overwrite the file
            if not always_overwrite:
                answer = confirm_overwrite(destination)
                always_overwrite = answer == 'a'
            else:
                answer = 'a'

            # Keep the file if the user answered no
            if answer == 'n':
                print('skipped %s (kept existing)' % short)
                skipped += 1
                continue

            # Remove the file if the user answered yes
            os.remove(destination)

        # Create the symlink
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        os.symlink(origin, destination)
        print('linked  %s -> %s' % (short, origin))
        linked += 1

    print('\ndone: %d linked, %d skipped' % (linked, skipped))


def pretty_path(path):
    'Shorten a path under the user home to a ~-prefixed form'
    home = os.path.expanduser('~')
    if path.startswith(home + os.sep):
        return '~' + path[len(home):]
    return path


def symlink_targets():
    'Return generic and explicit symlink origin/destination pairs'
    for symlink in glob.glob('*/*.symlink'):
        origin = os.path.join(SELF_PATH, symlink)
        filename = '.' + os.path.splitext(os.path.basename(symlink))[0]
        destination = os.path.expanduser(os.path.join('~', filename))
        yield origin, destination

    for source, target in EXPLICIT_SYMLINKS.items():
        origin = os.path.join(SELF_PATH, source)
        destination = os.path.expanduser(target)
        yield origin, destination


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
