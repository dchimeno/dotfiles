# Repository Guidelines

## Project Structure & Module Organization

This repository manages macOS dotfiles and utilities. Files named `*.symlink` are linked into `$HOME` by `bootstrap.py` as hidden dotfiles, for example `zsh/zshrc.symlink` becomes `~/.zshrc`. Files named `*.zsh` under topic directories are sourced by zsh startup.

- `bin/`: command-line utilities added to `$PATH`.
- `zsh/`: shell environment, aliases, Oh My Zsh customizations, and vendored themes/plugins.
- `git/`: global Git config, ignores, and helper commands.
- `homebrew/<machine>/Brewfile`: per-machine Homebrew bundles.
- `python/`, `vim/`, `ghostty/`, `osx/`, `fonts/`: tool-specific configuration and assets.

### Runtime Loading & Environment

Zsh startup order (driven by `zsh/zshrc.symlink`):

1. `zsh/zshrc.symlink` exports `$DOTFILES`, `$ZSH`, and the `powerlevel9k` theme.
2. Every `*/*.zsh` file under `$DOTFILES` is sourced (glob, de-duplicated).
3. `~/.localrc` is sourced if present (machine-specific secrets, not versioned).
4. Oh My Zsh is loaded from the `zsh/ohmyzsh.git` submodule.

Key environment variables: `$DOTFILES` (`~/.dotfiles`), `$ZSH` (`$DOTFILES/zsh/ohmyzsh.git`), `$PROJECTS` (`~/Documents/projects/`). `bin/` is prepended to `$PATH` by `zsh/env.zsh`.

## Build, Test, and Development Commands

- `python3 bootstrap.py`: create or refresh symlinks from `*/*.symlink` into `$HOME`.
- `git submodule init && git submodule update`: initialize vendored plugins and themes after cloning.
- `git submodule update --recursive --remote`: update all submodules.
- `pre-commit install`: enable local hooks.
- `pre-commit run --all-files`: run formatting, linting, and repository hygiene checks.
- `cd homebrew/<machine> && brew bundle install`: install packages for a specific machine.
- `brew bundle dump --force --file=$DOTFILES/homebrew/<machine>/Brewfile`: update a Brewfile after package changes.

## Coding Style & Naming Conventions

Shell formatting is enforced by `shfmt` with 2-space indentation and case indentation (`-i 2 -ci -w`). Shell scripts in `bin/` should be executable, start with an appropriate shebang, and use clear lower-case command names such as `monitor_url` or `curltime`. Keep zsh-only behavior in `.zsh` files and portable helpers in `.sh`, `.bash`, or `bin/` scripts. Use the established `topic/name.symlink` pattern for dotfiles intended for `$HOME`.

## Testing Guidelines

There is no single application test suite. Treat `pre-commit run --all-files` as the baseline validation before committing. For shell changes, prefer running the changed script directly with representative inputs and fix ShellCheck warnings where the hook applies. If editing vendored `powerlevel9k` content, use its local test documentation and scripts, such as `zsh/custom/themes/powerlevel9k/test-in-docker`, when relevant.

## Commit & Pull Request Guidelines

Git history uses short, lower-case, imperative or descriptive commit subjects, for example `add fzf`, `add monitor_url`, or `updated submodules`. Keep commits focused by component. Pull requests should describe the changed area, list validation performed, call out submodule or Brewfile updates, and note any user-visible shell, prompt, or symlink behavior changes. Include screenshots only for visual terminal or prompt changes.

## Security & Configuration Tips

Do not commit secrets, tokens, host-specific credentials, or private keys. Put local secrets and machine-specific exports in `$DOTFILES/.localrc` or `~/.localrc`. Create `git/gitconfigpersonal` and `git/gitconfigwork` locally when needed; they are intentionally not versioned.
