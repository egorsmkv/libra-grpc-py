# gRPC client for Libra in Python

This project contains generated gRPC files to establish a connection
to the Testnet of the Libra network developed by Facebook.

You can look how it seems in action by code from the examples directory.

## Installation

1. Clone the repository

```
git clone git@github.com:egorsmkv/libra-grpc-py.git
```

2. Install pipenv
3. Init a virtualenv

```
pipenv install
pipenv shell
```

4. Set `PYTHONPATH` to the current directory.

```
export PYTHONPATH=`pwd`
```

## Usage

Now you can run any examples, like the following:

```
python examples/update_to_latest_ledger.py
```

Output:

```
version: 112826
consensus_data_hash: ce322b10213f5b793692d12db71022e84389c09e8337d4f62f64862817b0e70d
consensus_block_id: 252d8108314178cfab56a8497ca3581634a7406304d8b871fd2ea82ab32712d7

Validator ID: 4d78ab90b759ecacafe4e687c5db9cc2936a7a29c84aa8be777f54db519d756b
Signature: 6b88627cfcad5ca37446c1af4e95317dad0a712424229fd98cf4bcd31bef3d30107b6cbc8fea1cfac0b43dad144b927dfd687dd6e0e175a481766ff48fd89d04

Validator ID: 9102bd7b1ad7e8f31023c500371cc7d2971758b450cfa89c003efb3ab192a4b8
Signature: d0acd6c5d920bf6c1bde133875f9057424ff257c0b38efe9a9000435bcfbcced4eba8bde2baa0624d39752c72a301e4a1272534e0b2bc3e81239143697dd3006

Validator ID: 4995559c4844b7e4101c486035329402a8ba4976c1be23080bac5bddf6a60f0d
Signature: 7e93d2cb447b0a8bcf133a5ccf9c3e18267e5301e5c873a78000ff24450282fa7fa7ea5e82eb108fa01da2d7c61a0455b4f3548e4092091f0f43f040eeda0300

Validator ID: 26873decd9330065988b0acf5027662b5097fb50913ae2a2652b50a9869df4fb
Signature: 62ae640822f74b50d6450a19a64719c6e3148e9e997321092ee5bc346e6e20a31a144ec4ae1d4fdbd2ad4c779adf8cfa1ad55c6e26acfcfa9ee4cf3769836e02

Validator ID: 6687e9a6e6c3de0dc4f7e91eacbc676a228a9c0c46450bbccbd1072780bfcb30
Signature: d3e14e8478bae6335e10ef8102033979611657a483593275381d6caaeff81afba6e4d7e146d8e7837f61097b629145a445835ddb08fa3541d8c6fa0253c43106

Validator ID: dfb9c683d1788857e961160f28d4c9c79b23f042c80f770f37f0f93ee5fa6a96
Signature: bfe68c928d73a17091158a171e9a12879dfae4f5d0c4f67beac031fac75f003db6c07584bf2129a1a8bda90994e52cc54811017e0a97f52b8e667190cff48901

Validator ID: 19f93314cbe8c0925a4492eb2f2f197ce6e11717449c218f50e043e37fa7a5f3
Signature: c1ccd3585c23e3140ae864c065449f763d3dc20c57f9729440d840ccc0a366364e8dd3ff5ce73585e36279a06d7047159110ec5fc26d43e80a2e758902cd2801
```

### Other information

- The project requires Python 3.
- License: Apache 2.0, see the LICENSE.md file.
