#!/bin/sh

# A dwm_bar function to print the weather from wttr.in
# Joe Standring <git@joestandring.com>
# GNU GPLv3

# Dependencies: curl

# Change the value of LOCATION to match your city
dwm_weather() {
    printf "%s" "$SEP1"
    if [ "$IDENTIFIER" = "unicode" ]; then
        printf "%s" "$(curl -s wttr.in?format=4)"
    else
        printf "WEA %s" "$(curl -s wttr.in/?format=4 | grep -o "[0-9].*")"
    fi
    printf "%s\n" "$SEP2"
}

dwm_weather
