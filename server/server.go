package main

import (
	"email-grpc-service/server/email/handler"
	"email-grpc-service/server/protos"
	"fmt"
	"google.golang.org/grpc"
	"net"
)

func main() {
	//创建服务
	rpcSrv := grpc.NewServer()
	email.RegisterEmailServer(rpcSrv, new(handler.Handler))
	lis, _ := net.Listen("tcp", ":0865")
	ret := rpcSrv.Serve(lis)
	if ret != nil {
		fmt.Println("ret is ", ret)
	}
}
