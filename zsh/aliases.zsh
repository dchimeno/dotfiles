

# ls aliases
alias l="ls -l"
alias ll="ls -alh"
alias la="ls -A"
alias lla="ls -lA"

# Generic aliases
alias grep="grep --color=auto"
alias reload='. ~/.zshrc'


# Homebrew
brewsize() {
  local cellar
  local sort_cmd
  cellar="$(brew --cellar)" || return
  sort_cmd=sort
  command -v gsort >/dev/null && sort_cmd=gsort
  du -hs "$cellar"/* | "$sort_cmd" -h
}
alias brews='brew list -1'
alias bubo='brew update && brew outdated'
alias bubc='brew upgrade && brew upgrade && brew cleanup'
alias bubu='bubo && bubc'
alias bdumpwork='brew bundle dump --file=$DOTFILES/homebrew/work/Brewfile --force'
alias bdumpmachost='brew bundle dump --file=$DOTFILES/homebrew/machost/Brewfile --force'

# Empty the Trash on all mounted volumes and the main HDD.
# Also, clear Apple’s System Logs to improve shell startup speed.
# Finally, clear download history from quarantine. https://mths.be/bum
alias emptytrash="sudo rm -rfv /Volumes/*/.Trashes; sudo rm -rfv ~/.Trash; sudo rm -rfv /private/var/log/asl/*.asl; sqlite3 ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV* 'delete from LSQuarantineEvent'"

alias path='echo -e ${PATH//:/\\n}'

# PS
alias psa="ps aux"
alias psg="ps aux | grep "
alias psp='ps aux | grep python'


# Docker
alias dkrstop='docker stop $(docker ps -aq)' # Stop all containers
alias dkrrm='docker rm $(docker ps -aq)' # Remove all containers
alias dkrrmimg='docker rmi $(docker images -q)' # Remove all images

alias cat="bat"

alias k="kubectl"


#other

alias jefri='ssh nasme -t "
  tmux has-session -t jefri 2>/dev/null \
  && tmux attach -t jefri \
  || tmux new-session -s jefri -c /home/daniel/sideprojects/jefri \; \
     send-keys \"claude --remote-control jefri\" Enter \; \
     split-window -v -c /home/daniel/sideprojects/jefri \; \
     send-keys \"uv run python manage.py runserver 0.0.0.0:8000\" Enter
"'
