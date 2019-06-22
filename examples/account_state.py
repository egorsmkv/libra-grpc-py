import grpc

from lib.admission_control_pb2_grpc import AdmissionControlStub
from lib.get_with_proof_pb2 import UpdateToLatestLedgerRequest, GetAccountStateRequest, RequestItem
from examples.config import SERVER_ADDRESS

ADDRESS = '4bb23eb092a04fae7dea56fffb88322f993017e9bb8e9822cb441c80862d78e6'.encode('utf-8')


def run():
    channel = grpc.insecure_channel(SERVER_ADDRESS)
    stub = AdmissionControlStub(channel)

    account = GetAccountStateRequest(address=ADDRESS)
    item = RequestItem(get_account_state_request=account)
    request = UpdateToLatestLedgerRequest(client_known_version=113526, requested_items=[item])
    response = stub.UpdateToLatestLedger(request)

    print(response)


if __name__ == '__main__':
    run()
