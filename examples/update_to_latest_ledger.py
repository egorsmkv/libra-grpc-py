import grpc

from lib.admission_control_pb2_grpc import AdmissionControlStub
from lib.get_with_proof_pb2 import UpdateToLatestLedgerRequest
from examples.config import SERVER_ADDRESS


def run():
    channel = grpc.insecure_channel(SERVER_ADDRESS)
    stub = AdmissionControlStub(channel)

    request = UpdateToLatestLedgerRequest(client_known_version=0, requested_items=[])
    response = stub.UpdateToLatestLedger(request)

    ledger_info = response.ledger_info_with_sigs.ledger_info
    print('version:', ledger_info.version)
    print('consensus_data_hash:', ledger_info.consensus_data_hash.hex())
    print('consensus_block_id:', ledger_info.consensus_block_id.hex())
    print()

    signatures = response.ledger_info_with_sigs.signatures
    for item in signatures:
        print('Validator ID:', item.validator_id.hex())
        print('Signature:', item.signature.hex())
        print()


if __name__ == '__main__':
    run()
