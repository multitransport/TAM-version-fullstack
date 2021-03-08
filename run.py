import multitransport.app as app
from apscheduler.schedulers.background import BackgroundScheduler
sched = BackgroundScheduler(daemon=True)
sched.add_job(main,'interval',seconds=59)
sched.start()


if __name__ == '__main__':
    app.app.run(debug=True)
