import multitransport.app as app
# from apscheduler.schedulers.background import BackgroundScheduler
# sched = BackgroundScheduler(daemon=True)
# sched.add_job(main,'interval',seconds=59)
# sched.start()


if __name__ == '__main__':
<<<<<<< HEAD
    app.app.run(host="0.0.0.0", port="5000", debug=True)
=======
    app.app.run(host="0.0.0.0")
    app.app.run(debug=True)
>>>>>>> 7ee58d765748e398fa1b885fa59ea258fcc1144c
