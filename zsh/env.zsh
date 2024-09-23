export PATH="/usr/local/bin:$PATH:$DOTFILES/bin:/usr/local/share/npm/bin:/usr/local/share/python"
export EDITOR='vim'

# Colors
export CLICOLOR=1
export LSCOLORS=gxfxcxdxbxegedabagacad
export LS_COLORS='di=36:fi=0:ln=35:pi=5:so=5:bd=5:cd=5:or=0;41:mi=0:ex=31'

export HOMEBREW_NO_ANALYTICS=1


if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi

