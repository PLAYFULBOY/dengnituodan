import werobot

robot = werobot.WeRoBot(token='dengnituodan')

@robot.text
def hello_world():
    return 'Hello World!'

robot.run()