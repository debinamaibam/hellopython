import webbrowser
import time
#print("hello world in python")
#a="nielit"
#print(a)

list = ["https://www.youtube.com/watch?v=rBbPvaAFzxo",
"https://www.youtube.com",
"https://www.youtube.com/watch?v=rBbPvaAFzxo"]
i=0
while(i<3):
    time.sleep(5)
    webbrowser.open_new(list[i])
    i = i+1

