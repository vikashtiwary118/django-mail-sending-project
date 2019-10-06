import threading
from django.core.mail import EmailMessage
# Create your views here.
from .forms import ContactForm
from django.shortcuts import render
import schedule
import time
from mailings.models import EmailTable
from datetime import date,timedelta

def send_mails(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            email = request.POST.get("mails")
            body = request.POST.get("body")
            subject = request.POST.get("subjects")

            ccs = request.POST.get("cc")
            bccs = request.POST.get("bcc")
            

            try:
                files = request.FILES["csv_file"]
            except Exception as e:
                files=None


            sendfrom = "ss"
            sendto = [email]
            cc = [ccs]
            bcc = [bccs]
            subject = subject
            text = (
                body
            )

            for to in sendto:
                MailThread(sendfrom, to, subject, text, cc, bcc, files).start()
                obj = EmailTable()
                obj.receiver = to
                obj.subject = subject
                obj.body = body
                obj.cc=cc
                obj.bcc=bcc
                obj.save()
    else:
        form = ContactForm()
    return render(request,'mailings/send_mail.html',{"form":form})


class MailThread(threading.Thread):
    def __init__(self, send_from, send_to, subject, text, cc, bcc, files):
        self.send_from = send_from
        self.send_to = send_to
        self.subject = subject
        self.text = text
        self.cc = cc
        self.bcc = bcc
        self.files = files
        threading.Thread.__init__(self)

    def send_mail(
        self, send_from, send_to, subject, text, cc, bcc, files=None, server="127.0.0.1"
    ):

        try:
            email = EmailMessage(subject, text, "info@letseduvate.com", [send_to])
            try:
                try:
                    docfile = open(files, "rb")
                    if docfile:
                        email.attach(docfile.name, docfile.read())
                except Exception as e:
                    print(e)
                email.send()
                print("Email send successfully")
            except Exception as e:
                print(e)
                print("mail not send")

        except Exception as e:
            print(e)

    def run(self):
        self.send_mail(
            self.send_from, self.send_to, self.subject, self.text, self.cc, self.bcc, self.files
        )




def sendAdminMail(request):
    today = date.today()
    all_data=EmailTable.objects.filter(timestamp=today)
    data_information=[]
    for d in all_data:
        data_information.append({"receiver":d.receiver,"subject":d.subject,"body":d.body,"cc":d.cc,"bcc":d.bcc,"timestamp":d.timestamp})
    sendfrom = "ss"
    sendto = ["vikashtiwary060@gmail.com"]
    cc = []
    bcc = []
    subject = "admin email"
    text = str(data_information)
    files=None

    for to in sendto:
        MailThread(sendfrom, to, subject, text, cc, bcc, files).start()
    schedule.every(30).minutes.do(sendAdminMail)

    while True:
        schedule.run_pending()
        time.sleep(1) 
