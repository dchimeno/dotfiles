

# ls aliases
alias l="ls"
alias ll="ls -l"
alias la="ls -A"
alias lla="ls -lA"

# Generic aliases
alias grep="grep --color=auto"
alias reload='. ~/.zshrc'

# cd into Development folder
alias d="cd $PROJECTS"


#Run ipython inside virtualenv
alias ipy="python -c 'import IPython; IPython.terminal.ipapp.launch_new_instance()'"

#vagrant up & vagrant ssh
alias vus="vagrant up && vagrant ssh"

#make sure pip not uses glob zsh pattern
#https://stackoverflow.com/questions/30539798/zsh-no-matches-found-requestssecurity
alias pip='noglob pip'

alias brewsize="du -hs /usr/local/Cellar/* | gsort -h"