# record commands
if [ -n "${BASH_VERSION}" ]; then
trap "caller >/dev/null || \
printf '%s\n' \"\$(date '+%Y-%m-%dT%H:%M:%S%z') \$(pwd) \$\$ \
\$(tty) \${BASH_COMMAND}\" 2>/dev/null >> ~/.command_log/command.`date '+%Y%m%d'`" DEBUG
fi

# remember last directory
alias exit="pwd > ~/.last_dir ; exit"
cd `cat ~/.last_dir`

#${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[01;34m\] \w \$\[\033[00m\]

#
export PS1='${debian_chroot:+($debian_chroot)}\[\033[0;31m\]\t \[\033[0;36m\]\u\[\033[0;31m\]@\[\033[0;36m\]\h\[\033[0;33m\]:\[\033[0;31m\]\w\[\033[0;31m\]\[\033[0;0m\] $ '
