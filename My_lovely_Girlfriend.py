import time
import webbrowser

def happy_birthday():
    print("Happy  Birthday to my lovely girlfriend! Luwam-(Metay<3) (^_^) ❤️" "🐦")
    time.sleep(2)
    print("Here's a surprise for you! But first lets play around, What's your favorite English Premier League team? (all lowercase letters)")
    time.sleep(2)
    answer = input("Favorite English Premier League team: ")
    if answer.lower() == "manchester united":
        print("Congratulations, Though that is a Very MID team!!! it may be an excellent choice! I have a surprise for you babe its is the first of two gift!")
        time.sleep(2)
        print("Get ready! I'm counting down from 20...")
        for i in range(20, 0, -1):
            print(i)
            time.sleep(1)

        print("Before you click the link below i want to know that you are a really special in my life and  that i am really grateful to have you in my life. I want more memories of us together")
        print("I sorry i hav have been acting wierd lately and i am sorry if i made you sad tonight i just wanted to spend more time with you okay")
        print("Surprise! Click this link to enjoy your gift:")
        time.sleep(1)
        webbrowser.open("https://open.spotify.com/playlist/496aYubYufmDoiFQXR2Q0Z?si=5Est3hO1ReaU8qNDvo60HA")
    else:
        print("Oh, nice choice! Definately better than Man U But I have a surprise for you anyway!")
        time.sleep(1)
        print("Get ready! I'm counting down from 10...")
        for i in range(10, 0, -1):
            print(i)
            time.sleep(1)
        print("Surprise! Click this link to enjoy your gift:")
        time.sleep(1)
        webbrowser.open("https://open.spotify.com/playlist/496aYubYufmDoiFQXR2Q0Z?si=5Est3hO1ReaU8qNDvo60HA")

happy_birthday()
