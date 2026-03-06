good = r"""
                             z
                              Z
                    .--.  Z Z
                   / _(c\   .-.     __
                  | / /  '-;   \'-'`  `\______
                  \_\/'/ __/ )  /  )   |      \--,
                  | \`""`__-/ .'--/   /--------\  \
                   \\`  ///-\/   /   /---;-.    '-'
                                (________\  \
                                          '-']
"""
print(good)
bad = r"""

                        .-------,
                     ../         \
                    /  ,   ,   ,  \
                   /  , \__\___\   \      
                  |   | __ || __',. \     
                  |   \_'_/ \_'_/.   |  
                  |  (|    v    |)   |    
                  ,    |       |    .   
                   |    \  ~  /     |   
                   |   /. | | .\    .
                   / ,/ |/   \| \,  |,
                  ( <-,  \___/  ,->   )
                   |  ,_ \   / _,  .|
                   | \  \ \ / /   / |
                   | |   \ * /    | |
                   | |     #      | |

"""
print(bad)
guard_awake = False
if not guard_awake:
    outcome = "Shadow: lets hurry past him before he wakes up."
else:
    outcome = "Doom: be quiet he's awake."
print(outcome)
