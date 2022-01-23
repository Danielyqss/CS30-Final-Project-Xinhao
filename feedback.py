def give_feedback():
    feedbacks = {"Your point is between 40-60":
                 {"Your a very healthy person, enjoy your life!\n"},
                 "Your point is between 20-60":
                 {"You are at the middle of the bridge, make more\
                  \nfriends, find things to do that will relax you, and\
                  \ndon't get too hung up on unhappy things!\n"},
                 "Your point is blow 20":
                 {"I'm sorry that you mental health is not so good\
                  \nbut here is some advance that would help! 1.You\
                  \ncan go to http://www.camh.ca' look for professinal\
                  \nhelp! 2.Don't be afraid to talk about your feelings\
                  \nwith your family and friend! 3.It's hard but try to\
                  \nthink positively and believe things will turn better!\n"
                 }}
    for helps in feedbacks:
        print(f"{helps}")
        for item in feedbacks[helps]:
            print(f"{item}")