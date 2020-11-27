import grpc

from proto.email_msg import email_msg_pb2, email_msg_pb2_grpc

def main():
    with grpc.insecure_channel("localhost:0865") as channel:
        client = email_msg_pb2_grpc.EmailStub(channel=channel)
        ret = client.SendEmail(
            email_msg_pb2.SendEmailRequest(
                to="15521370865@163.com",
                subject="grpc test",
                content="this is content"
            ))
        print(f"ret is {ret}")


if __name__ == '__main__':
    main()
