from datetime import datetime
import speedtest
import autoemail
title = "Netspeed test"
today_date = datetime.now()
hours = today_date.hour
minutes = today_date.minute
speedtester = speedtest.Speedtest()
download = (round(speedtester.download()) / 1000000)
upload = (round(speedtester.upload() / 1000000))
email = "windows internet stats Download speed {} mb and upload speed is {} at {} hours {} minites ".format(download,
                                                                                                            upload,
                                                                                                            hours,
                                                                                                            minutes)

autoemail.send(title, email)
print(autoemail.msg)

