def swith_func():
    """
    allows the user to turn devices on/off
    and displays the current settings

    """
    try:
        while True:
            user_asc = int(input("""
            1 - power|on
            2 - light|on
            3 - computer|on
            4 - monitor|on
            5 - show settings
            >>>
            """
                         )
                       )
            global swith
            if user_asc == 1:
                swith |= 0b0001
                print('power on')
            elif user_asc == 2:
                swith |= 0b0010
                print('light on')
            elif user_asc == 3:
                swith |= 0b0100
                print('computer on')
            elif user_asc == 4:
                swith |= 0b1000
                print('monitor on')
            elif user_asc == 5:
                status.clear()
                if swith & 0b0001:
                    status.append('power')
                if swith & 0b0010:
                    status.append('light')
                if swith & 0b0100:
                    status.append('computer')
                if swith & 0b1000:
                    status.append('monitor')
                print(status)
    except KeyboardInterrupt:
        print("goodbye")


if __name__ == "__main__":
    status = []
    swith = 0b0000
    swith_func()