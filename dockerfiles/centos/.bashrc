# .bashrc

# User specific aliases and functions

alias c='clear'
alias h='history'
alias df='df -h'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias ls='ls -asCF --color=auto'
alias ll='ls -alF --color=auto'

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

export PS1='[\[\e[1;31m\]\u\[\e[m\] \[\e[1;36m\]\w\[\e[m\]]\$ '
