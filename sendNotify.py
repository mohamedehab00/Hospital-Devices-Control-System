from win10toast import ToastNotifier


def send():
    Notify = ToastNotifier()
    Notify.show_toast("Hospital Control System", "Check Upcoming Repairs", icon_path=".//Images/Hospital.ico",
                      duration=(60 * 60 * 24), threaded=True)
