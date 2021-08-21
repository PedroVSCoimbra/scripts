#!/bin/sh

# A dwm_bar function to display information regarding system memory, CPU temperature, and storage
# Joe Standring <git@joestandring.com>
# GNU GPLv3

dwm_resources () {
    # Used and total memory
    MEMUSED=$(free -h | awk '(NR == 2) {print $3}' | sed 's/i/b/')
    MEMTOT=$(free -h |awk '(NR == 2) {print $2}' | sed 's/i/b/')
    # CPU temperature
    CPU=$(sensors | grep Pa | awk '{printf $4}' | sed 's/+//')

    printf "%s" "$SEP1"
    if [ "$IDENTIFIER" = "unicode" ]; then
        printf "💻 MEM %s/%s CPU %s" "$MEMUSED" "$MEMTOT" "$CPU"
    else
        printf "STA | MEM %s/%s CPU %s" "$MEMUSED" "$MEMTOT" "$CPU"
    fi
    printf "%s\n" "$SEP2"
}

dwm_resources

# Used and total storage in /home (rounded to 1024B)
#STOUSED=$(df -h | grep '/home$' | awk '{print $3}')
#STOTOT=$(df -h | grep '/home$' | awk '{print $2}')
#STOPER=$(df -h | grep '/home$' | awk '{print $5}')
