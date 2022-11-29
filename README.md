# chimeno does dotfiles

## dotfiles

Your dotfiles are how you personalize your system. These are mine.


## Install

- `git clone git://github.com/dchimeno/dotfiles ~/.dotfiles`
- `cd ~/.dotfiles`
- `git submodule init`
- `git submodule update`
- `python3 bootstrap.py`
- `chsh -s /bin/zsh` # Change shell in case you're using another one

This will symlink the appropriate files in `.dotfiles` to your home directory.
Everything is configured and tweaked within `~/.dotfiles`.

The main file you'll want to change right off the bat is `zsh/zshrc.symlink`,
which sets up a few paths that'll be different on your particular machine.


## Components

There's a few special files in the hierarchy.

- **bin/**: Anything in `bin/` will get added to your `$PATH` and be made
  available everywhere.
- **topic/\*.zsh**: Any files ending in `.zsh` get loaded into your
  environment.
- **topic/\*.symlink**: Any files ending in `*.symlink` get symlinked into
  your `$HOME`. This is so you can keep all of those versioned in your dotfiles
  but still keep those autoloaded files in your home directory. These get
  symlinked in when you run `python3 bootstrap.py`.


## Recommended software

Software that it is not necessary to have but you should.

- [Brew](http://brew.sh/)
- [Python3](https://www.python.org)

## Fonts
Install fonts in the /fonts/ folder
In case of iterm2, set the font on Preferences / Profiles / Fonts (Both Font and NON-ASCII Font)

## Recommended packages

Install brew and then, inside the ``homebrew/<machine>/`` directory run:

``brew bundle install``

To record all installed packages to a file, use:

``brew bundle dump --force --file=$DOTFILES/homebrew/[machost,work]/Brewfile``


## Configure git
To configure git, you need to create a ``git/gitconfigpersonal`` and or ``git/gitconfigwork`` files
in order to configure git according to the environment you use.
More info in the first lines of the ``git/gitconfig.symlink` file.

## Secret

Put secrets in $DOTFILES/.localrc


## Update
In order to update submodules, run:
`git submodule update --recursive --remote`
