package handler

import (
	"context"
	service "email-grpc-service/server/email/service"
	"email-grpc-service/server/protos"
	"fmt"
)

type Handler struct {
}

func (h *Handler) SendEmail(ctx context.Context, req *email.SendEmailRequest) (*email.SendEmailResponse, error) {
	ret := service.SendEmail(req.To, req.Subject, req.Content)
	fmt.Println("ret is ", ret)
	return &email.SendEmailResponse{Message: "ret"}, nil
}
