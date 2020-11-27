package service

import (
	localConfig "email-grpc-service/server/config"
	newEmail "github.com/jordan-wright/email"
	"net/smtp"
)

func SendEmail(to string, subject string, content string) string{
	e := newEmail.NewEmail()
	c := localConfig.GetEmailCnfig()

	e.From = c.USER
	e.To = []string{to}
	e.Subject = subject
	e.Text = []byte(content)
	ret := e.Send(c.ADDR, smtp.PlainAuth("", c.USER, c.PASSWORD, c.HOST))
	if ret != nil {
		return "error"
	}
	return "ok"
}

