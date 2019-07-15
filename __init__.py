"""
Author: Soufiane Alami
Email: inobody135@gmail.com

"""
import logging, logging.handlers

from logging.handlers import SMTPHandler


class SMTP_SSLHandler(SMTPHandler):
    def __init__(self, mailhost, fromaddr, toaddrs, subject, credentials=None, secure=None):
        super(SMTP_SSLHandler, self).__init__(mailhost, fromaddr, toaddrs, subject, credentials, secure)


    def emit(self, record):
        try:
            import smtplib
            from email.utils import formatdate
            port = self.mailport
            if not port:
                port = smtplib.SMTP_PORT
            smtp = smtplib.SMTP_SSL(self.mailhost, port)
            msg = self.format(record)
            msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s" % (self.fromaddr, ", ".join(self.toaddrs), self.getSubject(record), formatdate(), msg)
            if self.username:
                smtp.ehlo()
                smtp.login(self.username, self.password)
            smtp.sendmail(self.fromaddr, self.toaddrs, msg)
            smtp.quit()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

logger = logging.getLogger()
logger.addHandler(SMTP_SSLHandler(mailhost=['smtp.host.com', 465],
                            fromaddr='from@email.com',
                            toaddrs=['to@email.com'],
                            subject='Exceptional Log',
                            credentials=['user', 'pass'],
                            secure=()))

logger.exception('You Just Got An Email')
try:
    a = 0/0
except Exception as e:
    logger.exception(e)
